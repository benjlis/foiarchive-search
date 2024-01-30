import streamlit as st
from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

def grid(df):
    csv = df.drop('body', axis=1).to_csv().encode('utf-8')
    st.download_button(label="CSV download", data=csv, 
                       help="Download search results including document URLs",  
                       file_name='foiarchive-search.csv', mime='text/csv')
    st.markdown("Select row to see additional details including document text:")
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(value=True, editable=False)
    gb.configure_grid_options(domLayout='normal')
    gb.configure_selection(selection_mode='single', groupSelectsChildren=False)
    gb.configure_pagination(paginationAutoPageSize=False, 
                            paginationPageSize=12)
    # gb.configure_auto_height(False)
    gb.configure_column('authored', 'Date', width=150)
    gb.configure_column('corpus', 'Corpus', width=120)
    gb.configure_column('classification', 'Classification', width=150)
    gb.configure_column('title','Title', width=500)
    gb.configure_column('doc_id', 'Doc ID', width=270)
    gb.configure_column('pg_cnt', 'Pages', width=115)
    gb.configure_column('word_cnt', 'Words', width=115)
    gb.configure_column('doc_url', hide=True)
    gb.configure_column('body', hide=True)
    gridOptions = gb.build()
    grid_response = AgGrid(df, gridOptions=gridOptions,
                           return_mode_values='AS_INPUT',
                           update_mode='SELECTION_CHANGED',
                           theme='material',
                           allow_unsafe_jscode=False,
                           enable_enterprise_modules=False)    
    return grid_response['selected_rows']
