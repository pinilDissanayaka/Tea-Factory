# from sqlalchemy import Column, Integer, String, Sequence, Enum, ForeignKey, DateTime
# from sqlalchemy.orm import relationship, backref
# from app.database import Base
# from datetime import datetime
# import enum

# class TeaLeaf(Base):
#     __tablename__ = 'tea_leaves'
#     leaf_id = Column(Integer, primary_key=True, index=True)
#     type = Column(String, unique=True, index=True)
#     grade = Column(String, unique=True, index=True)

# class Routes(Base):
#     __tablename__ = 'route'
#     route_id = Column(Integer, primary_key=True, index=True)
#     route_name = Column(String, unique=True, index=True)
#     distance = Column(Integer, index=True)
#     password = Column(String, index=True)

#     # Relationship to CheckedRouteQuantity
#     checked_routes = relationship("CheckedRouteQuantity", back_populates="route")

# class SuplierRole(enum.Enum):
#     normal = 'normal'
#     super = 'super'

# class Suplier(Base):
#     __tablename__ = 'supliers'
#     user_id = Column(Integer, Sequence('custom_suplier_id_seq', start=600, increment=1), primary_key=True)
#     username = Column(String(50), unique=True, nullable=False)
#     first_name = Column(String(50))
#     last_name = Column(String(50))
#     phone = Column(String(50))
#     email = Column(String(100), unique=True, nullable=False)
#     password = Column(String(255), nullable=False)
#     role = Column(Enum(SuplierRole), default=SuplierRole.normal)

#     def __repr__(self):
#         return f"<Suplier(username={self.username}, role={self.role})>"

# class SupplyData(Base):
#     __tablename__ = 'suply_tea'
#     suply_id = Column(Integer, Sequence('suply_tea_suply_id_seq', start=1, increment=1), primary_key=True)
#     suplier_id = Column(Integer, ForeignKey('supliers.user_id'))
#     leaf_id = Column(Integer, ForeignKey('tea_leaves.leaf_id'))
#     quantity = Column(Integer)
#     route_id = Column(Integer, ForeignKey('route.route_id'))
#     created_at = Column(DateTime)

#     # Relationships
#     suplier = relationship("Suplier", backref=backref("supplies", cascade="all, delete-orphan"))
#     tea_leaf = relationship("TeaLeaf", backref=backref("supplies", cascade="all, delete-orphan"))
#     route = relationship("Routes", backref=backref("supplies", cascade="all, delete-orphan"))

# class CheckedRouteQuantity(Base):
#     __tablename__ = 'check_route'
#     checked_id = Column(Integer, Sequence('custom_check_id_seq', start=1, increment=1), primary_key=True, index=True)
#     route_id = Column(Integer, ForeignKey('route.route_id'))
#     quantity = Column(Integer)
#     prod = Column(Integer)
#     reject = Column(Integer)
#     created_at = Column(DateTime, default=datetime.utcnow)  # Auto-set on insert
#     updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

#     # Relationship to route
#     route = relationship("Routes", back_populates="checked_routes")
