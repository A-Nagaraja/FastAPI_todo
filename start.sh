#!/bin/bash

# Debug environment variables
echo "=== Environment Debug ==="
echo "DATABASE_URL: $DATABASE_URL"
echo "PORT: $PORT"
echo "========================="

# Wait for database to be ready
echo "Waiting for database to be ready..."
sleep 5

# Test database connection
echo "Testing database connection..."

# Run database migrations
echo "Creating database tables..."
python -c "from database import engine; from models import Base; Base.metadata.create_all(bind=engine)"

# Start the application
echo "Starting FastAPI application..."
uvicorn main:app --host 0.0.0.0 --port $PORT
