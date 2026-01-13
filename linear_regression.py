import pandas as pd
import streamlit as st
from sklearn.preprocessing import MinMaxScaler
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
import joblib
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(
    page_title="Linear regression algorithm",
    page_icon="📈",
    layout="wide",
    )


st.title("Linear Regression Algorithm")

col1, col2 = st.columns(2, gap="large")

with col1:
    st.subheader("Real Estate Dataset")
    df = pd.read_csv("./Real estate.csv")
    st.write(df.head(15))

with col2:
    st.subheader("Real Estate Map")
    st.map(df, latitude="X5 latitude", longitude="X6 longitude", height=450)

st.subheader("Explanatory Data Analysis", divider="yellow")

col3, col4, col5 = st.columns(3, gap="large")

with col3:
    st.write(df.describe())
with col4:
    st.line_chart(df, x="X2 house age", y="Y house price of unit area")
with col5:
    st.bar_chart(df, x="X4 number of convenience stores", y="Y house price of unit area")

st.subheader("Features Used For Model Training", divider="rainbow")
features = df[["X2 house age","X3 distance to the nearest MRT station","X4 number of convenience stores"]]
st.write(features)

# scale data

scaller = MinMaxScaler(feature_range=(1,10))
scalled_features = scaller.fit_transform(features)

y = df["Y house price of unit area"].values


# split data

X_train, X_test, y_train, y_test = train_test_split(scalled_features, y, test_size=0.2)

# train model

model = LinearRegression()
model.fit(X_train, y_train)

joblib.dump(model, "lr_model.pth")

# load model

loaded_model = joblib.load("lr_model.pth")
prediction = loaded_model.predict(X_test)

# visualize
st.divider()
st.subheader("Model Predictions")

col6, col7 = st.columns(2, gap="large")

with col6:

    fig,ax = plt.subplots()
    ax.plot(prediction, label="Prediction", c="blue")
    ax.plot(y_test, label="Actual values", c="green")
    ax.legend()

    st.pyplot(fig=fig)

with col7:

    st.subheader("Real Estate price prediction")


    with st.expander("Feature Entry"):
        c1, c2, c3 = st.columns(3)
        val1 = c1.number_input("Enter house age")
        val2 = c2.number_input("Enter distance(MRT station)")
        val3 = c3.number_input("Enter no. of c.stores")


    input_df = pd.DataFrame(
        [[val1, val2, val3]],
        columns=["X2 house age",
                "X3 distance to the nearest MRT station",
                "X4 number of convenience stores"
                ]
    )


    user_scaller = scaller.transform(input_df)


    if st.button("predict"):
        preds = loaded_model.predict(user_scaller)
        st.write("Your Real Estate price prediction is:", preds)