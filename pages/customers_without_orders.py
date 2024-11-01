import requests
import pandas as pd
import streamlit as st
import os

st.title("Clientes sin ordenes")

response = requests.get(os.getenv("API_DIR")+"customers_without_orders/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")