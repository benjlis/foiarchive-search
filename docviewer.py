import streamlit as st

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
    print('title', doc['title'])
    esc_title = escape_markdown(doc['title'])
    print('esc_title', esc_title)
    st.subheader(f"{doc['title']}" )
    st.markdown(f"**Date**: {doc['authored']} | **Corpus:** {doc['corpus']} | \
                  **ID:** {doc['doc_id']} | **URL:** {doc['doc_url']}")
    with st.container(height=600):
        st.markdown(f"{escape_markdown(doc['body'])}")
        # st.text(doc['body'])
