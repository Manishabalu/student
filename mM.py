import streamlit as st
import pandas as pd
import numpy as np
st.title('MYY MOVIES')
streamlit run MYY_MOVIES.py
DATE_COLUMN = 'date/time'
DATA_URL = ("C:\Users\MANIVASH\Downloads\credits.csv.")

def load_data(nrows):
    data = pd.read_csv(DATA_URL, nrows=nrows)
    lowercase = lambda x: str(x).lower()
    data.rename(lowercase, axis='columns', inplace=True)
    data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
    return data
