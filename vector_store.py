from typing import List, Dict
import os

try:
    from pinecone import Pinecone, ServerlessSpec
    PINECONE_AVAILABLE = True
except ImportError:
    PINECONE_AVAILABLE = False
    Pinecone = None
    ServerlessSpec = None

PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
PINECONE_INDEX_NAME = "rag-research-assistant"
VECTOR_DIMENSION = 768

class VectorStore:
    def __init__(self):
        self.pc = None
        self.index = None
        self.index_name = PINECONE_INDEX_NAME
        
        if not PINECONE_AVAILABLE:
            print("Warning: Pinecone not available, using mock mode")
            return
        
        try:
            self.pc = Pinecone(api_key=PINECONE_API_KEY)
            self._initialize_index()
            self.index = self.pc.Index(self.index_name)
            print("Pinecone initialized successfully")
        except Exception as e:
            print(f"Warning: Pinecone initialization failed: {e}")
            self.pc = None
            self.index = None

    def _initialize_index(self):
        """Create Pinecone index if it doesn't exist"""
        if self.pc is None:
            return
        
        try:
            indexes = self.pc.list_indexes()
            if self.index_name not in [idx.name for idx in indexes]:
                self.pc.create_index(
                    name=self.index_name,
                    dimension=VECTOR_DIMENSION,
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region=PINECONE_ENVIRONMENT
                    )
                )
                print(f"Created index: {self.index_name}")
        except Exception as e:
            print(f"Index initialization error: {e}")

    def upsert_chunks(self, chunks: List[Dict]) -> int:
        """Upsert chunks with embeddings to Pinecone"""
        if self.index is None:
            print("Warning: Pinecone index not available, skipping upsert")
            return 0
        
        vectors = []
        
        for chunk in chunks:
            if "embedding" not in chunk:
                continue
            
            vector_id = f"{chunk['document']}_{chunk['chunk_id']}"
            metadata = {
                "document": chunk["document"],
                "content": chunk["content"][:500] if chunk["content"] else "",
                "page": chunk.get("page", 0),
                "chunk_id": str(chunk["chunk_id"])
            }
            
            vectors.append((
                vector_id,
                chunk["embedding"],
                metadata
            ))
        
        if vectors:
            try:
                self.index.upsert(vectors=vectors)
                print(f"Upserted {len(vectors)} vectors")
            except Exception as e:
                print(f"Error upserting vectors: {e}")
        
        return len(vectors)

    def search(self, query_embedding: List[float], top_k: int = 10,
               filter_dict: Dict = None) -> List[Dict]:
        """Search for similar chunks"""
        if self.index is None:
            return []
        
        try:
            results = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                include_metadata=True,
                filter=filter_dict
            )
            
            retrieved_chunks = []
            for match in results.matches:
                retrieved_chunks.append({
                    "id": match.id,
                    "score": match.score,
                    "document": match.metadata.get("document"),
                    "content": match.metadata.get("content"),
                    "page": match.metadata.get("page"),
                    "chunk_id": match.metadata.get("chunk_id")
                })
            
            return retrieved_chunks
        except Exception as e:
            print(f"Search error: {e}")
            return []

    def search_by_document(self, query_embedding: List[float], 
                          document_name: str, top_k: int = 10) -> List[Dict]:
        """Search within a specific document"""
        filter_dict = {"document": {"$eq": document_name}}
        return self.search(query_embedding, top_k, filter_dict)

    def delete_document(self, document_name: str):
        """Delete all vectors for a document"""
        if self.index is None:
            return
        
        try:
            self.index.delete(filter={"document": {"$eq": document_name}})
            print(f"Deleted vectors for document: {document_name}")
        except Exception as e:
            print(f"Delete error: {e}")

    def get_index_stats(self) -> Dict:
        """Get index statistics"""
        if self.index is None:
            return {"status": "Pinecone not available"}
        
        try:
            return self.index.describe_index_stats()
        except Exception as e:
            return {"status": f"Error: {e}"}
