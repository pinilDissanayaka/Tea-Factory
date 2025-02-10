from fastapi import APIRouter, HTTPException, status, Response
from fastapi.responses import JSONResponse
from schema import RouteLogin, AddRoute
from database import session
from models import User, Routes
from utils import get_hashed_password, verify_password, create_access_token, create_refresh_token



router = APIRouter(
    prefix="/auth",
    tags=["auth"]
)


@router.post("/login")
async def login(route: RouteLogin):
    existing_route = session.query(Routes).filter_by(route_id=route.route_id).first()

    if existing_route:
        if verify_password(password=route.password, hashed_pass=existing_route.password):
            return JSONResponse(
                content={
                    "access_token": create_access_token(subject=existing_route.route_id),
                    "refresh_token": create_refresh_token(subject=existing_route.route_id),
                    "details": existing_route.to_dict()
                },
                status_code=200
            )
        else:
            return HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Given password is incorrect"
            )
    else:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this user name does not exist"
        )
    

@router.post("/register")
async def register(route: AddRoute):
    existing_route = session.query(Routes).filter_by(route_id=route.route_id).first()

    if existing_route:
        return HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,            
            detail="User with this user name already exist"
        )
    else:
        new_route = Routes(
            route_id = route.route_id,
            route_name = route.route_name,
            distance = route.distance,
            password = get_hashed_password(password=route.password)
        )
        session.add(new_route)
        session.commit()

        return JSONResponse(
            content={
                "details": new_route.to_dict()
            }
        )


    
    



