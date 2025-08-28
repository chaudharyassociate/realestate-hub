# Meta LLaMA 3 Model Service
FROM python:3.11-slim

WORKDIR /app

# Install dependencies
RUN pip install --no-cache-dir \
    fastapi \
    uvicorn \
    transformers \
    torch \
    requests \
    accelerate

# Copy service files
COPY llama-service.py /app/

# Install additional requirements if any
RUN echo "fastapi\nuvicorn\ntransformers\ntorch\nrequests\naccelerate" > requirements.txt && pip install --no-cache-dir -r requirements.txt

# Expose port
EXPOSE 8002

# Start the service
CMD ["uvicorn", "llama-service:app", "--host", "0.0.0.0", "--port", "8002"]