import os
from dotenv import load_dotenv

load_dotenv()

# API Configuration
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
PINECONE_API_KEY = os.getenv("PINECONE_API_KEY")
PINECONE_ENVIRONMENT = os.getenv("PINECONE_ENVIRONMENT", "us-east-1")
COHERE_API_KEY = os.getenv("COHERE_API_KEY")

# Model Configuration
LLM_MODEL = "gpt-4o"
EMBEDDING_MODEL = "text-embedding-3-small"
RERANKER_MODEL = "rerank-english-v2.0"

# Vector Store Configuration
VECTOR_DB_TYPE = "pinecone"  # Options: pinecone, weaviate
PINECONE_INDEX_NAME = "rag-research-assistant"
VECTOR_DIMENSION = 1536

# Chunking Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
HIERARCHICAL_CHUNK_SIZE = 3000

# Retrieval Configuration
TOP_K_RETRIEVAL = 20
TOP_K_RERANKED = 5
TOP_DOCUMENTS = 5
HYBRID_SEARCH_WEIGHT = 0.5

# Processing Configuration
BATCH_SIZE = 32
MAX_DOCUMENTS = 100
UPLOAD_FOLDER = "data/uploads"
INDEX_FOLDER = "data/indexes"

# Report Configuration
REPORT_FORMAT = "docx"  # Options: docx, pdf, markdown
INCLUDE_CITATIONS = True
INCLUDE_CONTRADICTIONS = True
INCLUDE_AGREEMENTS = True

# Logging
LOG_LEVEL = "INFO"
