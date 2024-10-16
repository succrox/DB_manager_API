from fastapi import APIRouter, HTTPException
""" from app.models import CourseCreate, Course, StudentCreate, Student """
from app.DB_connection import get_db_connection
from typing import List

router = APIRouter()

@router.get("/")
def connection():
    conn = get_db_connection()
    try:
        if conn.is_connected():
            cursor = conn.cursor()
            cursor.execute("SELECT DATABASE();")
            record = cursor.fetchone()
            return (f"Conectado a la base de datos: {record[0]}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    finally:
        cursor.close()
        conn.close()