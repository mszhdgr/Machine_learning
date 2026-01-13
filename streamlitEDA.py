import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt

st.title("Explanatory Data Analysis")

file_uploader = st.file_uploader("upload csv file", type="csv")

if file_uploader is not None:
    df = pd.read_csv(file_uploader)
    st.subheader("Sample Data")
    st.write(df)

    st.subheader("Data Insight")
    st.write(df.describe())

    columns = df.columns
    selected_column = st.selectbox("Select Columns", columns)
    unique_column = df[selected_column].unique()
    selected_unique_column = st.selectbox("Unique values", unique_column)

    st.subheader("Plot Distribution", divider=True, text_alignment="center")

    x_column = st.selectbox("Select x-column", columns)
    y_column = st.selectbox("Select y-column", columns)

    st.bar_chart(df, x=x_column, y=y_column)

else:
    st.write("Waiting for File Upload!!")