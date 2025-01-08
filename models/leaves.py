from sqlalchemy import Column, Integer, String
from ..database import Base

class TeaLeaf(Base):
    __tablename__ = 'tea_leaves'
    leaf_id = Column(Integer, primary_key=True, index=True)
    type = Column(String, unique=True, index=True)
    grade = Column(String, unique=True, index=True)