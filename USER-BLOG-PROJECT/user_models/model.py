from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from user_database.db import Base

class User(Base):
    __tablename__ = "all_users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(50), unique=True, nullable=False)
    password = Column(String(256), nullable=False)
    posts = relationship("Post", back_populates="owner")

class Post(Base):
    __tablename__ = "all_posts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    content = Column(String(1000), nullable=False)
    owner_id = Column(Integer, ForeignKey("all_users.id"))

    owner = relationship("User", back_populates="posts")
