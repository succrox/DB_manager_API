import requests
import pandas as pd
import streamlit as st
import os

st.title("Promedio de comisiones por vendedor")

response = requests.get(os.getenv("API_DIR")+"average_commission_per_vendor/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")