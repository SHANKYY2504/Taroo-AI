from db import Base
from sqlalchemy import Column, Integer, String

class User(Base):
    __tablename__ = 'users'
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)  # Store hashed passwords for security
    is_active = Column(Integer, default=1)  # 1 for active, 0 for inactive
