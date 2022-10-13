import json
from io import BytesIO

import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

from src.processor import process
from src.CustomTable import Table

def newData():
    if 'computing' not in st.session_state:
        st.session_state['computing'] = False

    st.header('New Data')
    col1,col2 = st.columns(2)
    data_source = col1.text_input('Source')
    data_class = col2.multiselect('Class',['Society','Education','Something','Blah2'])

    text = st.text_area('Text')

    process_button = st.button('Process🤔' if not st.session_state['computing'] else 'Stop')
    if process_button:
        st.session_state['computing'] = not st.session_state['computing']

    if st.session_state['computing']:
        sentences = process(text)
        dataframe = pd.DataFrame({
            'Sentence': sentences,
        })

        dataframe = Table(dataframe,'new_table')

        result = {
            'text' : text,
            'source': data_source,
            'class': data_class,
            'sentences' : [
                {'sentence':sentence}
                for sentence in dataframe['Sentence'].tolist()
            ]
        }
        # the json file where the output must be stored
        out_json = json.dumps(result, ensure_ascii=False)
        st.download_button(
            label="Download JSON",
            file_name="data.json",
            mime="application/json",
            data=out_json,
        )