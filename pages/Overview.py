import streamlit as st
import configs as c
import boilerplate

c.page()

# st.header("FOIArchive Overview")
st.header("Overview")
st.markdown("The FOIArchive is a collection of documents obtained through \
             the Freedom of Information Act (FOIA) and other public records \
             requests. The documents are primarily from the U.S. government, \
             but also include materials from other countries. The collection \
             is a work in progress, with new documents added as they are \
             obtained and processed.")

st.subheader("Corpora Description")
st.markdown("##### CIA Crest Collection (cia)")

st.subheader("Motivation")
st.markdown("Although this video is a few years old, it still does a great job\
             explaining why we built and continue to expand the FOIArchive.")
st.video("https://www.youtube.com/watch?v=6oTNw2jZ3zw&t=42s")

boilerplate.footer()