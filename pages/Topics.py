import streamlit as st
import configs as c
c.page("Topic Models")
import db
"""
Query the FOIArchive via topics derived by topic modeling. You can find
more information about topic modeling 
[here](http://history-lab.org/documentation).
"""
cdf = db.load_execute("corpora")
tdf = db.load_execute("topics")
col1, col2 = st.columns([1, 2])
corpora_with_topics = cdf[cdf["topic_cnt"].notnull()]
corpus = col1.selectbox("Corpus", corpora_with_topics)
corpora_topics = tdf.display[tdf["corpus"]==corpus]
topic = col2.selectbox("Topic", corpora_topics)
topic_id = tdf.topic_id[tdf["display"]==topic].values[0]
