from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine



SQLALCHEMY_DATABASE_URL ="postgresql+asyncpg://task_tracker:track_pass_123@localhost/task_tracker"

engine = create_async_engine(SQLALCHEMY_DATABASE_URL)

Session = async_sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

session = AsyncSession()