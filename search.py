import datetime
import tomli
import sqlgen as sg
import streamlit as st
# load configs
with open("appconfig.toml", mode="rb") as fp:
    config = tomli.load(fp)
# must be 1st streamlit cmd or strange behavior ensues
st.set_page_config(page_title=config["tab_title"],
                   page_icon=config["favicon"],
                   layout="wide",
                   menu_items={'Get Help': config["help_action"],
                               'Report a bug': config["bug_action"],
                               'About': f"### {config['gui_title']}\n" +
                                        f"{config['about_body']}"})
import column_configs as cf
import aggrid
import db
import footer

st.title(config['gui_title'])

# GUI search widgets
# get values to populate values and ranges
classification_lovs = db.get_lov("classifications", "classification")
corpora_lovs = db.get_lov("corpora", "corpus")
MIN_AUTHORED = datetime.date(1861, 5, 1)
MAX_AUTHORED = datetime.date(2013, 7, 8)
# display widgets
search_str = st.text_input(label=config['search_str_label'],
                           label_visibility="visible",
                           help=config['search_str_help'],
                           value=st.query_params.get('qry'))
col1, col2, col3 = st.columns(3)
corpora = col1.multiselect("Corpus", corpora_lovs)
classifications = col2.multiselect("Original Classification:", 
                                   classification_lovs)
dates = col3.date_input("Date Range", value=[], 
                        min_value=MIN_AUTHORED, max_value=MAX_AUTHORED) 
null_date = col3.checkbox("Include documents without a date", value=True)    
    

# Dynamic SQL generation
# build where clause
predicates = []
sg.add_predicate(predicates, sg.lov_predicate('corpus', corpora))
sg.add_predicate(predicates, sg.lov_predicate('classification', 
                                              classifications))
start_date, end_date = sg.convert_daterange(dates, "%Y/%m/%d")
sg.add_predicate(predicates, 
                 sg.daterange_predicate('authored',
                                        start_date, end_date, null_date, 
                                        MIN_AUTHORED, MAX_AUTHORED))
sg.add_predicate(predicates, sg.search_predicate('full_text', search_str))  
where_clause = sg.where_clause(predicates)

# display WHERE clause
st.divider()
query_display = where_clause.replace("full_text @@ websearch_to_tsquery('english',", 
                                     "search(")
if query_display:
    st.caption(":grey[Query Criteria]")
    st.code(f"{query_display}", language="sql")
    print(f'query|{datetime.datetime.now()}|{query_display}', flush=True)

# display metrics
metrics_sql = sg.query('metrics', config["table_name"], where_clause)
metrics_df = db.execute(metrics_sql)
metrics = metrics_df.iloc[0] 

st.metric(label="Documents Found", value=f"{metrics['doc_cnt']:,}", delta=None)
# if there are results, execute bar_chart and possibly other queries 
if metrics['doc_cnt']:
    aggdate, x_axis_label = sg.aggdate_expr('authored', metrics)
    bar_chart_sql = sg.aggquery('bar_chart', config["table_name"], 
                                 where_clause, aggdate)
    bar_chart_df = db.execute(bar_chart_sql)
    bar_chart_df.rename(columns={'Date': x_axis_label}, inplace=True)
    st.bar_chart(data=bar_chart_df, x=x_axis_label, y="Documents", color="Corpus",
                 use_container_width=True)    
    if metrics['doc_cnt'] > config["max_rows"]:
        st.caption(f"**Note:** Queries of {config['max_rows']} \
                 documents or less return downloadable metadata and text.")
    else:
        data_table_sql = sg.query('data_table', config["table_name"], 
                                  where_clause)        
        data_table_df = db.execute(data_table_sql)
        # st.dataframe(data=data_table_df, hide_index=True, 
        #              use_container_width=True, 
        #              column_config=cf.COLUMN_CONFIGS)
        selected = aggrid.grid(data_table_df)
        if selected:
            st.write(selected)
        st.caption("Double click cell to activate")

st.query_params.clear()
footer.display()