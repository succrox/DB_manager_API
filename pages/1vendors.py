import requests
import pandas as pd
import streamlit as st
import os

st.title("Vendedores")

response = requests.get(os.getenv("API_DIR")+"vendors/")
if response.status_code == 200:
    data = response.json()
    df = pd.DataFrame(data)
    st.write(df)
else:
    st.error("Error fetching customers data")

st.title("Agregar Vendedor")

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
    response = requests.post(os.getenv("API_DIR")+"vendors/", json=data)
    if response.status_code == 200:
        st.success("Vendedor agregado exitosamente")
    else:
        st.error("Error al agregar vendedor")

st.title("Carga masiva de vendedores")

uploaded_file = st.file_uploader("Vendors list excel file", type=["xls", "xlsx"])

save = st.button("Save vendors")

if save:
    if uploaded_file is not None:
        try:
            df = pd.read_excel(uploaded_file)
            df = df.rename(columns={
                'name': 'name',
                'zone': 'zone',
                'phone': 'phone',
                'email': 'email',
                'goal': 'goal',
                'sales': 'sales',
                'commissions': 'commissions',
                'clients': 'clients',
                'state': 'state',
                'comments': 'comments'
            })
            df["phone"] = df["phone"].astype(str)
            st.write(df)

            data = df.to_dict(orient="records")
            
            response = requests.post(os.getenv("API_DIR") + "vendors/", json=data)
            if response.status_code == 200:
                st.success("Vendedores agregados exitosamente")
            else:
                st.error("Error al agregar vendedores")
        except Exception as e:
            st.error(f"Error leyendo el archivo Excel: {e}")
