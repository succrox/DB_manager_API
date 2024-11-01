import requests
import pandas as pd
import streamlit as st
import os

st.title("Ordenes")

response = requests.get(os.getenv("API_DIR")+"orders/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

customers = requests.get(os.getenv("API_DIR")+"customers/")
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
    response = requests.post(os.getenv("API_DIR")+"orders/", json=data)
    if response.status_code == 200:
        st.success("Pedido agregado exitosamente")
    else:
        st.error("Error al agregar pedido")

st.title("Carga masiva de pedidos")

uploaded_file = st.file_uploader("Orders list excel file", type=["xls", "xlsx"])

save = st.button("Save orders")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'order_date': 'order_date',
                'customer_id': 'customer_id'
            })
            df['order_date'] = df['order_date'].astype(str)
            st.write(df)

            data = df.to_dict(orient="records")
            response = requests.post(os.getenv("API_DIR") + "orders/", json=data)
            if response.status_code == 200:
                st.success("Pedidos agregados exitosamente")
            else:
                st.error("Error al agregar pedidos")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")
