from datetime import datetime
from sqlalchemy import Column, ForeignKey, Integer, String, TIMESTAMP, JSON
from sqlalchemy.orm import relationship

from .database import Base, engine



class Users(Base):
    __tablename__ = "Users"
    
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String(256), nullable=False, unique=True, index=True)
    password = Column(String(128), nullable=False, index=True)
    username = Column(String(64), nullable=False)
    is_deleted = Column(TIMESTAMP, default=None)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)    #используется метод utcnow по причине того, что сервера могут располгаться в разных часовых поясах
    
    
    groups = relationship('Groups', back_populates='user')
    tasks = relationship('Tasks', back_populates='user')
    
class Tasks(Base):
    __tablename__ = "Tasks"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False, default='New Task')
    description = Column(String, nullable=True)
    status = Column(JSON, index=True, default='ToDo')
    is_deleted = Column(TIMESTAMP, default=None)
    created_at = Column(TIMESTAMP, default=datetime.utcnow)
    last_update = Column(TIMESTAMP)
    deadline = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    group_id = Column(Integer, ForeignKey('Groups.id'))
    
    user = relationship("Users", back_populates='tasks')
    groups = relationship('Groups', back_populates='tasks')
    

class Groups(Base):
    __tablename__ = "Groups"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), default="New Group", index=True)
    user_id = Column(Integer, ForeignKey('Users.id'))
    
    user = relationship("Users", back_populates='groups')
    tasks = relationship('Tasks', back_populates='groups')
    
    
Base.metadata.create_all(engine)