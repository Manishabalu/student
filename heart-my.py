import streamlit as st
import pandas as pd
import numpy as np
st.title("Heart-my")
datafile = st.file_uploader("Upload CSV",type=['csv'])
if datafile is not None:
   file_details = {"FileName":datafile.name,"FileType":datafile.type}
   df  = pd.read_csv(datafile)
   st.dataframe(df)
uploaded_file = st.file_uploader('https://github.com/Manishabalu/student/blob/1be1151c143a1633ccff1d7463d759daaee774a6/heart_failure_clinical_records_dataset.csv')



