# #!/usr/bin/env python3
# """
# Script to create database tables for the TodoApp
# Run this script to recreate the users and todos tables
# """

# from sqlalchemy import create_engine, text
# from models import Base
# import os
# from dotenv import load_dotenv

# # Load environment variables
# load_dotenv()

# def create_tables():
#     """Create all tables defined in models.py"""

#     # Get database URL from environment or use the one you provided
#     database_url = os.getenv("SQLALCHEMY_DATABASE_URL", "mysql+pymysql://root:root@127.0.0.1:3306/TodoApplicationDatabase")

#     print(f"Connecting to database: {database_url}")

#     try:
#         # Create engine
#         engine = create_engine(database_url, echo=True)

#         # Test connection
#         with engine.connect() as connection:
#             result = connection.execute(text("SELECT 1"))
#             print("✅ Database connection successful!")

#         # Drop all tables first (if they exist) to avoid conflicts
#         print("🗑️  Dropping existing tables...")
#         Base.metadata.drop_all(bind=engine)

#         # Create all tables
#         print("🏗️  Creating tables...")
#         Base.metadata.create_all(bind=engine)

#         print("✅ Tables created successfully!")
#         print("📋 Created tables:")
#         for table_name in Base.metadata.tables.keys():
#             print(f"   - {table_name}")

#     except Exception as e:
#         print(f"❌ Error: {e}")
#         return False

#     return True

# if __name__ == "__main__":
#     print("🚀 Starting table creation process...")
#     success = create_tables()

#     if success:
#         print("\n🎉 All done! You can now run your FastAPI application.")
#         print("Run: uvicorn main:app --reload")
#     else:
#         print("\n💥 Table creation failed. Please check the error messages above.")
