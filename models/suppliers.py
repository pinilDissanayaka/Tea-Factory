from sqlalchemy import Column, Integer, String, Sequence, Enum
from ..database import Base
import enum

class SuplierRole(enum.Enum):
    normal = 'normal'
    super = 'super'

class Suplier(Base):
    __tablename__ = 'supliers'
    user_id = Column(Integer, Sequence('custom_suplier_id_seq', start=600, increment=1), primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    first_name = Column(String(50))
    last_name = Column(String(50))
    phone = Column(String(50))
    email = Column(String(100), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    role = Column(Enum(SuplierRole), default=SuplierRole.normal)

    def __repr__(self):
        return f"<Suplier(username={self.username}, role={self.role})>"
