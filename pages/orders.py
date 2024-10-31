import streamlit as st
import requests

customers = requests.get("http://localhost:8000/customers/")
customers_data = customers.json()
customers_dict = {customer['customer_id']: customer['customer_name'] for customer in customers_data}

st.title("Agregar Pedido")

customer_id = st.selectbox("Cliente", options=list(customers_dict.keys()), format_func=lambda x: customers_dict[x])

order_date = st.date_input("Fecha del Pedido")

if st.button("Agregar Pedido"):
    data = [{
        "customer_id": customer_id,
        "order_date": str(order_date)
    }]
    response = requests.post("http://localhost:8000/orders/", json=data)
    if response.status_code == 200:
        st.success("Pedido agregado exitosamente")
    else:
        st.error("Error al agregar pedido")
