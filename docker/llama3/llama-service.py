from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import time
import uuid

app = FastAPI(title="LLaMA 3 Service", version="1.0.0")

class QueryRequest(BaseModel):
    prompt: str
    max_tokens: int = 1000
    temperature: float = 0.7

class QueryResponse(BaseModel):
    id: str
    model: str = "llama3"
    response: str
    tokens_used: int
    timestamp: str

@app.get("/")
async def root():
    return {"message": "Meta LLaMA 3 Service is running", "model": "llama3", "status": "ready"}

@app.get("/health")
async def health():
    return {"status": "healthy", "service": "llama3"}

@app.post("/v1/completions", response_model=QueryResponse)
async def create_completion(request: QueryRequest):
    try:
        # Simulate processing time (LLaMA models are typically slower)
        processing_time = min(len(request.prompt) * 0.02, 3.0)
        time.sleep(processing_time)
        
        # Generate a mock response with LLaMA characteristics
        response_text = f"LLaMA 3 Analysis: Based on your input '{request.prompt[:100]}{'...' if len(request.prompt) > 100 else ''}', I can provide the following insights: This is a placeholder response from the Meta LLaMA 3 model service."
        
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
                "id": "llama3",
                "object": "model",
                "owned_by": "meta",
                "permission": []
            }
        ]
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)