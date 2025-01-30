from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from database import session
from models import User, Suplier



router = APIRouter(
    prefix="/collect",
    tags=["collect"]
)


@router.post("/collect")
async def collect():
    pass