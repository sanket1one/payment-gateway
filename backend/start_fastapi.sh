#!/bin/bash

# Load environment variables from .env
export $(grep -v '^#' .env | xargs)

# Activate the virtual environment
source .venv/bin/activate  

# Run the Uvicorn server.
uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

deactivate