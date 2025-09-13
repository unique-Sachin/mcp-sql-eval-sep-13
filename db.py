# Database connection for cricket analytics database in sqlite
from sqlalchemy import create_engine, text
from sqlalchemy.orm import sessionmaker

DB_CONNECTION_STRING = "sqlite:///cricket_analytics.db"


engine = create_engine(DB_CONNECTION_STRING)

Session = sessionmaker(bind=engine)


# create a session
def get_db():
    session = Session()
    try:
        yield session
    finally:
        session.close()

