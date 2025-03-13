import streamlit as st
import pandas as pd
import plotly.express as px 
import plotly.graph_objects as go
import numpy as np


### CONFIG
st.set_page_config(
    page_title="E-commerce",
    page_icon="💸",
    layout="wide"
  )

### TITLE AND TEXT
st.title("Sport Heroes")
st.image("https://stillmed.olympic.org/media/Images/OlympicOrg/IOC/The_Organisation/The-Olympic-Rings/Olympic_rings_TM_c_IOC_All_rights_reserved_1.jpg", width=300)

### EXPANDER
st.subheader("Opening French Olympic Games")
with st.expander("⏯️ Watch "):
    st.video("https://youtu.be/6ldC6uHxHIc?si=94yBjIq41YakFQ1C")

st.subheader("The Raw Data")
st.markdown("""
    All the __Heroes__ are in this Raw Datas 👇
""")

### LOAD AND CACHE DATA
DATA_URL = ('athlete_events.csv')

@st.cache_data # this lets the 
def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    return data

data_load_state = st.text('Loading data...')
data = load_data(1000)
data_load_state.text("") # change text from "Loading data..." to "" once the the load_data function has run

## Run the below code if the check is checked ✅
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data) 


### SHOW GRAPH STREAMLIT

st.subheader("Medals per Country")
medal_per_country = data.groupby("NOC")["Medal"].describe()  # Fix bar chart issue
st.bar_chart(medal_per_country)

### SHOW GRAPH PLOTLY + STREAMLIT

st.subheader("All the Olympic Countries X events")

fig = px.histogram(data, x="Year", color='City', barmode="group")
st.plotly_chart(fig, use_container_width=True)


### SIDEBAR
st.sidebar.header("Build dashboards with Streamlit")
st.sidebar.markdown("""
    * [Opening French Olympic Games](#opening-french-olympic-games)
    * [Sport Heros Top](#sport-heroes)
    * [Medals per Country](#medals-per-country)
    * [Input Data](#input-data)
""")
e = st.sidebar.empty()
e.write("")
st.sidebar.write("Made with 💖 by [Jedha](https://jedha.co)")
st.sidebar.image("Leon-Marchand.png")



st.markdown("---")

#### CREATE TWO COLUMNS

@st.cache_data # this lets the 
def load_datam():
    datam = pd.read_csv(DATA_URL)
    return datam
datam = load_datam()
st.markdown("**1️⃣ Example of input widget**")
country = st.selectbox("Select a country you want to see all the medals", datam["NOC"].sort_values().unique())
country_medal = datam[datam["NOC"]==country].groupby('Medal')['Sex'].value_counts().reset_index()
fig = px.bar(country_medal, x='Medal', y='count', color='Sex', barmode='group')
fig.update_layout(bargap=0.2)
st.plotly_chart(fig, use_container_width=True)

