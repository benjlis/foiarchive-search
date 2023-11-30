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
import db

st.title(config['gui_title'])
# GUI search widgets
# get values to populate values and ranges
classification_lovs = db.get_lov("classifications", "classification")
corpora_lovs = db.get_lov("corpora", "corpus")
MIN_AUTHORED = datetime.date(1973, 10, 1)
MAX_AUTHORED = datetime.date(1973, 11, 1)
# display widgets
search_str = st.text_input(label=config['search_str_label'],
                           label_visibility="visible",
                           help=config['search_str_help'])
with st.expander("Additional search options"):
    col1, col2, col3 = st.columns(3)
    corpora = col1.multiselect("Corpus", corpora_lovs)
    classifications = col2.multiselect("Original Classification:", 
                                       classification_lovs)
    dates = col3.date_input("Date Range", value=(), min_value=MIN_AUTHORED,
                            max_value=MAX_AUTHORED)    
    
# Dynamic SQL generation
# build where clause
predicates = []
sg.add_predicate(predicates, sg.lov_predicate('corpus', corpora))
sg.add_predicate(predicates, sg.lov_predicate('classification', 
                                              classifications))
start_date, end_date = sg.convert_daterange(dates, "%Y/%m/%d")
sg.add_predicate(predicates, sg.compare_predicate('authored', ' >= ',
                                                  start_date))
sg.add_predicate(predicates, sg.compare_predicate('authored', ' <= ',
                                                  end_date))
sg.add_predicate(predicates, sg.search_predicate('full_text', search_str))  
where_clause = sg.where_clause(predicates)
# build queries
metrics_sql = sg.query('metrics', config["table_name"], where_clause)
bar_chart_sql = sg.query('bar_chart', config["table_name"], where_clause)
data_table_sql = sg.query('data_table', config["table_name"], where_clause)

# counts qry execution
metrics_df = db.execute(metrics_sql)
doc_cnt = metrics_df.iloc[0]['doccnt']
# display WHERE clause and counts
st.subheader(where_clause.replace("fts @@ websearch_to_tsquery('english',", 
                                  "search("))
st.metric(label="Documents Found", value=f"{doc_cnt:,}", delta=None)
# if there are results, execute bar_chart and possibly other queries 
if doc_cnt:
    bar_chart_df = db.execute(bar_chart_sql)
    st.bar_chart(data=bar_chart_df, x="Date", y="Documents", color="Corpus",
                 use_container_width=True)    
    if doc_cnt > config["max_rows"]:
        st.write(f"**Note:** Filter to {config['max_rows']} or \
                 less documents to see full details")
    else:
        data_table_df = db.execute(data_table_sql)
        st.dataframe(data=data_table_df, hide_index=True, 
                     use_container_width=True, 
                     column_config=cf.COLUMN_CONFIGS)
        st.caption("Double click cell to activate")            