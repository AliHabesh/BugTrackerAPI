from enum import Enum as PythonEnum
from sqlalchemy import Integer, String, Column, Enum
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class StatusEnum(str, PythonEnum):
    PENDING = 'Pending'
    IN_PROGRESS = 'In Progress'
    RESOLVED = 'Resolved'


class Bug(Base):
    __tablename__ = 'bugs'

    id = Column(Integer, primary_key=True, index=True)
    issued_by = Column(String)
    status = Column(Enum(StatusEnum), index=True)  # Use SQLAlchemy's Enum here
    description = Column(String)
    assigned_to = Column(String)