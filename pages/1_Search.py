import streamlit as st
import configs as c 
c.page("Search")    # must be 1st streamlit cmd or strange behavior ensues
import datetime
import sqlgen as sg
import db

# GUI search widgets
# get values to populate values and ranges
classification_lovs = db.get_lov("classifications", "classification")
corpora_lovs = db.get_lov("corpora", "corpus")
MIN_AUTHORED = datetime.date(1861, 5, 1)
MAX_AUTHORED = datetime.date(2013, 7, 8)
entities_df = db.load_execute('entities')

#
# display widgets
search_str = st.text_input(label_visibility="visible",
                           label="Full-Text",
                           placeholder="Enter search terms",
                           help=c.config['search_str_help'],
                           value=st.query_params.get('qry'))
col1, col2, col3, col4, col5 = st.columns(5)

persons = col1.multiselect("Person(s)", 
                         entities_df[entities_df['entgroup'] == 'PERSON']['entity_dropdown_str'], 
                         placeholder="Persons Placeholder",
                         help="Persons Help")
orgs = col2.multiselect("Organization(s)", 
                         entities_df[entities_df['entgroup'] == 'ORG']['entity_dropdown_str'], 
                         placeholder="Organizations Placeholder",
                         help="Organizations Help")
locations = col3.multiselect("Location(s)", 
                         entities_df[entities_df['entgroup'] == 'LOC']['entity_dropdown_str'], 
                         placeholder="Locations Placeholder",
                         help="Locations Help")
govts = col4.multiselect("Government(s)", 
                         entities_df[entities_df['entgroup'] == 'GOVT']['entity_dropdown_str'], 
                         placeholder="Governments Placeholder",
                         help="Governmentss Help")
others = col5.multiselect("Other(s)", 
                         entities_df[entities_df['entgroup'] == 'OTHER']['entity_dropdown_str'], 
                         placeholder="Others Placeholder",
                         help="Others Help")
corpora = col1.multiselect("Corpus", 
                           corpora_lovs,
                           placeholder=c.config['corpus_placeholder'])
classifications = col2.multiselect("Original Classification:", 
                                   classification_lovs,
                                   placeholder=
                                    c.config['classification_placeholder'],
                                   help=c.config['classification_help'])
dates = col3.date_input("Date Range", value=[], 
                        min_value=MIN_AUTHORED, max_value=MAX_AUTHORED,
                        help=c.config['date_help'])
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
query_display = where_clause.replace("full_text @@ websearch_to_tsquery('english',", 
                                     "search(")
if query_display:
    st.divider()
    st.caption(":grey[Query Criteria]")
    st.code(f"{query_display}", language="sql")
    print(f'query|{datetime.datetime.now()}|{query_display}', flush=True)
    # display metrics
    metrics_sql = sg.query('metrics', c.config["table_name"], where_clause)
    metrics_df = db.execute(metrics_sql)
    metrics = metrics_df.iloc[0] 
    st.metric(label="Documents Found", value=f"{metrics['doc_cnt']:,}", delta=None)
    # if there are results, execute bar_chart and possibly other queries 
    if metrics['doc_cnt']:
        aggdate, x_axis_label = sg.aggdate_expr('authored', metrics)
        bar_chart_sql = sg.aggquery('bar_chart', c.config["table_name"], 
                                    where_clause, aggdate)
        bar_chart_df = db.execute(bar_chart_sql)
        bar_chart_df.rename(columns={'Date': x_axis_label}, inplace=True)
        st.bar_chart(data=bar_chart_df, x=x_axis_label, y="Documents", color="Corpus",
                    use_container_width=True)    
        if metrics['doc_cnt'] > c.config["max_rows"]:
            st.caption(f"**Note:** Queries of {c.config['max_rows']} \
                    documents or less return downloadable metadata and text.")
        else:
            data_table_sql = sg.query('data_table', c.config["table_name"], 
                                    where_clause)        
            data_table_df = db.execute(data_table_sql)
            data_table_df['docviewer_url'] = data_table_df['doc_id'].apply(
                lambda x: f"{c.config['docviewer_url']}?doc_id={x}")
            st.dataframe(data_table_df,
                         use_container_width=True, 
                         hide_index=True,
                         column_order=c.COLUMN_ORDER, 
                         column_config=c.COLUMN_CONFIGS)        
# Additional text for the sidebar footer
c.footer()
st.sidebar.write('You can find the previous version of the History Lab \
                 search screen [here](http://history-lab.org/search).')            