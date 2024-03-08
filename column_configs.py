import streamlit as st
# This file gets pushed to GitHub. It should never contain any senitive 
# information such as authentication or authorization details. Assume the
# world has read privaleges on this file!

COLUMN_ORDER = ["doc_url", "title", "authored", "corpus", "classification", "pg_cnt", "word_cnt"]
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
    "body": st.column_config.TextColumn("Plain Text",
                                        help="Document body in plain text,\
                                              often produced by OCR.\
                                              Double click on cell for\
                                              window with complete text.")
    }