import tomli
import boilerplate
import streamlit as st

with open("appconfig.toml", mode="rb") as fp:
    config = tomli.load(fp)

def page(page_name):
    st.set_page_config(page_title=f'{config["tab_title"]}',
                       page_icon=config["favicon"],
                       layout="wide",
                       menu_items={'Get Help': config["help_action"],
                                   'Report a bug': config["bug_action"],
                                   'About': f"### {config['gui_title']}\n" +
                                            f"{config['about_body']}"})
    st.title(f'{config["gui_title"]} - {page_name}')
    with st.sidebar:
        boilerplate.sidebar()
