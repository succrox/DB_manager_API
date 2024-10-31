import streamlit as st
import requests

st.title("Agregar Cliente")

customer_name = st.text_input("Nombre del Cliente")
contact_info = st.text_input("Información de Contacto")

if st.button("Agregar Cliente"):
    data = [{
        "customer_name": customer_name,
        "contact_info": contact_info
    }]
    response = requests.post("http://localhost:8000/customers/", json=data)
    if response.status_code == 200:
        st.success("Cliente agregado exitosamente")
    else:
        st.error("Error al agregar cliente")
