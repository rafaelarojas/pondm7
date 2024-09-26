from sqlalchemy import Column, Integer, String, DateTime
from db.database import Base
from datetime import datetime

class Log(Base):
    __tablename__ = "Log"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow)
    message = Column(String, index=True)
