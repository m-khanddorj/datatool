import os
from fnmatch import filter
import json

import streamlit as st
import pandas as pd

from src.processor import process
from src.CustomTable import Table

def editData():

    path = st.text_input('Data path')

    if path != '':
        files = os.listdir(path)
        json_files = filter(files,'*.json')

        file = st.selectbox('File',json_files)
        if file:
            # JSON file
            f = open(os.path.join(path,file), "r")
            
            # Reading from file
            json_data = json.loads(f.read())

            col1,col2 = st.columns(2)
            data_source = col1.text_input('Source',json_data['source'],key='edit_source')
            data_class = col2.multiselect('Class',['Society','Education','Something','Blah2'],json_data['class'],key='edit_class')

            text = st.text_area('Text',json_data['text'],key='edit_text')

            dataframe = pd.DataFrame({
                'Sentence': [sentence['sentence'] for sentence in json_data['sentences']],
            })

            dataframe = Table(dataframe,'edit_table')

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
            out_json = json.dumps(result)

            st.download_button(
                label="Download JSON",
                file_name="data.json",
                mime="application/json",
                data=out_json,
                key='edit_download'
            )