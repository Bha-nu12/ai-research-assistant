# Troubleshooting Guide

## Common Issues & Solutions

### 1. ModuleNotFoundError: No module named 'google.generativeai'

**Error:**
```
ModuleNotFoundError: No module named 'google.generativeai'
```

**Solution:**
```bash
# Activate virtual environment first
pip install google-generativeai==0.8.6

# Or reinstall all dependencies
pip install -r requirements.txt
```

### 2. API Key Not Configured

**Error:**
```
❌ **API Keys Not Configured**
Please create a `.env` file with your API keys
```

**Solution:**
1. Copy `.env.example` to `.env`:
   ```bash
   cp .env.example .env
   ```
2. Edit `.env` and add your actual API keys
3. Restart Streamlit: `streamlit run app.py`

### 3. GEMINI_API_KEY is None

**Error:**
```
Error: GEMINI_API_KEY is None
```

**Solution:**
- Verify `.env` file exists in project root directory
- Check `.env` has correct format: `GEMINI_API_KEY=your-key-here`
- No spaces around `=` sign
- Restart Streamlit after editing `.env`

### 4. Pinecone Connection Failed

**Error:**
```
Warning: Pinecone initialization failed: ...
```

**Solution:**
- This is non-critical; system runs in mock mode
- Verify `PINECONE_API_KEY` in `.env` if you want Pinecone
- Check Pinecone API key is valid at https://app.pinecone.io
- Ensure `PINECONE_ENVIRONMENT` matches your Pinecone region

### 5. PDF Upload Fails

**Error:**
```
Error processing documents: ...
```

**Solution:**
- Ensure PDF files are not corrupted
- Try uploading smaller PDFs first
- Check file permissions
- Verify `data/uploads/` directory exists and is writable

### 6. Streamlit Not Found

**Error:**
```
'streamlit' is not recognized as an internal or external command
```

**Solution:**
```bash
# Activate virtual environment
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux

# Install streamlit
pip install streamlit==1.28.1

# Run app
streamlit run app.py
```

### 7. Port 8501 Already in Use

**Error:**
```
Error: Address already in use
```

**Solution:**
```bash
# Run on different port
streamlit run app.py --server.port 8502

# Or kill existing process
# Windows:
netstat -ano | findstr :8501
taskkill /PID <PID> /F

# macOS/Linux:
lsof -i :8501
kill -9 <PID>
```

### 8. Gemini API Rate Limit

**Error:**
```
Error: Rate limit exceeded
```

**Solution:**
- Wait a few minutes before retrying
- Reduce batch size in `config.py`: `BATCH_SIZE = 16`
- Reduce number of documents processed at once
- Consider upgrading Gemini API plan

### 9. Cohere Reranking Fails

**Error:**
```
Reranking error: ...
```

**Solution:**
- Verify `COHERE_API_KEY` in `.env`
- Check Cohere API key is valid at https://dashboard.cohere.com
- System continues without reranking (graceful degradation)
- Reranking is optional; hybrid search still works

### 10. Virtual Environment Issues

**Problem:** Packages installed but not found

**Solution:**
```bash
# Verify virtual environment is activated
# Windows - should show (venv) in prompt
venv\Scripts\activate

# macOS/Linux
source venv/bin/activate

# Reinstall packages
pip install -r requirements.txt

# Verify installation
pip list | grep streamlit
```

### 11. Embedding Dimension Mismatch

**Error:**
```
Error: Vector dimension mismatch
```

**Solution:**
- Gemini embeddings are 768-dimensional
- Ensure `VECTOR_DIMENSION = 768` in `src/vector_store.py`
- If using different embedding provider, update dimension accordingly

### 12. Memory Issues with Large PDFs

**Error:**
```
MemoryError or process killed
```

**Solution:**
- Reduce `CHUNK_SIZE` in `config.py` (default: 1000)
- Process fewer documents at once
- Increase system RAM or use smaller PDFs
- Reduce `BATCH_SIZE` for embeddings

## Debug Mode

Enable debug logging:

```python
# In app.py, add at top:
import logging
logging.basicConfig(level=logging.DEBUG)
```

Then run:
```bash
streamlit run app.py --logger.level=debug
```

## Performance Optimization

### Slow Embedding Generation
- Reduce `BATCH_SIZE` in `config.py`
- Use fewer documents
- Check internet connection (API calls)

### Slow Search
- Reduce `TOP_K_RETRIEVAL` in `config.py`
- Disable reranking if not needed
- Use semantic search instead of hybrid

### Slow Report Generation
- Reduce number of retrieved chunks
- Use simpler prompts
- Check Gemini API quota

## Getting Help

1. Check this troubleshooting guide
2. Review error messages carefully
3. Check API provider status pages:
   - Google AI: https://status.cloud.google.com
   - Pinecone: https://status.pinecone.io
   - Cohere: https://status.cohere.com
4. Verify all dependencies: `pip list`
5. Check `.env` file configuration

## Reporting Issues

When reporting issues, include:
- Error message (full traceback)
- Python version: `python --version`
- Installed packages: `pip list`
- Operating system
- Steps to reproduce
- `.env` configuration (without API keys)
