# GPT-OSS - Open Source GPT Service
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    transformers \
    torch \
    requests

# Copy application files
COPY gpt-service.py /app/

# Install additional requirements if any
RUN echo "fastapi\nuvicorn\ntransformers\ntorch\nrequests" > requirements.txt && pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8001

# Start the service
CMD ["uvicorn", "gpt-service:app", "--host", "0.0.0.0", "--port", "8001"]