from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.future import select
from sqlalchemy.orm import Session

from src.user.routers import router as user_router
from src.transaction.routers import router as transactions_router
from src.product.routers import router as product_router
from src.product import models, schemas
from .database import async_sessionmaker

app = FastAPI(
    title="Shop-backend"
)

def get_db():
    db = async_sessionmaker()
    try:
        yield db
    finally:
        db.close()


app.include_router(product_router)
app.include_router(transactions_router)
app.include_router(user_router)