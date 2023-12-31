import streamlit as st
# This file gets pushed to GitHub. It should never contain any senitive 
# information such as authentication or authorization details. Assume the
# world has read privaleges on this file!

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
                                         help="Document title"),
    "doc_url": st.column_config.LinkColumn("Doc URL",
                                           help="URL to human readable version of doc.\
                                             Double click on cell for clickable link.",
                                    width="large"),
    "body": st.column_config.TextColumn("Plain Text",
                                        help="Document body in plain text,\
                                              often produced by OCR.\
                                              Double click on cell for\
                                              window with complete text.")
    }