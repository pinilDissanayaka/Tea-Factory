from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from database import session
from schema import AddSupplier
from models import Suplier


router = APIRouter(
    prefix="/supplier",
    tags=["supplier"]
)


@router.post("/add")
async def add_supplier(supplier:AddSupplier):
    existing_supplier = session.query(Suplier).filter_by(username=supplier.username).first()
    
    if existing_supplier:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Given supplier already exist"
        )
    else:

        new_supplier= Suplier(
            username = supplier.username,
            first_name = supplier.first_name,
            last_name = supplier.last_name,
            phone = supplier.phone,
            email = supplier.email,
            password = supplier.password,
            role = supplier.role
        )

        session.add(new_supplier)

        session.commit()

        return Response(
            content="Supplier Added Successfully",
            status_code=status.HTTP_201_CREATED
        )
