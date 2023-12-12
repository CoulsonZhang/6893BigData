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

# Create 3 tabs to the main panel of the web page.
tab1, tab2, tab3 = st.tabs(["Dataset Overview", "Numeric Features", "Categorical Features"])


with tab1:
    # Displaying Data and its Shape
    st.write("**League of Legends dataset**", data)
    st.write("Shape of data", data.shape)

    st.write('''
    After considering the correlation matrix, we finally choose the following 11 features to explore 
    their relationship with the target variable 'the Winning Team'.
    * winner
    * firstInhibitor
    * t1_towerKills
    * t1_inhibitorKills
    * t1_baronKills
    * t1_dragonKills
    * t1_riftHeraldKills
    * t2_towerKills
    * t2_inhibitorKills
    * t2_baronKills
    * t2_dragonKills
    * t2_riftHeraldKills
    ''')