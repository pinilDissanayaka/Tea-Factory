from pydantic import BaseModel, Field, EmailStr
from uuid import UUID, uuid4


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

    
