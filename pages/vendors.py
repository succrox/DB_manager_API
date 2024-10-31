import streamlit as st
import requests

st.title("Agregar Vendedor")

# Campos del formulario
nombre = st.text_input("Nombre del Vendedor")
zona = st.text_input("Zona")
telefono = st.text_input("Teléfono")
correo = st.text_input("Correo")
meta = st.number_input("Meta", min_value=0)
ventas = st.number_input("Ventas", min_value=0)
comisiones = st.number_input("Comisiones", min_value=0)
clientes = st.number_input("Clientes", min_value=0)
estado = st.selectbox("Estado", ["Activo", "Inactivo"])
comentarios = st.text_area("Comentarios")

# Enviar datos al servidor
if st.button("Agregar Vendedor"):
    data = [{
        "name": nombre,
        "zone": zona,
        "phone": telefono,
        "email": correo,
        "goal": meta,
        "sales": ventas,
        "commissions": comisiones,
        "clients": clientes,
        "state": estado,
        "comments": comentarios
    }]
    response = requests.post("http://localhost:8000/vendors/", json=data)
    if response.status_code == 200:
        st.success("Vendedor agregado exitosamente")
    else:
        st.error("Error al agregar vendedor")
