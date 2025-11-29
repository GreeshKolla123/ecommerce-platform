from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base, scoped_session
from sqlalchemy.orm.session import sessionmaker

SQLALCHEMY_DATABASE_URL = 'sqlite:///./app.db'

engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

SessionLocal = sessionmaker(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
