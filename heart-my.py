import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pandas import read_csv
from pandas import datetime
st.title('**HEART FAILURE PREDICTION**')
st.markdown("**MANISHA WELCOME U TO THIS WEB APP**") 
st.write("""
         **The health care industries collect huge amounts of data that contain some hidden information, which
         is useful for making effective decisions. For providing appropriate results and making effective decisions
         on data, some advanced data mining techniques are used. In this study, an effective heart disease prediction system 
         (EHDPS) is developed using neural network for predicting the risk level of heart disease. The system uses 15 medical
         parameters such as age, sex, blood pressure, cholesterol, and obesity for prediction. The EHDPS predicts the likelihood of patients getting heart disease. It enables significant knowledge, eg, relationships between medical factors related to heart disease and patterns, to be established. We have employed the multilayer perceptron neural network with backpropagation as the training algorithm. The obtained results have illustrated that the designed diagnostic system can effectively predict the risk level of heart diseases.**
         """)
st.image("https://media.istockphoto.com/vectors/3d-realistic-vector-isolated-human-heart-anatomically-correct-heart-vector-id1148910293?k=20&m=1148910293&s=612x612&w=0&h=9jvKArN3eCFYX92LINaUgLKkFlDp3xVbIrf00W6YQ3U=")


st.header('**SAMPLE DATASET**')
column = ['age','sex']
data = pd.read_csv("heart_failure_clinical_records_dataset.csv", names = column);
st.table(data)

st.header('**DATETIME ANALYSIS**')
dateparse = lambda dates: pd.datetime.strptime(dates, '%m/%d/%Y')
data = pd.read_csv("Heart_failure.pdf")names = column, parse_dates=['Month'], index_col=['age'],date_parser=dateparse);
st.line_chart(data)

st.write("**Thank You**")
st.write("To get the source code click on the [link]https://colab.research.google.com/drive/14YZQ2swFnimLR38cwTWnz7TezC_NOrus?usp=sharing")




