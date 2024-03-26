import streamlit as st
import configs as c
doc_id = st.query_params.get('doc_id') 
c.page(f"{doc_id}", display_menu=False)    # must be 1st streamlit cmd or strange behavior ensues
import datetime
import sqlgen as sg
import db


def display_date(date):
    if date:
        if date.time() == datetime.time(0, 0):
            date_str = f"{date.date().strftime('%b %d, %Y')}"
        else:
            date_str = f"{date.strftime('%b %d, %Y %H:%M:%S')}"
        st.markdown(f"**{date_str}**") 

def display_citation(title, corpus_name, doc_id):
    st.sidebar.markdown(f"### Citation:")
    citation_str = (f"{title}, _{corpus_name}_, Document ID Number: {doc_id}, "
                    "accessed on http://www.history-lab.org") 
    st.sidebar.markdown(citation_str)

def display_topics(doc_id):
    doc_topics_sql = sg.by_doc_id('doc_topics', doc_id)
    tdf = db.execute(doc_topics_sql)
    if not tdf.empty:
        st.sidebar.markdown("### Topic(s):")
        st.sidebar.dataframe(tdf, hide_index=True)

def display_source(source):
    if source:
        st.markdown(f"[Source Document PDF]({source})")

def display_frus_body(id):
    qry =(f"select body from docs_frus where doc_id = '{id}'")
    results = db.execute(qry)
    st.markdown(results.iloc[0]['body'], unsafe_allow_html=True)

def display_body(doc):
    if doc.body:
        if doc.corpus == 'frus':
            display_frus_body(doc.doc_id)
        else:
            st.text(doc.body)
    else:
        st.write("No document body")
 
def display_cnt(type, cnt):
    if cnt:
        st.sidebar.markdown(f"### {type}: {cnt}")

def display_doc(doc):
    st.subheader(doc.title)
    display_date(doc.authored)
    display_source(doc.source)
    display_body(doc)
    display_citation(doc.title, doc.corpus_title, doc.doc_id)
    st.sidebar.markdown(f"### Original Classification: {doc.classification}") 
    display_topics(doc.doc_id)
    display_cnt('Pages', doc.pg_cnt)
    display_cnt('Words', doc.word_cnt)

print(f'viewer|{datetime.datetime.now()}|{doc_id}', flush=True)    # logging
if doc_id:
    doc_sql = sg.by_doc_id('docviewer', doc_id)
    doc_df = db.execute(doc_sql)
    if doc_df.empty:
        st.warning(f"Warning: No document with ID {doc_id} found")
    else:                   # doc exists, display it
        display_doc(doc_df.iloc[0])
else:
    st.error("Error: No document ID provided")
c.footer()
