import chromadb
from app.config import settings
  
def get_chroma_client():
    return chromadb.HttpClient(
        host=settings.chroma_host,
        port=settings.chroma_port
    )

def get_or_create_collection(client, name: str):
    return client.get_or_create_collection(name=name)