from sqlalchemy import Column, Integer, String, Sequence, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from ..database import Base
from datetime import datetime
import enum


class Routes(Base):
    __tablename__ = 'route'
    route_id = Column(Integer, primary_key=True, index=True)
    route_name = Column(String, unique=True, index=True)
    distance = Column(Integer, index=True)
    password = Column(String, index=True)

    # Relationship to CheckedRouteQuantity
    checked_routes = relationship("CheckedRouteQuantity", back_populates="route")

