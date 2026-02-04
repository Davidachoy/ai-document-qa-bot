from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.config import settings
from app.routes import test as test_router

app = FastAPI(title=settings.app_name)

# CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(test_router.router)

@app.get("/")
async def root():
    return {"message": "Doc Q&A API is running"}

@app.get("/health")
async def health_check():
    return {"status": "healthy"}


from app.services.openai_service import get_embedding
  
@app.post("/openai-test")
async def test_openai(text: str = "Hello world"):
    embedding = await get_embedding(text)
    return {
        "text": text,
        "embedding_length": len(embedding),
        "first_5_values": embedding[:5]
    }