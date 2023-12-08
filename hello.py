import streamlit as st
from PIL import Image
import numpy as np
import pandas as pd
from joblib import dump, load
import sklearn
from sklearn.linear_model import LogisticRegression




#Create header
st.write("""# League of Legends Winner Predictor""")
st.write("""## How it works""")
st.write("Model your predicted winner by using the left side of the screen to apply value to the different metrics. This will give you a predicted winning team based on your selections. "
         "The current selections are default values.")
st.write("## For more information visit:")

github = '[Code - Github](https://github.com/CoulsonZhang/6893BigData)'
st.write(github)

#image
image = Image.open('Assets/Arcane.jpeg')
st.image(image)

#Create and name sidebar
st.sidebar.header('Set your metrics')

st.sidebar.write("""#### Choose your SG bias""")

def user_input_features():
    firstInhibitor = st.sidebar.slider('First Inhibitor', 0, 1, 0)  # Assuming binary value (0 or 1)
    t1_towerKills = st.sidebar.slider('T1 Tower Kills', 0, 11, 0)  # Assuming max 11 towers
    t1_inhibitorKills = st.sidebar.slider('T1 Inhibitor Kills', 0, 3, 0)  # Assuming max 3 inhibitors
    t1_baronKills = st.sidebar.slider('T1 Baron Kills', 0, 5, 0)  # Assuming an arbitrary max of 5 barons
    t1_dragonKills = st.sidebar.slider('T1 Dragon Kills', 0, 5, 0)  # Assuming an arbitrary max of 5 dragons
    t2_towerKills = st.sidebar.slider('T2 Tower Kills', 0, 11, 0)  # Assuming max 11 towers
    t2_inhibitorKills = st.sidebar.slider('T2 Inhibitor Kills', 0, 3, 0)  # Assuming max 3 inhibitors
    t2_baronKills = st.sidebar.slider('T2 Baron Kills', 0, 5, 0)  # Assuming an arbitrary max of 5 barons
    t2_dragonKills = st.sidebar.slider('T2 Dragon Kills', 0, 5, 0)  # Assuming an arbitrary max of 5 dragons
    t2_riftHeraldKills = st.sidebar.slider('T2 Rift Herald Kills', 0, 2, 0)  # Assuming max 2 heralds

    user_data = {
        'firstInhibitor': firstInhibitor,
        't1_towerKills': t1_towerKills,
        't1_inhibitorKills': t1_inhibitorKills,
        't1_baronKills': t1_baronKills,
        't1_dragonKills': t1_dragonKills,
        't2_towerKills': t2_towerKills,
        't2_inhibitorKills': t2_inhibitorKills,
        't2_baronKills': t2_baronKills,
        't2_dragonKills': t2_dragonKills,
        't2_riftHeraldKills': t2_riftHeraldKills
    }

    features = pd.DataFrame(user_data, index=[0])
    return features


df_user = user_input_features()
st.write(df_user.shape)
st.write(df_user)
logistic_model = load('Mode_train/logistic_model.joblib')
prediction = logistic_model.predict(df_user)
st.write(prediction)