from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4
from enum import Enum


class UserRegistration(BaseModel):
    username : str = Field(max_length=50, description="Username")
    password : str = Field(max_length=20, min_length=4, description="Password")
    nic : str = Field(max_length=50, description="NIC")
    email : EmailStr 
    phone : str = Field(max_length=10, description="Phone Number")


class UserLogin(BaseModel):
    username : str = Field(max_length=50, description="Username")
    password : str = Field(max_length=20, min_length=4, description="Password")


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
