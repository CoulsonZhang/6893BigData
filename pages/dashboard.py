import streamlit as st
import pandas as pd
import plotly.express as px

st.title("League of Legends Exploratory Data Analysis and Visualization")


st.markdown('''
A Web Page to visualize and analyze the League of Legends data from North America
* **Libraries Used:** Streamlit, Pandas, Plotly
* **Data Source:** Riot API
''')

# Reading csv data
data = pd.read_csv('/Users/wen/Desktop/6893BigData/model_train/match_data_till_Nov22_62k.csv')
# Displaying Data and its Shape
st.write("**League of Legends dataset**", data)
st.write("Shape of data", data.shape)