from datetime import datetime
from typing import AsyncGenerator
from fastapi import Depends
from fastapi_users_db_sqlalchemy import SQLAlchemyBaseUserTable, SQLAlchemyUserDatabase
from sqlalchemy import Boolean, Column, ForeignKey, Integer, String, TIMESTAMP
from sqlalchemy.orm import relationship, Mapped, mapped_column
from sqlalchemy.ext.asyncio import AsyncSession


from .database import Base, engine



class Users(SQLAlchemyBaseUserTable[int], Base):
    id: Mapped[int] = mapped_column(Integer, primary_key=True, index=True)
    email: Mapped[str] = mapped_column(String(length=320), unique=True, index=True, nullable=False)
    hashed_password: Mapped[str] = mapped_column(String(length=1024), nullable=False)
    is_active: Mapped[bool] = mapped_column(Boolean, default=True, nullable=False)
    is_superuser: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    is_verified: Mapped[bool] = mapped_column(Boolean, default=False, nullable=False)
    username = Column(String(64), nullable=False)
    registered_at = Column(TIMESTAMP, default=datetime.utcnow)    #используется метод utcnow по причине того, что сервера могут располгаться в разных часовых поясах
    
    group = relationship('Groups', back_populates='user')
    task = relationship('Tasks', back_populates='user')
    
class Tasks(Base):
    __tablename__ = "task"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), nullable=False, default='New Task')
    description = Column(String, nullable=True)
    status = Column(String, index=True, default='ToDo')
    is_deleted = Column(TIMESTAMP, default=None)
    created_at = Column(TIMESTAMP, default=datetime.utcnow())
    last_update = Column(TIMESTAMP)
    deadline = Column(TIMESTAMP, nullable=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    group_id = Column(Integer, ForeignKey('group.id'), nullable=True, default=None)
    
    user = relationship("Users", back_populates='task')
    group = relationship('Groups', back_populates='task')
    

class Groups(Base):
    __tablename__ = "group"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(64), default="New Group", index=True)
    user_id = Column(Integer, ForeignKey('user.id'))
    
    user = relationship("Users", back_populates='group')
    task = relationship('Tasks', back_populates='group')
    
    
#Base.metadata.create_all(engine)


async def get_async_session() -> AsyncGenerator[AsyncSession, None]:
    async with session() as session:
        yield session


async def get_user_db(session: AsyncSession = Depends(get_async_session)):
    yield SQLAlchemyUserDatabase(session, Users)