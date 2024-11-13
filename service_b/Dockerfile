# Use a lightweight Python image
FROM python:3.11-slim


WORKDIR /app

# Install FastAPI and Uvicorn
RUN pip install fastapi uvicorn

# Copy the application code
COPY ./main.py /app/main.py

# Expose UDS path as a volume
VOLUME ["/tmp"]

# Run Uvicorn using the Unix Domain Socket
CMD ["uvicorn", "main:app", "--uds", "/tmp/service_b.sock"]
