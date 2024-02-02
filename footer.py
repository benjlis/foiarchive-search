import streamlit as st

def sidebar():
    st.markdown('Please [contact us](mailto:info@history-lab.org?subject=FOIArchive%20Search) \
                 with your questions, comments, and suggestions.')
    st.markdown("[History Lab Homepage](http://history-lab.org)")

def display():
    st.divider()
    st.subheader("About")
    st.markdown("Columbia University's [History Lab](http://history-lab.org) \
                created, maintains, and enhances the FOIArchive and its associated tools.")
    logo, _, description, _ = st.columns([.2, .1, .4, .3])
    logo.image('static/NEH-Preferred-Seal820.jpeg', use_column_width=True)
    description.text("")
    description.markdown("FOIArchive Search has been made possible in part by \
                         the [National Endowment for the Humanities](https://neh.gov):\
                         Democracy demands wisdom.")
