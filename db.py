import streamlit as st

conn = st.connection("postgresql", type="sql")

def load(filename):
    with open(f'sql/{filename}.sql', 'r') as file:
        sql = file.read()
    return sql

def load_execute(filename, ttl):
    return conn.query(load(filename), ttl=ttl)

def execute(query):
    return conn.query(query)

@st.cache_data
def get_lov(filename, colname):
    lov_df = load_execute(filename, ttl="1d")
    lov_list = lov_df[colname].to_list()
    return lov_list
