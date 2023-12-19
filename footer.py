import streamlit as st

def display():
    st.subheader("About")
    st.markdown("Columbia University's [History Lab](http://history-lab.org) \
                created, maintains, and enhances the FOIArchive and its associated tools.")
    logo, _, description, _ = st.columns([.2, .1, .4, .3])
    logo.image('static/NEH-Preferred-Seal820.jpeg', use_column_width=True)
    description.text("")
    description.markdown("FOIArchive Search has been made possible in part by \
                         the [National Endowment for the Humanities](https://neh.gov):\
                         Democracy demands wisdom.")
