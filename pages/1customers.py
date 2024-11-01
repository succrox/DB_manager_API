import requests
import pandas as pd
import streamlit as st
import os

st.title("Clientes")

response = requests.get(os.getenv("API_DIR")+"customers/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

st.title("Agregar Cliente")

customer_name = st.text_input("Nombre del Cliente")
contact_info = st.text_input("Información de Contacto")

if st.button("Agregar Cliente"):
    data = [{
        "customer_name": customer_name,
        "contact_info": contact_info
    }]
    response = requests.post(os.getenv("API_DIR")+"customers/", json=data)
    if response.status_code == 200:
        st.success("Cliente agregado exitosamente")
    else:
        st.error("Error al agregar cliente")

st.title("carga masiva de clientes")

uploaded_file = st.file_uploader("Lista de clientes en excel", type=["xls", "xlsx"])

save = st.button("Guardar clientes")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'customer_name': 'customer_name',
                'contact_info': 'contact_info'
            })
            st.write(df)

            data = df.to_dict(orient="records")
            response = requests.post(os.getenv("API_DIR") + "customers/", json=data)
            if response.status_code == 200:
                st.success("Clientes agregados exitosamente")
            else:
                st.error("Error al agregar clientes")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")