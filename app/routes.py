from fastapi import APIRouter, HTTPException
from app.models import (
    CustomerCreate, Customer, ProductCreate, Product,
    OrderCreate, Order, OrderDetailCreate, OrderDetail,
    VendorCreate, Vendor, SaleCreate, Sale
)
from app.DB_connection import get_db_connection
from typing import List

router = APIRouter()

# Inserción masiva de clientes (customers)
@router.post("/customers/", response_model=dict)
def bulk_insert_customers(customers: List[CustomerCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO customers (customer_name, contact_info) 
        VALUES (%s, %s)
        """
        values = [(customer.customer_name, customer.contact_info) for customer in customers]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Inserción masiva de productos (products)
@router.post("/products/", response_model=dict)
def bulk_insert_products(products: List[ProductCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO products (product_name, price) 
        VALUES (%s, %s)
        """
        values = [(product.product_name, product.price) for product in products]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Inserción masiva de órdenes (orders)
@router.post("/orders/", response_model=dict)
def bulk_insert_orders(orders: List[OrderCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO orders (order_date, customer_id) 
        VALUES (%s, %s)
        """
        values = [(order.order_date, order.customer_id) for order in orders]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Inserción masiva de detalles de pedido (order_details)
@router.post("/order_details/", response_model=dict)
def bulk_insert_order_details(order_details: List[OrderDetailCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO order_details (order_id, product_id, quantity) 
        VALUES (%s, %s, %s)
        """
        values = [(detail.order_id, detail.product_id, detail.quantity) for detail in order_details]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Inserción masiva de vendedores (vendors)
@router.post("/vendors/", response_model=dict)
def bulk_insert_vendors(vendors: List[VendorCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO vendors (name, zone, phone, email, goal, sales, commissions, clients, state, comments) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        values = [(vendor.name, vendor.zone, vendor.phone, vendor.email, vendor.goal, vendor.sales, vendor.commissions, 
                   vendor.clients, vendor.state, vendor.comments) for vendor in vendors]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

# Inserción masiva de ventas (sales)
@router.post("/sales/", response_model=dict)
def bulk_insert_sales(sales: List[SaleCreate]):
    conn = get_db_connection()
    cursor = conn.cursor()
    
    try:
        query = """
        INSERT INTO sales (id_vendor, name_client, product_id, quantity, tot_sale, payment, status) 
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        values = [(sale.id_vendor, sale.name_client, sale.product_id, sale.quantity, sale.tot_sale, sale.payment, sale.status) 
                  for sale in sales]
        
        cursor.executemany(query, values)
        conn.commit()

        return {"OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
