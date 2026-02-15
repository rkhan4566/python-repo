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

from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier

@st.cache_data
def load_data():
    iris=load_iris()
    df=pd.DataFrame(iris.data,columns=iris.feature_names)
    df['species']=iris.target
    return df,iris.target_names

df,target_names=load_data()

model=RandomForestClassifier()
model.fit(df.iloc[:, :-1], df['species'])

st.sidebar.title("Input Features")

sepal_length = st.sidebar.slider(
    "Sepal length",
    float(df['sepal length (cm)'].min()),
    float(df['sepal length (cm)'].max())
)

sepal_width = st.sidebar.slider(
    "Sepal width",
    float(df['sepal width (cm)'].min()),
    float(df['sepal width (cm)'].max())
)

petal_length = st.sidebar.slider(
    "Petal length",
    float(df['petal length (cm)'].min()),
    float(df['petal length (cm)'].max())
)

petal_width = st.sidebar.slider(
    "Petal width",
    float(df['petal width (cm)'].min()),
    float(df['petal width (cm)'].max())
)

input_data = [[sepal_length, sepal_width, petal_length, petal_width]]

# Prediction
prediction = model.predict(input_data)
predicted_species = target_names[prediction[0]]

st.write("prediction")
st.write("the Predicted Species is:", predicted_species)
