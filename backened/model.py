from sqlalchemy import Column, Integer, String
from database import Base


class Request(Base):
    __tablename__ = "requests"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    request_type = Column(String)
    location = Column(String)
    priority = Column(String)
    status = Column(String)
