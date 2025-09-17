from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from config import settings

# Create engine with error handling
try:
    print(f"Attempting to create engine with URL: {settings.database_url}")
    engine = create_engine(settings.database_url)
    print("✅ Database engine created successfully")
except Exception as e:
    print(f"❌ Error creating database engine: {e}")
    print("Falling back to SQLite...")
    # Fallback to SQLite if there's any issue
    engine = create_engine("sqlite:///./TodoApplicationDatabase.db")


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()