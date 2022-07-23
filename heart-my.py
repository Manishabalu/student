import streamlit as st
import pandas as pd
import numpy as np
st.title("Heart-my")
datafile = st.file_uploader("Upload CSV",type=['csv'])
if datafile is not None:
   file_details = {"FileName":datafile.name,"FileType":datafile.type}
   df  = pd.read_csv(datafile)
   st.dataframe(df)
uploaded_file = st.file_uploader('')



