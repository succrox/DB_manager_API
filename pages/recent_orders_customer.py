import requests
import pandas as pd
import streamlit as st
import os

st.title("Ordenes de clientes por fecha")

response = requests.get(os.getenv("API_DIR")+"recent_orders_by_customer/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")