from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings



# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={'check_same_thread':False})

engine = create_engine(settings.database_url)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()