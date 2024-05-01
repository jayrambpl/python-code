import pandas as pd
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as splt
from PIL import Image
import datetime
from streamlit_extras.metric_cards import style_metric_cards
import pickle
import streamlit_authenticator as  stauth
from pathlib import Path
from st_aggrid import AgGrid , JsCode , GridUpdateMode
from st_aggrid.grid_options_builder import GridOptionsBuilder
import os


st.set_page_config(page_title="CDRCOM Dashboard",layout="wide")

# names = ["Jayram Singh", "User1", "Rohan misra","Admin"]
# usernames = ["jayram", "user1", "rohan","admin"]
# file_path = Path(__file__).parent / "hashed_pw.pkl"

# with file_path.open("rb") as file:
#     hashed_passwords = pickle.load(file)


# authenticator = stauth.Authenticate(names, usernames, hashed_passwords, cookie_expiry_days=30)

# name, authenticator_status, username = authenticator.login("Login", "main")

authenticator_status= True

if authenticator_status == False:
    st.error("Username/password is incorrect")
    st.stop()

if authenticator_status == None:
    st.warning("Please enter your username and password")
    st.stop()
    
if authenticator_status:
    
    # authenticator.logout("Logout", "sidebar")
    # st.write(f"Welcome Jayram", "sidebar")

    file1 = st.sidebar.file_uploader(":file_folder: Upload Mgt Report:", type=(["csv","csv"]))
    if file1:
        st.sidebar.success("File successfully uploaded!")
    if file1 is not None:
        Input_file1 = file1.name
    else:
        try:
            with open("conf.ini", "r") as f1:
                Input_file1 = f1.read().strip()
        except Exception as e:
            st.error("File not found")
            # st.stop()
            
        
    @st.cache_data(ttl=60*60*24)
    def get_data(Input_file1):
        df1 = pd.read_csv(Input_file1)
        return df1

    df1 = get_data(Input_file1)

    # ------------
    st.sidebar.header("Select Filter:", divider='rainbow')
    
    hub_selected= st.sidebar.multiselect("Select Hub :",
                                options=df1["hub"].unique(),
                                # default=df1["hub"].unique()
                                )
    # date_selected = st.sidebar.multiselect("Select Date :",
    #                                     options=df1["Date"].unique(),
    #                                     default=df1["Date"].unique()
                                            # )
    df1_selected = df1.query( "hub==@hub_selected")
    stream_selected = st.sidebar.multiselect("Select Stream Name :",
                                        options=df1_selected["StreamName"].unique(),
                                        # default=df1["StreamName"].unique()
                                            )

    df1_selected = df1.query( "hub==@hub_selected & StreamName==@stream_selected")
    # =============

    # =======
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    image = Image.open("logo125x140.png")

    
    html_title = """
        <style>
        .title-test {
        font-weight:bold;
        padding:10px;
        border-radius:6px;
        }
        </style>
        <center><h2 class="title-test">CDRCOM Dashboard</h2></center> """  
    html_footer = """ 
        <style>
        .foot-test {
        padding:10px;
        border-radius:6px;
        }
        </style><center><h4 class="foot-test">Desing & Developed by: \n Jayram Singh @IBM, Rohan Misra @IBM</h4></center> """  


    col1, col2 = st.columns([0.1,0.9])
    with col1:
        st.image(image, width=100)


    with col2:
        st.markdown(html_title, unsafe_allow_html=True)

    col3, col4 , col5, col6, col7 = st.columns([0.1,0.20,0.20,0.20,0.20])
    with col3:
        box_date = str(datetime.datetime.now().strftime("%d %B %Y"))
        st.write(f"Report Date:  \n {box_date}")

    df1_copy = df1_selected.copy()
    data1 = df1_selected.groupby(['hub']).size()
    df1_selected = pd.DataFrame(data1)
    

    def metrics():
        col4.metric("Total Hub :", df1_selected['hub'].count())
        col5.metric("Total Stream :", df1_selected["StreamName"].count())
        # col6.metric("Total time taken :", df2_selected['Count of band'].sum())
        # col7.metric("Total CDR proccessed :", df2_selected["BandAsPerSR"].count())
        style_metric_cards(background_color="#1F3748", border_left_color="#3577DA")
        
    st.divider()

    _, fig1 , fig2 = st.columns([0.1,0.45,0.45])
    df1_bar = df1_selected.copy()
    df2_bar = df1_bar.groupby(['hub', 'StreamName']).size().reset_index(name='Count')
    # df1_bar.rename(columns={'hub': 'Hub'}, inplace=True)
    # df1_bar['Stream Count'] = df1_bar['StreamName']
    # df1_bar.drop(columns=['StreamName'], inplace=True)
    st.write(df2_bar.shape)
    st.write(df2_bar)

    # with fig1:
    #     st.header("**Hub vs Stream**")
    #     # df1_selected['Color'] = df1_selected['BandAsPerSR'].map(dark_color_map)    
    #     fig = px.bar(df1_selected, x="Hub", y="Stream Count",
    #                 labels={"Count of Hub": "Count of Stream"},
    #                 title= "<b>Hub wise distribution</b>", hover_data=["StreamName"],
    #                 color="hub", barmode="group",
    #                 color_discrete_sequence=["#3577DA"] * len(df1_selected),
    #                 template="gridon", height=400) 
                    
    #     st.plotly_chart(fig, use_container_width=True)

    
    # _, view1 , view2 = st.columns([0.1,0.45,0.45])

    # with view1:
    #     # st.header("**Current Bench Data**")
    #     with st.expander("Hub Data"):
    #         gd = GridOptionsBuilder.from_dataframe(df1_selected)
    #         gd.configure_pagination(enabled=True)
    #         gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
    #         gridoptions = gd.build()
    #         gridoptions['autoSizeColumns'] = 'all'
    #         grid_df1_1 = AgGrid(df1_selected, gridOptions=gridoptions,
    #                                enable_enterprise_modules=True,
    #                                update_mode='MODEL_CHANGED',
    #                                height=350, width='100%',
    #                                allow_unsafe_jscode=True,
    #                                theme='streamlit')

    
    metrics()

    
    # ------------
    # _, view3 , view4 = st.columns([0.1,0.45,0.45])
    # with view3:
    #     expander = st.expander("Hub & Stream Data")
    #     with st.expander("Hub & Stream Data"):
    #         gd = GridOptionsBuilder.from_dataframe(df1_copy)
    #         gd.configure_pagination(enabled=True, paginationPageSize=5)  # Set pagination options as needed
    #         gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
    #         gd.configure_selection(selection_mode='single', use_checkbox=True)
    #         gridoptions = gd.build()
    #         grid_df1_2 = AgGrid(df1_copy, gridOptions=gridoptions,
    #                     enable_enterprise_modules=True,
    #                     update_mode=GridUpdateMode.SELECTION_CHANGED,
    #                     height=350, width='100%',
    #                     allow_unsafe_jscode=True,
    #                     theme='streamlit')
    
    #     sel_row1 = grid_df1_2["selected_rows"]
    #     st.write(sel_row1)
        # if sel_row1:
        #     jrss_primary_value = sel_row1[0]["JRSS-Primary"]
        #     Tower_value = sel_row1[0]["Tower"]
        #     name_emp = sel_row1[0]["Name"]
        #     uti1 = sel_row1[0]["13 Wk Ute"]
        #     skill1 = sel_row1[0]["Skills"]
        #     skill2 = sel_row1[0]["Secondary Skills"] 

        #     st.subheader("Selected Resource Details:", divider='rainbow')
        #     st.write(f"\nName : {name_emp}")
        #     st.write(f"JRSS-Primary : {jrss_primary_value}")
        #     st.write(f"Tower : {Tower_value}")
        #     st.write(f"13 Wk Ute : {uti1}")
        #     st.write(f"Skill-1 : {skill1}")
        #     st.write(f"Skill-2 : {skill2}")
            

        # else:
        #     st.write("No rows selected.")
        # # stick1_call()


    st.markdown(html_footer, unsafe_allow_html=True)
