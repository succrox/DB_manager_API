import streamlit as st
import requests

products = requests.get("http://localhost:8000/products/")
products_data = products.json()
products_dict = {product['product_id']: product['product_name'] for product in products_data}

orders = requests.get("http://localhost:8000/orders/")
orders_data = orders.json()
orders_dict = {order['order_id']: f"Pedido {order['order_id']} - {order['order_date']}" for order in orders_data}

st.title("Agregar Detalle de Pedido")

product_id = st.selectbox("Producto", options=list(products_dict.keys()), format_func=lambda x: products_dict[x])
order_id = st.selectbox("Pedido", options=list(orders_dict.keys()), format_func=lambda x: orders_dict[x])
quantity = st.number_input("Cantidad", min_value=1)

if st.button("Agregar Detalle de Pedido"):
    data = [{
        "order_id": order_id,
        "product_id": product_id,
        "quantity": quantity
    }]
    response = requests.post("http://localhost:8000/order_details/", json=data)
    if response.status_code == 200:
        st.success("Detalle de pedido agregado exitosamente")
    else:
        st.error("Error al agregar detalle de pedido")
