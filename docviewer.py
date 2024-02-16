import streamlit as st
import db
import sqlgen as sg

def escape_markdown(text):
    """
    Replace characters that have special meaning in GitHub flavored Markdown.
    """
    text = text.replace('\\', '\\\\')
    text = text.replace('*', '\\*')
    text = text.replace('_', '\\_')
    text = text.replace('{', '\\{')
    text = text.replace('}', '\\}')
    text = text.replace('[', '\\[')
    text = text.replace(']', '\\]')
    text = text.replace('(', '\\(')
    text = text.replace(')', '\\)')
    text = text.replace('#', '\\#')
    text = text.replace('+', '\\+')
    text = text.replace('-', '\\-')
    text = text.replace('.', '\\.')
    text = text.replace('!', '\\!')
    text = text.replace(':', '\\:')
    text = text.replace('$', '\\$')
    return text


def docviewer(doc):
    st.subheader(f"{doc['title']}" )
    st.markdown(f"**Date**: {doc['authored']} | **Corpus:** {doc['corpus']} | \
                  **ID:** {doc['doc_id']} | **URL:** {doc['doc_url']}")
    doc_topics_sql = sg.get_topics(doc['doc_id'])
    tdf = db.execute(doc_topics_sql)
    if not tdf.empty:
        st.markdown(f"**Topic(s)**:")
        st.dataframe(tdf, hide_index=True)       
    with st.container(height=600):
        st.markdown(f"{escape_markdown(doc['body'])}")

