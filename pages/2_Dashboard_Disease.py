import streamlit as st
from matplotlib import image
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import os

st.title("Disease Data")

# absolute path to this file
FILE_DIR = os.path.dirname(os.path.abspath(__file__))
# absolute path to this file's root directory
PARENT_DIR = os.path.join(FILE_DIR, os.pardir)
# absolute path of directory_of_interest
dir_of_interest = os.path.join(PARENT_DIR, "resources")

IMAGE_PATH = os.path.join(dir_of_interest, "images", "Fungal_infection.jpg")
DATA_PATH = os.path.join(dir_of_interest, "data", "Disease.csv")

img = image.imread(IMAGE_PATH)
st.image(img)

df = pd.read_csv(DATA_PATH)
st.dataframe(df)

