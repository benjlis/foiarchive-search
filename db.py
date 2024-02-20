import streamlit as st

conn = st.connection("postgresql", type="sql")

def load(filename):
    with open(f'sql/{filename}.sql', 'r') as file:
        sql = file.read()
    return sql

@st.cache_data
def load_execute(filename):
    return conn.query(load(filename))

def execute(query):
    return conn.query(query)

def get_lov(filename, colname):
    lov_df = load_execute(filename)
    lov_list = lov_df[colname].to_list()
    return lov_list
