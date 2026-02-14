#Introduction to Streamlit
#Streamlit is an open-source app framework for Machine Learning and Data Science projects.
#  It allows you to create beautiful web applications for your machine learning and data science projects with simple Python scripts.

import streamlit as st
import pandas as pd
import numpy as np

# title of the application
st.title("Hello streamlit")

#display a simple text
st.write("this is a simple text")

#create a simple dataframe

df=pd.DataFrame({
    'first column':[1,2,3,4],
    'second column':[10,20,30,40]
})

#display the dataframe
st.write("here is the dataframe")
st.write(df)

#create a linechart
chart_data=pd.DataFrame(
    np.random.randn(20,3),columns=['a','d','c']
)
st.line_chart(chart_data)
