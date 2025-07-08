import os
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.exc import OperationalError
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()

db_url = f"postgresql+psycopg2://{os.getenv('db_user')}:{os.getenv('db_password')}@{os.getenv('db_host')}:{os.getenv('db_port')}/{os.getenv('db_database')}"

try:
    engine = create_engine(db_url)
    SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

    # Test connection
    with engine.connect() as conn:
        conn.execute(text("SELECT 1"))  # ✅ wrap raw SQL in text()
except OperationalError:
    print("⚠️ Database connection failed. Using DummySession.")
    engine = None
    SessionLocal = None


class DummySession:
    """ A dummy session that safely ignores DB calls. """

    def __getattr__(self, name):
        def dummy_func(*args, **kwargs):
            return None

        return dummy_func


def get_db():
    if SessionLocal:
        db_session = SessionLocal()
        try:
            yield db_session
        finally:
            db_session.close()
    else:
        yield DummySession()
