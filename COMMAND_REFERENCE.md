# COMMAND REFERENCE - Multi-Document RAG Research Assistant

## 🚀 STARTUP COMMANDS

### Windows (Recommended)
```bash
cd PROJECT_28_RAG_ASSISTANT
run.bat
```

### Windows (Manual)
```bash
cd PROJECT_28_RAG_ASSISTANT
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

### Mac/Linux
```bash
cd PROJECT_28_RAG_ASSISTANT
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
```

---

## 📦 DEPENDENCY MANAGEMENT

### Install All Dependencies
```bash
pip install -r requirements.txt
```

### Install Specific Package
```bash
pip install streamlit==1.28.1
pip install langchain==0.1.0
pip install pinecone-client==3.0.0
```

### Update All Packages
```bash
pip install --upgrade -r requirements.txt
```

### Check Installed Packages
```bash
pip list
```

### Create Requirements File
```bash
pip freeze > requirements.txt
```

---

## 🔧 CONFIGURATION COMMANDS

### Edit Configuration
```bash
# Windows
notepad config.py

# Mac/Linux
nano config.py
```

### Edit Environment Variables
```bash
# Windows
notepad .env

# Mac/Linux
nano .env
```

### View Configuration
```bash
cat config.py
cat .env
```

---

## 🎯 STREAMLIT COMMANDS

### Run Application
```bash
streamlit run app.py
```

### Run with Custom Port
```bash
streamlit run app.py --server.port 8502
```

### Run with Custom Host
```bash
streamlit run app.py --server.address 0.0.0.0
```

### Clear Cache
```bash
streamlit cache clear
```

### Run in Development Mode
```bash
streamlit run app.py --logger.level=debug
```

### Stop Application
```bash
Ctrl+C
```

---

## 📁 FILE MANAGEMENT

### Create Directories
```bash
mkdir data
mkdir data\uploads
mkdir data\indexes
```

### List Files
```bash
# Windows
dir

# Mac/Linux
ls -la
```

### View File Contents
```bash
# Windows
type filename.py

# Mac/Linux
cat filename.py
```

### Copy Files
```bash
# Windows
copy source.pdf destination.pdf

# Mac/Linux
cp source.pdf destination.pdf
```

### Delete Files
```bash
# Windows
del filename.pdf

# Mac/Linux
rm filename.pdf
```

---

## 🐍 PYTHON COMMANDS

### Check Python Version
```bash
python --version
```

### Run Python Script
```bash
python script.py
```

### Interactive Python Shell
```bash
python
```

### Exit Python Shell
```bash
exit()
```

### Run Python Module
```bash
python -m module_name
```

---

## 🔍 DEBUGGING COMMANDS

### Check Virtual Environment
```bash
# Windows
venv\Scripts\activate

# Mac/Linux
source venv/bin/activate
```

### Verify Virtual Environment Active
```bash
# Windows - should show (venv) in prompt
# Mac/Linux - should show (venv) in prompt
```

### Deactivate Virtual Environment
```bash
deactivate
```

### Check Python Path
```bash
python -c "import sys; print(sys.path)"
```

### Test Import
```bash
python -c "import streamlit; print(streamlit.__version__)"
```

---

## 📊 DATA MANAGEMENT

### Export Results to JSON
```bash
# In Python
import json
with open("results.json", "w") as f:
    json.dump(results, f, indent=2)
```

### Export Results to CSV
```bash
# In Python
import pandas as pd
df = pd.DataFrame(results)
df.to_csv("results.csv", index=False)
```

### Backup Collection
```bash
# Windows
xcopy data\indexes backup\indexes /E /I

# Mac/Linux
cp -r data/indexes backup/indexes
```

### Clear Cache
```bash
# Windows
rmdir /s data\indexes

# Mac/Linux
rm -rf data/indexes
```

---

## 🔐 API MANAGEMENT

### Test OpenAI Connection
```bash
python -c "from openai import OpenAI; print('OpenAI OK')"
```

### Test Pinecone Connection
```bash
python -c "from pinecone import Pinecone; print('Pinecone OK')"
```

### Test Cohere Connection
```bash
python -c "import cohere; print('Cohere OK')"
```

### Verify API Keys
```bash
# Windows
echo %OPENAI_API_KEY%

# Mac/Linux
echo $OPENAI_API_KEY
```

---

## 📝 DOCUMENT PROCESSING

### Process Single PDF
```python
from src.document_processor import DocumentProcessor

processor = DocumentProcessor()
metadata = processor.extract_pdf_metadata("document.pdf")
text, pages = processor.extract_text_from_pdf("document.pdf")
```

### Process Multiple PDFs
```python
pdf_paths = ["doc1.pdf", "doc2.pdf", "doc3.pdf"]
collection_data = processor.process_pdf_collection(pdf_paths)
```

### Save Metadata
```python
processor.save_collection_metadata(collection_data, "metadata.json")
```

---

## 🔎 RETRIEVAL COMMANDS

### Semantic Search
```python
from src.embeddings import EmbeddingsManager
from src.vector_store import VectorStore

embeddings = EmbeddingsManager()
vector_store = VectorStore()

query_embedding = embeddings.embed_query("Your question")
results = vector_store.search(query_embedding, top_k=10)
```

### Hybrid Search
```python
from src.retrieval import RetrieverWithReranking

retriever = RetrieverWithReranking(vector_store, embeddings)
results = retriever.retrieve_with_reranking("Your question", top_k=5)
```

### Per-Document Search
```python
results_by_doc = retriever.retrieve_from_documents(
    "Your question",
    document_names=["Document1.pdf", "Document2.pdf"]
)
```

---

## 📄 SYNTHESIS COMMANDS

### Generate Synthesis
```python
from src.synthesis import CrossDocumentSynthesis

synthesis = CrossDocumentSynthesis()
result = synthesis.synthesize_answer("Your question", retrieved_chunks)
```

### Detect Agreements
```python
agreements = synthesis.identify_agreements("Your question", chunks)
```

### Detect Contradictions
```python
contradictions = synthesis.detect_contradictions("Your question", chunks)
```

---

## 📊 REPORT GENERATION

### Generate Report
```python
from src.report_generator import ResearchReportGenerator

report_gen = ResearchReportGenerator()
report = report_gen.generate_report(
    query="Your question",
    synthesis_result=synthesis_result,
    agreements=agreements,
    contradictions=contradictions,
    documents=document_list
)
```

### Export to Word
```python
report_gen.export_to_docx(
    report_content,
    query="Your question",
    documents=document_list,
    output_path="report.docx"
)
```

### Export to Markdown
```python
report_gen.export_to_markdown(
    report_content,
    query="Your question",
    documents=document_list,
    output_path="report.md"
)
```

### Generate Analytics
```python
analytics = report_gen.generate_analytics(synthesis_results, documents)
```

---

## 🔄 BATCH PROCESSING

### Process Multiple Queries
```python
queries = [
    "Question 1?",
    "Question 2?",
    "Question 3?"
]

for query in queries:
    result = synthesis.synthesize_answer(query, chunks)
    print(result)
```

### Batch Embedding
```python
chunks_with_embeddings = embeddings.embed_chunks(chunks)
```

### Batch Upsert
```python
vector_store.upsert_chunks(chunks_with_embeddings)
```

---

## 🧹 MAINTENANCE COMMANDS

### Clear Pinecone Index
```python
from src.vector_store import VectorStore

vector_store = VectorStore()
vector_store.delete_document("Document_Name")
```

### Get Index Statistics
```python
stats = vector_store.get_index_stats()
print(stats)
```

### Rebuild Index
```bash
# Delete old index
# Reprocess documents
# Upsert to new index
```

### Backup Data
```bash
# Windows
xcopy data backup /E /I

# Mac/Linux
cp -r data backup
```

---

## 🐛 TROUBLESHOOTING COMMANDS

### Check Python Installation
```bash
python --version
python -m pip --version
```

### Verify Virtual Environment
```bash
# Windows
venv\Scripts\activate
python -c "import sys; print(sys.prefix)"

# Mac/Linux
source venv/bin/activate
python -c "import sys; print(sys.prefix)"
```

### Test Imports
```bash
python -c "import streamlit; import langchain; import pinecone; print('All OK')"
```

### Check API Connectivity
```bash
python -c "import requests; print(requests.get('https://api.openai.com').status_code)"
```

### View Error Logs
```bash
# Streamlit logs
streamlit run app.py --logger.level=debug

# Python errors
python -u app.py
```

---

## 📈 PERFORMANCE MONITORING

### Monitor Memory Usage
```bash
# Windows
tasklist | findstr python

# Mac/Linux
ps aux | grep python
```

### Check Disk Usage
```bash
# Windows
dir /s data

# Mac/Linux
du -sh data
```

### Monitor API Usage
```python
# Check in respective dashboards:
# - OpenAI: https://platform.openai.com/account/usage
# - Pinecone: https://app.pinecone.io
# - Cohere: https://dashboard.cohere.com
```

---

## 🚀 DEPLOYMENT COMMANDS

### Docker Build
```bash
docker build -t rag-assistant .
```

### Docker Run
```bash
docker run -p 8501:8501 rag-assistant
```

### Docker Push
```bash
docker tag rag-assistant username/rag-assistant
docker push username/rag-assistant
```

### Streamlit Cloud Deploy
```bash
streamlit cloud deploy
```

---

## 📚 DOCUMENTATION COMMANDS

### View README
```bash
# Windows
type README.md

# Mac/Linux
cat README.md
```

### View Prompt Guide
```bash
# Windows
type PROMPT_GUIDE.md

# Mac/Linux
cat PROMPT_GUIDE.md
```

### View Execution Guide
```bash
# Windows
type EXECUTION_GUIDE.md

# Mac/Linux
cat EXECUTION_GUIDE.md
```

---

## 🔗 USEFUL LINKS

### API Documentation
- OpenAI: https://platform.openai.com/docs
- Pinecone: https://docs.pinecone.io
- Cohere: https://docs.cohere.com

### Frameworks
- LangChain: https://python.langchain.com
- Streamlit: https://docs.streamlit.io

### Tools
- Python: https://www.python.org
- Git: https://git-scm.com
- Docker: https://www.docker.com

---

## 💡 QUICK TIPS

### Faster Startup
```bash
# Use run.bat on Windows
run.bat
```

### Better Performance
```python
# In config.py
TOP_K_RETRIEVAL = 10  # Fewer results
CHUNK_SIZE = 1500     # Larger chunks
```

### Debug Mode
```bash
streamlit run app.py --logger.level=debug
```

### Clear Cache
```bash
streamlit cache clear
```

### Kill Process
```bash
# Windows
taskkill /IM python.exe

# Mac/Linux
pkill -f streamlit
```

---

## ✅ COMMAND CHECKLIST

- [ ] `run.bat` - Quick start
- [ ] `pip install -r requirements.txt` - Install dependencies
- [ ] `streamlit run app.py` - Launch app
- [ ] `python -c "import streamlit"` - Test import
- [ ] `cat .env` - Verify API keys
- [ ] `streamlit cache clear` - Clear cache
- [ ] `docker build -t rag-assistant .` - Build Docker image

---

**Last Updated**: 2024
**Version**: 1.0.0
**Status**: Production Ready
