from sqlalchemy import Column, DateTime, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship
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


tags_comments = Table("tags_comments",
    Column("comment_id",Integer, ForeignKey("comments.id")),
    Column("tag_id",Integer, ForeignKey("tags.id"))
)
class Comment(Base, TimeStampMixIn, DeleteMixIn):
    __tablename__ = "comments"
    id = Column(Integer, primary_key= True)
    user_id = Column(Integer, ForeignKey("users.id"))
    content = Column(String, nullable=False)
    users = relationship("User")
    tags = relationship("Tag", secondary=tags_comments)

class Tag(Base, TimeStampMixIn, DeleteMixIn):
    __tablename__ = "tags"
    id = Column(Integer, primary_key=True)
    word = Column(String, nullable=False)
    comments = relationship("Comment", secundary = tags_comments)
