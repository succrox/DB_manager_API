import requests
import pandas as pd
import streamlit as st
import os

st.title("Ventas por estado del vendedor")

response = requests.get(os.getenv("API_DIR")+"sales_orders_by_vendor_state/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")