from pydantic import BaseModel
from sqlalchemy import Boolean, Column, DateTime, Integer, String
from ..conf.connection import Base

class DeleteMixIn():
    @property
    def is_deleted(self):
        return self.is_delted
    def set_deleted(self,is_del:bool):
        self.is_delted=is_del

class TimeStampMixIn():
    @property
    def created_at(self):
        self.created_at= DateTime.now()
    @property
    def updated_at(self):
        self.updated_at=DateTime.now()

class User(Base, DeleteMixIn, TimeStampMixIn):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True, nullable=False)
    email = Column(String, unique=True , nullable=False)
    name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    password = Column(String, nullable=False)

