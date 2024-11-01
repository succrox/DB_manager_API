import requests
import pandas as pd
import streamlit as st
import os

st.title("Precio promedio de producto")

response = requests.get(os.getenv("API_DIR")+"average_product_price/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame([data])
    st.write(df)
else:
    st.error("Error fetching customers data")