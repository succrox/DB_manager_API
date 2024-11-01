import requests
import pandas as pd
import streamlit as st
import os

st.title("Total de ventas por zona")

response = requests.get(os.getenv("API_DIR")+"sales_summary_by_zone/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")