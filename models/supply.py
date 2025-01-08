from sqlalchemy import Column, Integer, String, Sequence, Enum, ForeignKey, DateTime
from sqlalchemy.orm import relationship, backref
from ..database import Base
from datetime import datetime
import enum

class SupplyData(Base):
    __tablename__ = 'suply_tea'
    suply_id = Column(Integer, Sequence('suply_tea_suply_id_seq', start=1, increment=1), primary_key=True)
    suplier_id = Column(Integer, ForeignKey('supliers.user_id'))
    leaf_id = Column(Integer, ForeignKey('tea_leaves.leaf_id'))
    quantity = Column(Integer)
    route_id = Column(Integer, ForeignKey('route.route_id'))
    created_at = Column(DateTime, default=datetime.utcnow)

    # Relationships
    suplier = relationship("Suplier", backref=backref("supplies", cascade="all, delete-orphan"))
    tea_leaf = relationship("TeaLeaf", backref=backref("supplies", cascade="all, delete-orphan"))
    route = relationship("Routes", backref=backref("supplies", cascade="all, delete-orphan"))

