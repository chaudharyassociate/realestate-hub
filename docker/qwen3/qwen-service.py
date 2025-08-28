from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import time
import uuid

app = FastAPI(title="Qwen 3 Service", version="1.0.0")

class QueryRequest(BaseModel):
    prompt: str
    max_tokens: int = 1000
    temperature: float = 0.7

class QueryResponse(BaseModel):
    id: str
    model: str = "qwen3"
    response: str
    tokens_used: int
    timestamp: str

@app.get("/")
async def root():
    return {"message": "Alibaba Qwen 3 Service is running", "model": "qwen3", "status": "ready"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "qwen3"}

@app.post("/v1/completions", response_model=QueryResponse)
async def create_completion(request: QueryRequest):
    try:
        # Simulate processing time
        processing_time = min(len(request.prompt) * 0.015, 2.5)
        time.sleep(processing_time)
        
        # Generate a mock response with Qwen characteristics
        response_text = f"Qwen 3 Intelligence: Analyzing your query '{request.prompt[:100]}{'...' if len(request.prompt) > 100 else ''}', here's my comprehensive response: This is a simulated output from Alibaba's Qwen 3 model, known for multilingual capabilities and reasoning."
        
        return QueryResponse(
            id=str(uuid.uuid4()),
            response=response_text,
            tokens_used=min(len(response_text) // 4, request.max_tokens),
            timestamp=time.strftime("%Y-%m-%dT%H:%M:%SZ")
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.get("/models")
async def list_models():
    return {
        "data": [
            {
                "id": "qwen3",
                "object": "model",
                "owned_by": "alibaba",
                "permission": []
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8003)