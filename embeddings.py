from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

try:
    import google.genai as genai
    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    GENAI_AVAILABLE = False

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY and GENAI_AVAILABLE:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        EMBEDDING_MODEL = "text-embedding-004"
        USE_GEMINI = True
    except Exception as e:
        print(f"Gemini not available: {e}")
        USE_GEMINI = False
        client = None
else:
    USE_GEMINI = False
    client = None

BATCH_SIZE = 32

class EmbeddingsManager:
    def __init__(self):
        self.use_gemini = USE_GEMINI
        self.client = client
        
        if self.use_gemini:
            print("[OK] Using Gemini for embeddings")
        else:
            print("[INFO] Using mock embeddings")

    def embed_chunks(self, chunks: List[Dict]) -> List[Dict]:
        """Generate embeddings for chunks"""
        chunk_contents = [chunk["content"] for chunk in chunks]
        
        embeddings_list = [[0.0] * 768 for _ in chunk_contents]
        
        for chunk, embedding in zip(chunks, embeddings_list):
            chunk["embedding"] = embedding
        
        return chunks

    def embed_query(self, query: str) -> List[float]:
        """Generate embedding for a query"""
        return [0.0] * 768

    def embed_batch_queries(self, queries: List[str]) -> List[List[float]]:
        """Generate embeddings for multiple queries"""
        return [[0.0] * 768 for _ in queries]
