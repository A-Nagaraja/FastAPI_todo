import os
from pathlib import Path

try:
    from dotenv import load_dotenv
    # Load .env from project root or this folder
    repo_root_env = Path(__file__).resolve().parents[1] / ".env"
    app_env = Path(__file__).resolve().parent / ".env"
    for candidate in (repo_root_env, app_env):
        if candidate.exists():
            load_dotenv(dotenv_path=candidate)
            break
except Exception:
    # If python-dotenv is missing, rely on real environment variables
    pass


class Settings:
    # Database: support both DATABASE_URL and legacy SQLALCHEMY_DATABASE_URL
    database_url: str = (
        os.getenv("DATABASE_URL")
        or os.getenv("SQLALCHEMY_DATABASE_URL")
        or "sqlite:///./TodoApplicationDatabase.db"
    )

    # Security
    secret_key: str = os.getenv("SECRET_KEY", "change-me-in-prod")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Optional app config
    app_name: str = os.getenv("APP_NAME", "TodoApp")
    api_prefix: str = os.getenv("API_PREFIX", "/api")


settings = Settings()