from sqlalchemy import Column, DateTime, Integer, String
from sqlalchemy.sql import func

from app.db_conf import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    username = Column(String)
    email = Column(String)
    time_created = Column(DateTime(timezone=True), server_default=func.now())
