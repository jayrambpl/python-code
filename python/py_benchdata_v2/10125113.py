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


st.set_page_config(page_title="Data Dashboard",layout="wide")

# names = ["Jayram Singh", "User1", "Pitambar B Javale","Admin"]
# usernames = ["jayram", "user1", "pitambar","admin"]
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

    file1 = st.sidebar.file_uploader(":file_folder: Upload discussion Report:", type=(["xlsx","xls"]))
    if file1:
        st.sidebar.success("File successfully uploaded!")
    if file1 is not None:
        Input_file1 = file1.name
    else:
        try:
            with open("web.ini", "r") as f1:
                Input_file1 = f1.read().strip()
        except Exception as e:
            st.error("File not found")
            # st.stop()
            
        
    @st.cache_data(ttl=60*60*24)
    def get_excel_data(Input_file1):

        df1 = pd.read_excel(io=Input_file1,
                            engine="openpyxl",
                            sheet_name="Bench",
                            usecols="B:U"
                            )
        df2 = pd.read_excel(io=Input_file1,
                            engine="openpyxl",
                            sheet_name="Upcoming_Bench",
                            usecols="B:U")
        return df1,df2

    print(Input_file1)

    df1, df2 = get_excel_data(Input_file1)


    # ------------
    st.sidebar.header("Select Filter:", divider='rainbow')
    
    tower_selected= st.sidebar.multiselect("Select Tower for Bench Data",
                                options=df1["Tower"].unique(),
                                default=df1["Tower"].unique()
                                )
    band_selected = st.sidebar.multiselect("Select Band for Bench Data",
                                        options=df1["BandAsPerSR"].unique(),
                                        default=df1["BandAsPerSR"].unique()
                                            )

    df1_selected = df1.query(
        "Tower==@tower_selected & BandAsPerSR==@band_selected")
    # =============

    st.sidebar.subheader("Upcoming Data Filter:", divider='rainbow')
    upcoming_tower_selected= st.sidebar.multiselect("Select Tower for Upcoming Bench Data",
                                options=df2["Tower"].unique(),
                                default=df2["Tower"].unique()
                                )
    upcoming_band_selected = st.sidebar.multiselect("Select Band for Upcoming Bench Data",
                                        options=df2["BandAsPerSR"].unique(),
                                        default=df2["BandAsPerSR"].unique()
                                            )

    df2_selected = df2.query(
        "Tower==@upcoming_tower_selected & BandAsPerSR==@upcoming_band_selected")

    # =======
    st.markdown('<style>div.block-container{padding-top:1rem;}</style>', unsafe_allow_html=True)
    image = Image.open("logo125x140.png")

    dark_color_map = {
        "6A": "#1f77b4",  # Blue
        "6B": "#2ca02c",  # Green
        "7A": "#d62728",  # Red
        "7B": "#ff7f0e",  # Orange
        "8": "#9467bd",  # Purple
        "9": "#7f7f7f",  # Gray
        "10": "#17becf"  # Turquoise
    }

    light_color_map = {
        "6A": "#3498db",  # Blue
        "6B": "#2ecc71",  # Green
        "7A": "#e74c3c",  # Red
        "7B": "#f39c12",  # Orange
        "8": "#9b59b6",  # Purple
        "9": "#34495e",  # Dark Gray
        "10": "#1abc9c"  # Turquoise

    }

    html_title = """
        <style>
        .title-test {
        font-weight:bold;
        padding:10px;
        border-radius:6px;
        }
        </style>
        <center><h2 class="title-test">Data Dashboard</h2></center> """  
    html_footer = """ 
        <style>
        .foot-test {
        padding:10px;
        border-radius:6px;
        }
        </style><center><h4 class="foot-test">Desing & Developed by: \n Jayram Singh @IBM</h4></center> """  


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
    df2_copy = df2_selected.copy()

    data1 = df1_selected.groupby(['Tower', 'BandAsPerSR']).size().reset_index(name='Count of band')
    df1_selected = pd.DataFrame(data1)
    data2 = df2_selected.groupby(['Tower', 'BandAsPerSR']).size().reset_index(name='Count of band')
    df2_selected = pd.DataFrame(data2)


    def metrics():
        col4.metric("Total Bench Count:", df1_selected['Count of band'].sum())
        # col5.metric("Band Count:", df1_selected["BandAsPerSR"].count())
        col6.metric("Total Upcoming Bench:", df2_selected['Count of band'].sum())
        # col7.metric("Band Count (upcoming):", df2_selected["BandAsPerSR"].count())
        style_metric_cards(background_color="#1F3748", border_left_color="#3577DA")
        # --#1F3748 - dark
        # --#3577DA - blue
        #  #284860 - light
        # #B0D68E - green dark
    st.divider()

    _, fig1 , fig2 = st.columns([0.1,0.45,0.45])

    with fig1:
        st.header("**Current Bench**")
        # df1_selected['Color'] = df1_selected['BandAsPerSR'].map(dark_color_map)    
        fig = px.bar(df1_selected, x="Tower", y="Count of band",
                    labels={"Count of band": "Count of band"},
                    title= "<b>Tower wise Band mix</b>", hover_data=["BandAsPerSR"],
                    color="BandAsPerSR", barmode="group",
                    color_discrete_sequence=["#3577DA"] * len(df1_selected),
                    template="gridon", height=400) 
                    
        st.plotly_chart(fig, use_container_width=True)

    with fig2:
        st.header("**Upcoming Bench**")
        # df1_selected['Color'] = df1_selected['BandAsPerSR'].map(light_color_map)    
        fig = px.bar(df2_selected, x="Tower", y="Count of band",
                    title= "Tower wise Band mix", hover_data=["BandAsPerSR"],
                    color="BandAsPerSR", barmode="group",
                    color_discrete_sequence=["#3577DA"] * len(df1_selected),
                    template="gridon", height=400) 
        st.plotly_chart(fig, use_container_width=True)


    _, view1 , view2 = st.columns([0.1,0.45,0.45])

    with view1:
        # st.header("**Current Bench Data**")
        with st.expander("Tower wise Bench Data"):
            gd = GridOptionsBuilder.from_dataframe(df1_selected)
            gd.configure_pagination(enabled=True)
            gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
            gridoptions = gd.build()
            gridoptions['autoSizeColumns'] = 'all'
            grid_df1_1 = AgGrid(df1_selected, gridOptions=gridoptions,
                                   enable_enterprise_modules=True,
                                   update_mode='MODEL_CHANGED',
                                   height=350, width='100%',
                                   allow_unsafe_jscode=True,
                                   theme='streamlit')

    with view2:
        # st.header("**Upcoming Bench Data**")
        with st.expander("Tower wise Bench Data"):
            gd = GridOptionsBuilder.from_dataframe(df2_selected)
            gd.configure_pagination(enabled=True)
            gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
            gridoptions = gd.build()
            grid_df2_2 = AgGrid(df2_selected, gridOptions=gridoptions,
                                   enable_enterprise_modules=True,
                                   update_mode='MODEL_CHANGED',
                                   height=350, width='100%',
                                   allow_unsafe_jscode=True,
                                   theme='streamlit')

    metrics()

    # _, stick1 , stick2 = st.columns([0.1,0.45,0.45])
    # stick1_text = f""
    # stick2_text = f""
    
    # with stick1:
    #     custom_style = f"font-size: 16px; color: white; background-color: #1F3748; border-left: 6px solid #3577DA; padding: 10px;"
    #     # st.markdown(f'<div style="{custom_style}">Selected Row: {stick1_text}</div>', unsafe_allow_html=True)
    #     stick1.metric("Selected Row:",stick1_text) 
    #     style_metric_cards(background_color="#1F3748", border_left_color="#3577DA")
        
    # with stick2:
    #     custom_style = f"font-size: 16px; color: white; background-color: #1F3748; border-left: 6px solid #3577DA; padding: 10px;"
    #     # st.markdown(f'<div style="{custom_style}">Selected Row: {stick2_text}</div>', unsafe_allow_html=True)
    #     stick2.metric("Selected Row:",stick2_text)
    #     style_metric_cards(background_color="#1F3748", border_left_color="#3577DA")


    st.divider()
    # ------------
    _, view3 , view4 = st.columns([0.1,0.45,0.45])
    with view3:
        expander = st.expander("Tower wise Bench Data")
        with st.expander("Tower wise Bench Data"):
            gd = GridOptionsBuilder.from_dataframe(df1_copy)
            gd.configure_pagination(enabled=True, paginationPageSize=5)  # Set pagination options as needed
            gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
            gd.configure_selection(selection_mode='single', use_checkbox=True)
            gridoptions = gd.build()
            grid_df1_2 = AgGrid(df1_copy, gridOptions=gridoptions,
                        enable_enterprise_modules=True,
                        update_mode=GridUpdateMode.SELECTION_CHANGED,
                        height=350, width='100%',
                        allow_unsafe_jscode=True,
                        theme='streamlit')
    
        sel_row1 = grid_df1_2["selected_rows"]
        
        if sel_row1:
            jrss_primary_value = sel_row1[0]["JRSS-Primary"]
            Tower_value = sel_row1[0]["Tower"]
            name_emp = sel_row1[0]["Name"]
            uti1 = sel_row1[0]["13 Wk Ute"]
            skill1 = sel_row1[0]["Skills"]
            skill2 = sel_row1[0]["Secondary Skills"] 

            st.subheader("Selected Resource Details:", divider='rainbow')
            st.write(f"\nName : {name_emp}")
            st.write(f"JRSS-Primary : {jrss_primary_value}")
            st.write(f"Tower : {Tower_value}")
            st.write(f"13 Wk Ute : {uti1}")
            st.write(f"Skill-1 : {skill1}")
            st.write(f"Skill-2 : {skill2}")
            

        else:
            st.write("No rows selected.")
        # stick1_call()

    with view4:
        expander = st.expander("Tower wise Bench Data")
        with st.expander("Tower wise Bench Data"):
            gd = GridOptionsBuilder.from_dataframe(df2_copy)
            gd.configure_pagination(enabled=True)
            gd.configure_default_column(groupable=True, value=True, enableRowGroup=True, aggFunc='sum', editable=True)
            gd.configure_selection(selection_mode='single', use_checkbox=True)
            # gd.configure_viewport_size(20)  # Set the viewport size to enable vertical scroll
            # gd.configure_dom_layout('autoHeight') 
            # gd.configure_enable_horizontal_scrollbar(True)
            gridoptions = gd.build()
            grid_df2_2 = AgGrid(df2_copy, gridOptions=gridoptions,
                                enable_enterprise_modules=True,
                                update_mode='MODEL_CHANGED',
                                height=350, width='100%',
                                allow_unsafe_jscode=True,
                                theme='streamlit')
            sel_row2 = grid_df2_2["selected_rows"]
            if sel_row2:
                jrss_primary_value1 = sel_row2[0]["JRSS-Primary"]
                Tower_value1 = sel_row2[0]["Tower"]
                name_emp1 = sel_row2[0]["Name"]
                uti2 = sel_row2[0]["13 Wk Ute"]
                skill1_1 = sel_row2[0]["Skills"]
                skill2_1 = sel_row2[0]["Secondary Skills"] 
            
                st.subheader("Selected Resource Details:", divider='rainbow')
                # stick1_text = f"Name: {name_emp}, Primary-JRSS : {jrss_primary_value}, Skill : {skill_value}, 13wkUtilization"
                # st.write(f"\nName : {name_emp}, \nJRSS-Primary : {jrss_primary_value}, \nSkill : {skill_value}")
                st.write(f"\nName : {name_emp1}")
                st.write(f"JRSS-Primary : {jrss_primary_value1}")
                st.write(f"Tower : {Tower_value1}")
                st.write(f"13 wk Utilization : {uti2}")
                st.write(f"Skill-1 : {skill1_1}")
                st.write(f"Skill-2 : {skill2_1}")
                
            else:
                st.write("No rows selected.")
                # stick2_call()

            # st.subheader("Selected Resource Details:")
            # st.write(sel_row2)
    
    st.divider()

    st.markdown(html_footer, unsafe_allow_html=True)
