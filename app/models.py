from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import date

class CustomerCreate(BaseModel):
    customer_name: str = Field(..., description="Nombre del cliente (campo requerido)")
    contact_info: Optional[str] = Field(None, description="Información de contacto del cliente")

class Customer(CustomerCreate):
    id: int

class ProductCreate(BaseModel):
    product_name: str = Field(..., description="Nombre del producto (campo requerido)")
    price: float = Field(..., description="Precio del producto")

class Product(ProductCreate):
    id: int

class OrderCreate(BaseModel):
    order_date: date = Field(..., description="Fecha de la orden (campo requerido)")
    customer_id: int = Field(..., description="ID del cliente (campo requerido)")

class Order(OrderCreate):
    id: int

class OrderDetailCreate(BaseModel):
    order_id: int = Field(..., description="ID de la orden (campo requerido)")
    product_id: int = Field(..., description="ID del producto (campo requerido)")
    quantity: int = Field(..., description="Cantidad de producto (campo requerido)")

class OrderDetail(OrderDetailCreate):
    id: int

class VendorCreate(BaseModel):
    name: str = Field(..., description="Nombre del vendedor (campo requerido)")
    zone: Optional[str] = Field(None, description="Zona del vendedor")
    phone: Optional[str] = Field(None, description="Teléfono del vendedor")
    email: Optional[EmailStr] = Field(None, description="Correo electrónico del vendedor")
    goal: Optional[int] = Field(None, description="Meta del vendedor")
    sales: Optional[int] = Field(None, description="Ventas realizadas por el vendedor")
    commissions: Optional[int] = Field(None, description="Comisiones del vendedor")
    clients: Optional[int] = Field(None, description="Número de clientes del vendedor")
    state: Optional[str] = Field(None, description="Estado del vendedor")
    comments: Optional[str] = Field(None, description="Comentarios sobre el vendedor")

class Vendor(VendorCreate):
    id: int

class SaleCreate(BaseModel):
    id_vendor: int = Field(..., description="ID del vendedor (campo requerido)")
    name_client: str = Field(..., description="Nombre del cliente (campo requerido)")
    product_id: int = Field(..., description="ID del producto (campo requerido)")
    quantity: int = Field(..., description="Cantidad de producto (campo requerido)")
    tot_sale: float = Field(..., description="Total de la venta")
    payment: str = Field(..., description="Método de pago")
    status: Optional[str] = Field(None, description="Estado de la venta")

class Sale(SaleCreate):
    id: int
