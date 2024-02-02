import tomli
import boilerplate
import streamlit as st

with open("appconfig.toml", mode="rb") as fp:
    config = tomli.load(fp)

def page():
    st.set_page_config(page_title=config["tab_title"],
                       page_icon=config["favicon"],
                       layout="wide",
                       menu_items={'Get Help': config["help_action"],
                                   'Report a bug': config["bug_action"],
                                   'About': f"### {config['gui_title']}\n" +
                                            f"{config['about_body']}"})
    st.title(config['gui_title'])
    with st.sidebar:
        boilerplate.sidebar()
