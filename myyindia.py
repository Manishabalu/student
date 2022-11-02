import streamlit as st
import pandas as pd
import numpy as np
import warnings
from pandas import read_csv
from pandas import datetime
    
st.title('**GOVERNMENT BUS DATA ANALYSIS**')
st.markdown("**PUBLIC TRANSPORT IN TAMIL NADU**") 
st.write("""
         **The State of Tamil Nadu is a forerunner in providing efficient, safe, affordable, comfortable, 3 reliable and 
         sustainable access for the growing number of city residents to jobs, education, recreation and such other needs 
         within the cities and rural people to reach cities and also all parts of the State are well connected with one another
         through dense and reliable road transport connectivity. The State Transport Undertakings under the administrative control of 
         the Government of Tamil Nadu are pioneers in public bus transport in India. The State Transport Undertakings transported about
         1.3142 Crore passengers every day and it was 1.7 Crore with all concession holders during the normal period of the year 2019-2020 
         which has temporarily come down to about 0.7 Crore per day in the year 2020-2021 and maintained about 0.76 Crore per day in the year
         2021-2022 (upto July 2021) due to Covid Pandemic. 4 To accomplish the vision of the Government, the State Transport Undertakings have 
         planned to introduce electric buses with financial assistance from KfW (German Development Bank) to make the public bus transport
         environment friendly in future.**
         """)
st.image("https://www.oneindia.com/ph-big/2018/01/bus-strike-hits-tamil-nadu_151525209780.jpg")


st.header('**BUS DATA**')

data = pd.read_csv("routedata1.csv", names = column);
st.table(data)

st.header('**DATA STUDIO**')
st.image("https://www.oneindia.com/ph-big/2018/01/bus-strike-hits-tamil-nadu_151525209780.jpg")
st.image("https://s01.sgp1.digitaloceanspaces.com/large/864234-78559-fevawrfter-1515398150.jpg")

st.write("**Thank You for your wonderful time**")
st.write("To get the source code click on the [link]https://colab.research.google.com/drive/1s1fLYhvS0lZLEg6BnAnegz4XblfTEmVp?usp=sharing")



