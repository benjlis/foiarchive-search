import tomli
import streamlit as st

with open("appconfig.toml", mode="rb") as fp:
    config = tomli.load(fp)

COLUMN_ORDER = ["docviewer_url", "title", "authored", "corpus", "classification", 
                "doc_id", "pg_cnt", "word_cnt", "body"]
COLUMN_CONFIGS = {
    "doc_id": st.column_config.TextColumn("Document ID", 
                                          help="Unique Document ID", 
                                          width="medium"),
    "authored": st.column_config.DatetimeColumn("Date",
                                                help="Document Date",
                                                width="small"),
    "corpus": st.column_config.TextColumn("Corpus",
                                          help="Corpus document belongs to.\
                                                See http://history-lab.org for further explanation."),
    "classification": st.column_config.TextColumn("Classification",
                                                  help="Document's original \
                                                    classification"),
    "pg_cnt": st.column_config.NumberColumn("Pages",
                                            help="Document page count \
                                                (if available)",
                                            format="%5d",
                                            width="small"),
    "word_cnt": st.column_config.NumberColumn("Words",
                                              help="Document word count",
                                              width="small"),                            
    "title": st.column_config.TextColumn("Title",
                                         help="Document title",
                                         width="large"),
    "doc_url": st.column_config.LinkColumn("Source",
                                           help="Opens the source document in a new tab.",
                                           display_text="View",
                                           width="small"),
    "docviewer_url": st.column_config.LinkColumn("Document",
                                                help="Opens the document in the DocViewer",
                                                display_text="View",
                                                width="small"),
    "body": st.column_config.TextColumn("Plain Text",
                                        help="Document body in plain text,\
                                              often produced by OCR.\
                                              Double click on cell for\
                                              window with complete text.")
    }

def sidebar_menu():
    st.sidebar.divider()
    st.sidebar.page_link("Overview.py", label="Overview")
    st.sidebar.page_link("pages/1_Search.py", label="Search")
    st.sidebar.page_link("pages/2_Topics.py", label="Topics")
 
def footer():
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
    st.sidebar.divider()
    st.sidebar.markdown('Please [contact us](mailto:info@history-lab.org?subject=FOIArchive%20Search) \
                 with your questions, comments, and suggestions.')


def page(page_name, display_menu=True):
    st.set_page_config(page_title=f'{page_name} * HL-FOIA',
                       page_icon=config["favicon"],
                       layout="wide",
                       menu_items={'Get Help': config["help_action"],
                                   'Report a bug': config["bug_action"],
                                   'About': f"### {config['gui_title']}\n" +
                                            f"{config['about_body']}"})
    # sidebar logic
    st.sidebar.header("Freedom of Information Archive (FOIArchive)")
    st.sidebar.divider()
    if display_menu:
        st.title(f'{page_name}')
        sidebar_menu()
