from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from enum import Enum


class RouteLogin(BaseModel):
    route_id : int = Field(description="Username")
    password : str = Field(max_length=20, min_length=4, description="Password")


class AddRoute(BaseModel):
    route_id : int = Field(description="Route ID")
    route_name : str = Field(max_length=50, description="Route Name")
    distance : int = Field(description="Distance")
    password : str = Field(description="Password")

class CollectTea(BaseModel):
    pass


class AddSupplier(BaseModel):   
    class RoleChoice(str, Enum):
        normal = 'normal'
        super = 'super'

    
    username : str = Field(max_length=50, description="Username")
    first_name : str = Field(max_length=50, description="First Name")
    last_name : str = Field(max_length=50, description="Last Name")
    phone : str = Field(max_length=50, description="Phone Number")
    email : str = Field(max_length=50, description="Email")
    password : str = Field(max_length=50, description="Password")
    role : RoleChoice


class DeleteSupplier(BaseModel):
    username : str = Field(max_length=50, description="Username")
    password : str = Field(max_length=20, min_length=4, description="Password")
