from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker



SQLALCHEMY_DATABASE_URL ="postgresql://task_tracker:track_pass_123@localhost/task_tracker"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

Session = sessionmaker(bind=engine, autoflush=False, autocommit=False)

Base = declarative_base()

session = Session()