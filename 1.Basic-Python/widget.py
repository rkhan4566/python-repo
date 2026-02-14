import streamlit as st
import pandas as pd

st.title("Streamlit Text Input")
name=st.text_input("enter your name")
age=st.slider("select your age",0,100,25)
st.write(f"your age is {age}.")

options=["python","java","c++","javaScript"]
choice = st.selectbox("choose your favorite language:",options)
st.write(f"you selected {choice}.")

if name:
    st.write(f"hello, {name}")

data={
    "name": ["john","jane","jake","jilli"],
    "age": [28,47,48,24],
    "City":["muri","silli","ranchi","jkharkhand"]
}

df=pd.DataFrame(data)
df.to_csv("sampledata.csv")
st.write(df)

uploaded_file=st.file_uploader("choose a CSV file",type="csv")
if uploaded_file is not None:
    df=pd.read_csv(uploaded_file)
    st.write(df)