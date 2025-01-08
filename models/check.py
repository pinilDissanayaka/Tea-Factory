from sqlalchemy import Column, Integer, String, Sequence, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from ..database import Base
from datetime import datetime
import enum


class CheckedRouteQuantity(Base):
    __tablename__ = 'check_route'
    checked_id = Column(Integer, Sequence('custom_check_id_seq', start=1, increment=1), primary_key=True, index=True)
    route_id = Column(Integer, ForeignKey('route.route_id'))
    quantity = Column(Integer)
    prod = Column(Integer)
    reject = Column(Integer)
    created_at = Column(DateTime, default=datetime.utcnow)  # Auto-set on insert
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationship to route
    route = relationship("Routes", back_populates="checked_routes")
