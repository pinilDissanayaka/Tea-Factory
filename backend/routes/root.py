from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from database import session
from models import User, Routes, Suplier
from schema import RouteLogin
from utils import get_hashed_password, verify_password, create_access_token, create_refresh_token


router = APIRouter(
    prefix="",
    tags=["root"]
)


@router.get("/")
async def root():
    total_suppliers = session.query(Suplier).count()

    return {"total_suppliers": total_suppliers}