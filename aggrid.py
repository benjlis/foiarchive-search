from st_aggrid import AgGrid
from st_aggrid.grid_options_builder import GridOptionsBuilder

def grid(df):
    gb = GridOptionsBuilder.from_dataframe(df)
    gb.configure_default_column(value=True, editable=False)
    gb.configure_grid_options(domLayout='normal')
    gb.configure_selection(selection_mode='single', groupSelectsChildren=False)
    # gb.configure_auto_height(False)
    gb.configure_pagination(paginationAutoPageSize=False, 
                            paginationPageSize=20)
    # gb.configure_column('email_id', hide=True)
    # gb.configure_column('pg_number', hide=True)
    # gb.configure_column('top_topic', hide=True)
    # gb.configure_column('entities', hide=True)
    # gb.configure_column('sent', maxWidth=150)
    # gb.configure_column('subject', maxWidth=600)
    # gb.configure_column('from', maxWidth=225)
    # gb.configure_column('to', maxWidth=425)
    gridOptions = gb.build()
    grid_response = AgGrid(df, gridOptions=gridOptions,
                           return_mode_values='AS_INPUT',
                           update_mode='SELECTION_CHANGED',
                           allow_unsafe_jscode=False,
                           enable_enterprise_modules=False)    
    return grid_response['selected_rows']
