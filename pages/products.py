import streamlit as st
import requests

st.title("Agregar Producto")

# Campos del formulario
product_name = st.text_input("Nombre del Producto")
price = st.number_input("Precio", min_value=0.0, format="%.2f")

# Enviar datos al servidor
if st.button("Agregar Producto"):
    data = [{
        "product_name": product_name,
        "price": price
    }]
    response = requests.post("http://localhost:8000/products/", json=data)
    if response.status_code == 200:
        st.success("Producto agregado exitosamente")
    else:
        st.error("Error al agregar producto")
