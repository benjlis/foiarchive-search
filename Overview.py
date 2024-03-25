import streamlit as st
import configs as c
c.page("Overview")    # must be 1st streamlit cmd or strange behavior ensues
import sqlgen as sg
import db

"""
The Freedom of Information Archive (FOIArchive) is a collection of documents
obtained through the Freedom of Information Act (FOIA) and other public 
records requests. The documents are primarily from the U.S. government but
include materials from other countries. Its focus is on international 
relations. The collection is a work in progress, with new documents added as
they are obtained and processed. 
"""

# display metrics
totals_sql = sg.query('totals', 'foiarchive.totals', None)
totals_df = db.execute(totals_sql)
doc_cnt, pg_cnt, word_cnt = totals_df.iloc[0] 
col1, col2, col3 = st.columns(3)
col1.metric(label="**Documents**", value=f"{doc_cnt:,}", delta=None)
col2.metric(label="**Pages**", value=f"{pg_cnt:,}", delta=None)
col3.metric(label="**Words**", value=f"{word_cnt:,}", delta=None)
# display metrics over time

totals_sql = sg.query('totals', 'foiarchive.totals_decade', None)
totals_df = db.execute(totals_sql)
totals_df.rename(columns={'decade':'Decade',
                          'word_cnt': 'Words',
                          'pg_cnt': 'Pages',
                          'doc_cnt': 'Documents'}, 
                 inplace=True)
metrics =['Documents', 'Pages', 'Words']
metric = st.radio('**Metric**', metrics, index=2,
                  horizontal=True,
                  label_visibility='collapsed')
st.bar_chart(data=totals_df, x='Decade', y=metric, use_container_width=True)
"""
The FOIArchive is composed of numerous corpora.
"""
cdf = db.load_execute("corpora")
st.dataframe(cdf, 
             hide_index=True,
             use_container_width=True, 
             column_config={
                "corpus": "Corpus",
                "title": "Title",
                "begin_date": "Starts",
                "end_date": "Ends",
                "doc_cnt": "Documents",
                "pg_cnt": "Pages",
                "word_cnt": "Words",
                "topic_cnt": "Topics"})
with open(c.config["corpora_description"], "r") as f:
    st.markdown(f.read())
c.footer()