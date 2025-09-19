from database import Base
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean


class Users(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(255), unique = True)
    username = Column(String(255), unique=True)
    first_name = Column(String(255))
    last_name = Column(String(255))
    hashed_password = Column(String(255))
    is_active = Column(Boolean, default=True)
    role = Column(String(50))
    phone_number = Column(String(15))


class Todos(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    description = Column(String(1000))
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    owner_id = Column(Integer, ForeignKey("users.id"))