import streamlit as st
import requests

st.title("Agregar Venta")

vendors = requests.get("http://localhost:8000/vendors/")

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

# Enviar datos al servidor
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
    response = requests.post("http://localhost:8000/sales/", json=data)
    if response.status_code == 200:
        st.success("Venta agregada exitosamente")
    else:
        st.error("Error al agregar venta")
