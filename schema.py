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


class AddEquipment(BaseModel):
    equipment_name : str = Field(description="Name of the equipment")
    equipment_type : str = Field(description="Type of the equipment")
    equipment_status : str = Field(description="Status of the equipment")
    description : str = Field(description="description of the equipment")
