import streamlit as st
import requests

st.title("My mini machine learning frontend!")

sepal_length = st.slider("sepal_length", min_value=0.0, max_value=4.0, step=0.1)
sepal_width = st.slider("sepal_width", min_value=0.0, max_value=4.0, step=0.1)
petal_length = st.slider("petal_length", min_value=0.0, max_value=4.0, step=0.1)
petal_width = st.slider("petal_width", min_value=0.0, max_value=4.0, step=0.1)

url = "https://my-api-app-43984031362.europe-west6.run.app/predict"



params = dict(sepal_length= float(sepal_length),
          sepal_width = float(sepal_width),
          petal_length=float(petal_length),
          petal_width=float(petal_width))

response = requests.get(url, params)

f_class = response.json()['flower class']
st.write(f"The predicted class is {f_class}.")
