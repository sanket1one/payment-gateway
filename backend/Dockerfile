FROM python:3.12.9-alpine3.21

WORKDIR /app

# Installing dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application
COPY . .

# Expose backend port
EXPOSE 8000

# Run the FastAPI server
CMD ["uvicorn", "app.main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]