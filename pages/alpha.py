import requests
import pandas as pd
import streamlit as st
import os


response = requests.get(os.getenv("API_DIR")+"vendors/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write("Vendors Table")
    st.write(df)
else:
    st.error("Error fetching vendors data")
