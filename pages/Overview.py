import streamlit as st
import configs as c
c.page("Overview")    # must be 1st streamlit cmd or strange behavior ensues
import boilerplate
import sqlgen as sg
import db

st.markdown("The FOIArchive is a collection of documents obtained through \
             the Freedom of Information Act (FOIA) and other public records \
             requests. The documents are primarily from the U.S. government, \
             but also include materials from other countries. The collection \
             is a work in progress, with new documents added as they are \
             obtained and processed.")
st.markdown("The foiarchive is currently comprised of:")

# display metrics
totals_sql = sg.query('totals', "foiarchive.totals", None)
totals_df = db.execute(totals_sql)
doc_cnt, pg_cnt, word_cnt = totals_df.iloc[0] 
st.metric(label="Documents", value=f"{doc_cnt:,}", delta=None)
st.metric(label="Pages", value=f"{pg_cnt:,}", delta=None)
st.metric(label="Words", value=f"{word_cnt:,}", delta=None)

st.subheader("Corpora Description")
with open(c.config["corpora_description"], "r") as f:
    st.markdown(f.read())

st.subheader("Motivation")
st.markdown("Although this video is a few years old, it still does a great job\
             explaining why we built and continue to expand the FOIArchive.")
st.video("https://www.youtube.com/watch?v=6oTNw2jZ3zw&t=42s")

boilerplate.footer()