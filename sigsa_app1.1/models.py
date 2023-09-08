from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class User(Base):
    __tablename__ = "users"

    clave = Column(Integer, primary_key=True, index=True)
    nombre = Column(String)
    jefe_directo=Column (String)
    departamento = Column(String)
    fecha_ingreso = Column(String)
    antiguedad = Column(String)
    is_active = Column(Boolean, default=True)

