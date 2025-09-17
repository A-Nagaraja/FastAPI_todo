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
    def __init__(self):
        # Initialize database URL during instance creation
        self._database_url = self._get_database_url()

    def _get_database_url(self) -> str:
        """Get and validate database URL from environment variables."""
        # Get database URL from environment
        database_url = os.getenv("DATABASE_URL") or os.getenv("SQLALCHEMY_DATABASE_URL")

        print(f"Raw DATABASE_URL from environment: {database_url}")

        if not database_url:
            print("No DATABASE_URL found, using SQLite fallback")
            return "sqlite:///./TodoApplicationDatabase.db"

        # Handle different database URL formats
        if database_url.startswith("postgres://"):
            print("Converting postgres:// to postgresql://")
            database_url = database_url.replace("postgres://", "postgresql://", 1)
        elif database_url.startswith("mysql://"):
            print("Converting mysql:// to mysql+pymysql://")
            database_url = database_url.replace("mysql://", "mysql+pymysql://", 1)

        # Additional URL validation and fixes
        try:
            from urllib.parse import urlparse, urlunparse
            parsed = urlparse(database_url)

            # Check if URL is valid
            if not parsed.scheme:
                raise ValueError("Invalid database URL: missing scheme")

            # Validate based on database type
            if parsed.scheme in ["postgresql", "postgres"]:
                if not parsed.hostname:
                    raise ValueError("Invalid PostgreSQL URL: missing hostname")
                if not parsed.path or parsed.path == "/":
                    raise ValueError("Invalid PostgreSQL URL: missing database name")
            elif parsed.scheme in ["mysql", "mysql+pymysql"]:
                if not parsed.hostname:
                    raise ValueError("Invalid MySQL URL: missing hostname")
                if not parsed.path or parsed.path == "/":
                    raise ValueError("Invalid MySQL URL: missing database name")

            # Reconstruct URL to ensure it's properly formatted
            clean_url = urlunparse(parsed)
            print(f"Cleaned database URL: {clean_url}")
            return clean_url

        except Exception as e:
            print(f"Warning: Invalid database URL format: {e}")
            print(f"URL was: {database_url}")
            print(f"Using fallback SQLite database")
            return "sqlite:///./TodoApplicationDatabase.db"

    @property
    def database_url(self) -> str:
        return self._database_url

    # Security
    secret_key: str = os.getenv("SECRET_KEY", "change-me-in-prod")
    algorithm: str = os.getenv("ALGORITHM", "HS256")
    access_token_expire_minutes: int = int(os.getenv("ACCESS_TOKEN_EXPIRE_MINUTES", "30"))

    # Optional app config
    app_name: str = os.getenv("APP_NAME", "TodoApp")
    api_prefix: str = os.getenv("API_PREFIX", "/api")


settings = Settings()