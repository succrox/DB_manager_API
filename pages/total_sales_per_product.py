import requests
import pandas as pd
import streamlit as st
import os

st.title("Total de ventas por producto")

response = requests.get(os.getenv("API_DIR")+"total_sales_per_product/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")