# Docs link - https://fastapi.tiangolo.com/tutorial/sql-databases/

from sqlalchemy import create_engine # to connect with db we need sql engine
from sqlalchemy.orm import declarative_base, sessionmaker
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

SQLALCHEMY_DATABASE_URL = f"sqlite:///{os.path.join(BASE_DIR, 'product.db')}"


engine = create_engine(SQLALCHEMY_DATABASE_URL,
                        connect_args = {
                            "check_same_thread":False
                        }
                       )

engine = create_engine(SQLALCHEMY_DATABASE_URL)

session_local = sessionmaker(bind=engine,
                             autocommit = False,
                             autoflush=False
                             )

Base = declarative_base()

def get_db():
    db = session_local() #Creates a new DB session
    try:
        yield db # Sends db to the API endpoint and Keeps function alive until request is done
    finally:
        db.close() # Ensures DB connection is closed after request and Prevents memory leaks / connection exhaustion
