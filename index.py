import streamlit as st

from pages.newData import newData
from pages.editData import editData

if __name__ == '__main__':
    #configurations
    st.set_page_config(layout="wide")
    st.markdown(
        """
        <style>
                html, body, [class*="css"],[class="ag-cell-value"]  {
                font-family: 'Arial' !important;
                }
                .ag-cell-value{
                    font-family: 'Arial' !important;
                }
                div.ag-theme-alpine div.ag-row {
                    font-size: 12px !important;
                }

        </style>

        """,
            unsafe_allow_html=True,
        )
    tab1,tab2 =  st.tabs(['New data','Edit data'])

    with tab1:
        newData()
    with tab2:
        editData()