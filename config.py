# config.py
from dotenv import load_dotenv
import os

load_dotenv()  # Load .env file

class Settings:
    def __init__(self):
        self.database_url = self._get_database_url()
        self.secret_key = os.getenv("SECRET_KEY", "change-me-in-prod")
        self.algorithm = os.getenv("ALGORITHM", "HS256")
        self.access_token_expire_minutes = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))
        self.app_name = os.getenv("APP_NAME", "TodoApp")
        self.api_prefix = os.getenv("API_PREFIX", "/api")

    def _get_database_url(self) -> str:
        """
        Prefer DATABASE_URL (Render, Heroku) if present,
        else fallback to SQLALCHEMY_DATABASE_URL,
        else fallback to SQLite.
        """
        database_url = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URL")

        if not database_url:
            return "sqlite:///./TodoApplicationDatabase.db"

        # Fix SQLAlchemy compatibility
        if database_url.startswith("postgres://"):
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        elif database_url.startswith("mysql://"):
            database_url = database_url.replace("mysql://", "mysql+pymysql://", 1)

        return database_url


settings = Settings()

# print(f"Database URL: {settings.database_url}")
# print(f"Secret Key: {settings.secret_key}")
# print(f"Algorithm: {settings.algorithm}")
# print(f"Access Token Expire Minutes: {settings.access_token_expire_minutes}")
# print(f"App Name: {settings.app_name}")
# print(f"API Prefix: {settings.api_prefix}")