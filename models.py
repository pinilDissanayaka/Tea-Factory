from database import Base
from sqlalchemy import Column, Integer, String, Text, BigInteger
from uuid import uuid4


class User(Base):
    __tablename__="user"

    user_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    username = Column(String(length=50), unique=True)
    password = Column(String(length=1000))
    nic = Column(String(length=50))
    email = Column(String(length=50))
    phone = Column(String(length=50))

    def to_dict(self):
        return {
            "user_id": self.user_id,
            "username": self.username,
            "nic": self.nic,
            "email": self.email,
            "phone": self.phone
        }

class Equipment(Base):
    __tablename__="equipment"

    equipment_id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    equipment_name = Column(String(length=50))
    equipment_type = Column(String(length=50))
    equipment_status = Column(String(length=50), nullable=True)
    description = Column(Text(length=1000), nullable=True)

    def to_dict(self):
        return {
            "equipment_id": self.equipment_id,
            "equipment_name": self.equipment_name,
            "equipment_type": self.equipment_type,
            "equipment_status": self.equipment_status,
            "description": self.description
        }
    

    


