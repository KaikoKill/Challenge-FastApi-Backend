from typing import List
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey, Table, func
from sqlalchemy.orm import DeclarativeBase, relationship, Mapped, mapped_column
from datetime import datetime

class Base(DeclarativeBase):
    pass

class DeleteMixIn:
    is_deleted: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)

class TimeStampMixIn:
    created_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), server_default=func.now(), onupdate=func.now(), nullable=False)

class User(Base, DeleteMixIn, TimeStampMixIn):
    __tablename__ = "users"
    id:Mapped[int]= mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(String(255), unique=True, nullable=False)
    email: Mapped[str] = mapped_column(String(255), unique=True , nullable=False)
    name: Mapped[str] = mapped_column(String(255), nullable=False)
    last_name: Mapped[str] = mapped_column(String(255), nullable=False)
    password: Mapped[str] = mapped_column(String(72), nullable=False)
    comments: Mapped[List["Comment"]] = relationship(back_populates="user", cascade="all, delete-orphan")

tags_comments = Table(
                      "tags_comments",
                      Base.metadata,
                      Column("comment_id",Integer,ForeignKey("comments.id"), primary_key=True),
                      Column("tag_id", Integer, ForeignKey("tags.id"), primary_key=True)
)
class Comment(Base, TimeStampMixIn, DeleteMixIn):
    __tablename__ = "comments"
    id: Mapped[int] = mapped_column(primary_key= True)
    user_id: Mapped[int] = mapped_column(ForeignKey("users.id"))
    content: Mapped[str] = mapped_column(String(255), nullable=False)
    user: Mapped["User"] = relationship(back_populates="comments")
    tags: Mapped[List["Tag"]] = relationship(secondary=tags_comments, back_populates="comments")

class Tag(Base, TimeStampMixIn, DeleteMixIn):
    __tablename__ = "tags"
    id: Mapped[int] = mapped_column(primary_key=True)
    word: Mapped[str] = mapped_column(String(255), nullable=False)
    comments: Mapped[List["Comment"]] = relationship(secondary = tags_comments, back_populates="tags")

