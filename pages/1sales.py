import requests
import pandas as pd
import streamlit as st
import os

st.title("Ventas")

response = requests.get(os.getenv("API_DIR")+"sales/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

st.title("Agregar Venta")

vendors = requests.get(os.getenv("API_DIR")+"vendors/")

vendors_data = vendors.json()
vendors_dict = {vendor['ID']: vendor['name'] for vendor in vendors_data}
vendors_ids = list(vendors_dict.keys())

id_vendor = st.selectbox("Nombre del Vendedor", vendors_ids, format_func=lambda id: vendors_dict[id])
name_client = st.text_input("Nombre del Cliente")
product_id = st.number_input("ID del Producto", min_value=1)
quantity = st.number_input("Cantidad", min_value=1)
tot_sale = st.number_input("Total de Venta", min_value=0.0, format="%.2f")
payment = st.selectbox("Método de Pago", ["Efectivo", "Tarjeta", "Transferencia"])
status = st.selectbox("Estado de Venta", ["Completado", "Pendiente", "Cancelado"])

if st.button("Agregar Venta"):
    data = [{
        "id_vendor": id_vendor,
        "name_client": name_client,
        "product_id": product_id,
        "quantity": quantity,
        "tot_sale": tot_sale,
        "payment": payment,
        "status": status
    }]
    response = requests.post(os.getenv("API_DIR")+"sales/", json=data)
    if response.status_code == 200:
        st.success("Venta agregada exitosamente")
    else:
        st.error("Error al agregar venta")

st.title("Carga masiva de ventas")

uploaded_file = st.file_uploader("Sales list excel file", type=["xls", "xlsx"])

save = st.button("Save sales")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'id_vendor': 'id_vendor',
                'name_client': 'name_client',
                'product': 'product_id',
                'quantity': 'quantity',
                'total_sale': 'tot_sale',
                'payment': 'payment',
                'status': 'status'
            })
            df['tot_sale'] = df['tot_sale'].astype(float)
            st.write(df)

            data = df.to_dict(orient="records")

            response = requests.post(os.getenv("API_DIR") + "sales/", json=data)
            if response.status_code == 200:
                st.success("Ventas agregadas exitosamente")
            else:
                st.error("Error al agregar ventas")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")
