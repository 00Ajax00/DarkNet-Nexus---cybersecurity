# Use official Python image
FROM python:3.9

# Set working directory
WORKDIR /app

# Copy backend files
COPY ../backend /app

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose FastAPI/Flask default port
EXPOSE 8000

# Run the backend server
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
