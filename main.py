from fastapi import FastAPI
from app.routes import router
from pydantic import BaseModel, Field
from datetime import date
import streamlit as st

app = FastAPI()

app.include_router(router)