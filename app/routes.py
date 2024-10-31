from fastapi import APIRouter, HTTPException
from app.models import (
    CustomerCreate, Customer, ProductCreate, Product,
    OrderCreate, Order, OrderDetailCreate, OrderDetail,
    VendorCreate, Vendor, SaleCreate, Sale
)
from app.DB_connection import get_db_connection
from typing import List
from mysql.connector import Error

router = APIRouter()

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

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

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

        return {"message": "OK"}
    except Exception as e:
        conn.rollback()
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/vendors/")
def get_vendors():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM vendors")
        vendors = cursor.fetchall()
        return vendors
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/sales/")
def get_sales():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM sales")
        sales = cursor.fetchall()
        return sales
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/products/")
def get_products():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM products")
        products = cursor.fetchall()
        return products
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/customers/")
def get_customers():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM customers")
        customers = cursor.fetchall()
        return customers
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/orders/")
def get_orders():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM orders")
        orders = cursor.fetchall()
        return orders
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/order_details/")
def get_order_details():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM order_details")
        order_details = cursor.fetchall()
        return order_details
    except Error as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/sales_by_vendor/")
def get_sales_by_vendor():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT vendors.name AS vendor_name, SUM(sales.tot_sale) AS total_sales
            FROM vendors
            INNER JOIN sales ON vendors.id = sales.id_vendor
            GROUP BY vendors.name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/top_selling_products/")
def get_top_selling_products():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT products.product_name, SUM(order_details.quantity) AS total_quantity
            FROM products
            INNER JOIN order_details ON products.product_id = order_details.product_id
            GROUP BY products.product_name
            ORDER BY total_quantity DESC
            LIMIT 10
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/average_sales_per_customer/")
def get_average_sales_per_customer():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT customers.customer_name, AVG(sales.tot_sale) AS avg_sale
            FROM customers
            LEFT JOIN orders ON customers.customer_id = orders.customer_id
            LEFT JOIN sales ON orders.order_id = sales.id_sale
            GROUP BY customers.customer_name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/min_max_sales_per_vendor/")
def get_min_max_sales_per_vendor():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT vendors.name AS vendor_name, MIN(sales.tot_sale) AS min_sale, MAX(sales.tot_sale) AS max_sale
            FROM vendors
            INNER JOIN sales ON vendors.id = sales.id_vendor
            GROUP BY vendors.name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/orders_per_customer/")
def get_orders_per_customer():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT customers.customer_name, COUNT(orders.order_id) AS order_count
            FROM customers
            LEFT JOIN orders ON customers.customer_id = orders.customer_id
            GROUP BY customers.customer_name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/average_commission_per_vendor/")
def get_average_commission_per_vendor():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT name AS vendor_name, AVG(commissions) AS avg_commission
            FROM vendors
            GROUP BY vendor_name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/total_sales_by_zone/")
def get_total_sales_by_zone():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT vendors.zone, SUM(sales.tot_sale) AS total_sales
            FROM vendors
            LEFT JOIN sales ON vendors.id = sales.id_vendor
            GROUP BY vendors.zone
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/sales_orders_by_vendor_state/")
def get_sales_orders_by_vendor_state():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT 
                vendors.state AS vendor_state,
                COUNT(sales.id_sale) AS total_orders,
                SUM(sales.tot_sale) AS total_sales
            FROM vendors
            LEFT JOIN sales ON vendors.id = sales.id_vendor
            GROUP BY vendors.state
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/average_product_price/")
def get_average_product_price():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT AVG(price) AS avg_price
            FROM products
        """)
        result = cursor.fetchone()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/customers_without_orders/")
def get_customers_without_orders():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT customers.customer_name
            FROM customers
            LEFT JOIN orders ON customers.customer_id = orders.customer_id
            WHERE orders.order_id IS NULL
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/product_count_by_category/")
def get_product_count_by_category():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT products.product_name, COUNT(order_details.product_id) AS product_count
            FROM products
            LEFT JOIN order_details ON products.product_id = order_details.product_id
            GROUP BY products.product_name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/total_sales_per_product/")
def get_total_sales_per_product():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT products.product_name, SUM(order_details.quantity * products.price) AS total_sales
            FROM products
            INNER JOIN order_details ON products.product_id = order_details.product_id
            GROUP BY products.product_name
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/recent_orders_by_customer/")
def get_recent_orders_by_customer():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT customers.customer_name, orders.order_date
            FROM customers
            INNER JOIN orders ON customers.customer_id = orders.customer_id
            ORDER BY orders.order_date DESC
            LIMIT 10
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/total_sales_by_date/")
def get_total_sales_by_date():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT order_date, SUM(sales.tot_sale) AS total_sales
            FROM orders
            INNER JOIN sales ON orders.order_id = sales.id_sale
            GROUP BY order_date
            ORDER BY order_date DESC
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()

@router.get("/sales_summary_by_zone/")
def get_sales_summary_by_zone():
    conn = get_db_connection()
    try:
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""
            SELECT vendors.zone, SUM(sales.tot_sale) AS total_sales, AVG(sales.tot_sale) AS avg_sales
            FROM vendors
            INNER JOIN sales ON vendors.id = sales.id_vendor
            GROUP BY vendors.zone
        """)
        result = cursor.fetchall()
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()
