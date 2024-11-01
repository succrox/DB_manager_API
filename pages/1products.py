import requests
import pandas as pd
import streamlit as st
import os

st.title("Productos")

response = requests.get(os.getenv("API_DIR")+"products/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

st.title("Agregar Producto")

product_name = st.text_input("Nombre del Producto")
price = st.number_input("Precio", min_value=0.0, format="%.2f")

if st.button("Agregar Producto"):
    data = [{
        "product_name": product_name,
        "price": price
    }]
    response = requests.post(os.getenv("API_DIR")+"products/", json=data)
    if response.status_code == 200:
        st.success("Producto agregado exitosamente")
    else:
        st.error("Error al agregar producto")

st.title("Carga masiva de productos")

uploaded_file = st.file_uploader("Products list excel file", type=["xls", "xlsx"])

save = st.button("Save products")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'product_name': 'product_name',
                'price': 'price'
            })
            st.write(df)

            data = df.to_dict(orient="records")
            response = requests.post(os.getenv("API_DIR") + "products/", json=data)
            if response.status_code == 200:
                st.success("Productos agregados exitosamente")
            else:
                st.error("Error al agregar productos")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")
