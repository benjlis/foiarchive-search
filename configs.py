import tomli
import boilerplate
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

def page(page_name, display_menu=True):
    st.set_page_config(page_title=f'{page_name} * HL-FOIA',
                       page_icon=config["favicon"],
                       layout="wide",
                       menu_items={'Get Help': config["help_action"],
                                   'Report a bug': config["bug_action"],
                                   'About': f"### {config['gui_title']}\n" +
                                            f"{config['about_body']}"})
    boilerplate.sidebar()
    if display_menu:
        st.title(f'{page_name}')
        boilerplate.menu()
