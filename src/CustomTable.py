from typing import Optional
import streamlit as st
import pandas as pd
from st_aggrid import GridOptionsBuilder, JsCode, AgGrid



string_to_add_row = """
    function(e) {  
        let api = e.api;  
        let rowIndex = e.rowIndex + 1;  
        api.applyTransaction({addIndex: rowIndex, add: [{}]});  
    }; 
 """

string_to_delete = """
    function(e) {  
        let api = e.api;  
        let sel = api.getSelectedRows();  
        api.applyTransaction({remove: sel});  
    };      
"""

custom_css = {'font-family': " 'Arial' !important;"}

    
cell_button_add = JsCode('''
    class BtnAddCellRenderer {
        init(params) {
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
             <span>
                <style>
                .btn_add {
                  background-color: limegreen;
                  border: none;
                  color: white;
                  text-align: center;
                  text-decoration: none;
                  display: inline-block;
                  font-size: 10px;
                  font-weight: bold;
                  height: 2.5em;
                  width: 8em;
                  cursor: pointer;
                }

                .btn_add :hover {
                  background-color: #05d588;
                }
                </style>
                <button id='click-button' 
                    class="btn_add" 
                    >&CirclePlus; Add</button>
             </span>
          `;
        }

        getGui() {
            return this.eGui;
        }

    };
    ''')
    

cell_button_delete = JsCode('''
    class BtnCellRenderer {
        init(params) {
            console.log(params.api.getSelectedRows());
            this.params = params;
            this.eGui = document.createElement('div');
            this.eGui.innerHTML = `
             <span>
                <style>
                .btn {
                  background-color: #F94721;
                  border: none;
                  color: white;
                  font-size: 10px;
                  font-weight: bold;
                  height: 2.5em;
                  width: 8em;
                  cursor: pointer;
                }

                .btn:hover {
                  background-color: #FB6747;
                }
                </style>
                <button id='click-button'
                    class="btn"
                    >&#128465; Delete</button>
             </span>
          `;
        }

        getGui() {
            return this.eGui;
        }

    };
    ''')    



cellsytle_jscode_Name = JsCode("""
                            function(params){
                                if (params.value.includes('Violation of Rule')) {
                                    return {
                                        'color': 'red', 
                                        'backgroundColor': 'white',
                                    }
                                }
                            
                            
                            if (params.value.includes('Missing')) {
                                return {
                                    'color': 'red', 
                                    'backgroundColor': 'white',
                                }
                            }
                            
                                                                    
                                if (params.value.length>6) {
                                    return {
                                        'color': 'red', 
                                        'backgroundColor': 'white',
                                    }
                                }                                    
                                                                    
                            
                            
                                if (params.value.length<=6) {
                                    return {
                                        'color': 'red', 
                                        'backgroundColor': 'white',
                                    }
                                } 
                            
                            if (params.value=="") {
                                return {
                                    'color': 'black', 
                                    'backgroundColor': 'yellow',
                                }
                            }                                    
                            
                            
                            }
                            
                            """)



def Table(dataframe: pd.DataFrame,key: Optional[str] = '') -> pd.DataFrame:

    gb = GridOptionsBuilder.from_dataframe(dataframe)
    gb.configure_column('Add', headerTooltip='Click on Button to add new row', editable=False, filter=False,
                                onCellClicked=JsCode(string_to_add_row), cellRenderer=cell_button_add,
                                autoHeight=True, wrapText=True, lockPosition='left')

    gb.configure_column('Delete', headerTooltip='Click on Button to remove row',
                                        editable=False, filter=False, onCellClicked=JsCode(string_to_delete),
                                        cellRenderer=cell_button_delete,
                                        autoHeight=True, suppressMovable='true')



    gb.configure_default_column(editable=True)
    gb.configure_selection(use_checkbox=True,selection_mode="multiple")
    grid_options = gb.build()
    grid_return = AgGrid(dataframe, gridOptions=grid_options,allow_unsafe_jscode=True,theme="streamlit",key=key,custom_css=custom_css)
    return grid_return['data']
