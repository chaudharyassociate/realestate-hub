from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import time
import uuid

app = FastAPI(title="GPT-OSS Service", version="1.0.0")

class QueryRequest(BaseModel):
    prompt: str
    max_tokens: int = 1000
    temperature: float = 0.7

class QueryResponse(BaseModel):
    id: str
    model: str = "gpt-oss"
    response: str
    tokens_used: int
    timestamp: str

@app.get("/")
async def root():
    return {"message": "GPT-OSS Service is running", "model": "gpt-oss", "status": "ready"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "gpt-oss"}

@app.post("/v1/completions", response_model=QueryResponse)
async def create_completion(request: QueryRequest):
    try:
        # Simulate processing time
        processing_time = min(len(request.prompt) * 0.01, 2.0)
        time.sleep(processing_time)
        
        # Generate a mock response
        response_text = f"GPT-OSS Response: This is a simulated AI response to your prompt: '{request.prompt[:100]}{'...' if len(request.prompt) > 100 else ''}'. This is a placeholder implementation."
        
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
                "id": "gpt-oss",
                "object": "model",
                "owned_by": "cid-copilot",
                "permission": []
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8001)