from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker,declarative_base

database_url = "sqlite:///./aitools.tb"

engine = create_engine(database_url,connect_args={"check_same_thread":False})

localSession = sessionmaker(autoflush=False,autocommit=False,bind=engine)

Base = declarative_base()

def get_db():
    db = localSession()
    try:
        yield db 
    except:
        db.close()