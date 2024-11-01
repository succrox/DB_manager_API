import requests
import pandas as pd
import streamlit as st
import os

st.title("Detalle de orden")

response = requests.get(os.getenv("API_DIR")+"order_details/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

products = requests.get(os.getenv("API_DIR")+"products/")
products_data = products.json()
products_dict = {product['product_id']: product['product_name'] for product in products_data}

orders = requests.get(os.getenv("API_DIR")+"orders/")
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
    response = requests.post(os.getenv("API_DIR")+"order_details/", json=data)
    if response.status_code == 200:
        st.success("Detalle de pedido agregado exitosamente")
    else:
        st.error("Error al agregar detalle de pedido")

st.title("Carga masiva de detalles de pedido")

uploaded_file = st.file_uploader("Order details list excel file", type=["xls", "xlsx"])

save = st.button("Save order details")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'order_id': 'order_id',
                'product_id': 'product_id',
                'quantity': 'quantity'
            })
            st.write(df)

            data = df.to_dict(orient="records")
            response = requests.post(os.getenv("API_DIR") + "order_details/", json=data)
            if response.status_code == 200:
                st.success("Detalles de pedido agregados exitosamente")
            else:
                st.error("Error al agregar detalles de pedido")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")

