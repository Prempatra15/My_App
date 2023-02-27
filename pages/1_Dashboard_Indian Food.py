import streamlit as st
import numpy as np
import pandas as pd
from matplotlib import image
import plotly.express as px
import os

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "food.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "indian_food.csv")

st.title("INDIAN FOOD")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

st.write(df.head())

st.write(df.describe())

time_option = df['cook_time'].unique().tolist()
time = st.selectbox("Select time:", time_option, 0)

data = df[df['cook_time'] == time]

fig = px.scatter(data, x='name', y='region', size='prep_time', color='state', hover_name='state')
st.write(fig)