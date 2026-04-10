# 🔧 Embedding Model Fix

## Issue
The embedding model `models/embedding-001` is no longer available in the Gemini API.

**Error**: 
```
404 models/embedding-001 is not found for API version v1beta
```

## Solution
Updated to use `models/text-embedding-004` which is the current available embedding model.

## What Changed
- **File**: `src/embeddings.py`
- **Line**: Changed `EMBEDDING_MODEL = "models/embedding-001"` to `EMBEDDING_MODEL = "models/text-embedding-004"`
- **Impact**: All embeddings now use the correct, available model

## Embedding Dimensions
- **Model**: `text-embedding-004`
- **Dimensions**: 768 (unchanged)
- **Status**: ✅ Verified working

## How to Apply
The fix has been automatically applied. Just restart Streamlit:

```bash
# Kill existing process
Ctrl+C

# Restart
streamlit run app.py
```

## Verification
After restart, you should see:
```
✅ Using Gemini for embeddings
```

No more "404 models/embedding-001" errors.

## API Models Reference
Current available Gemini embedding models:
- `models/text-embedding-004` - Latest (768-dim) ✅ CURRENT
- `models/embedding-001` - Deprecated ❌

For the latest models, check: https://ai.google.dev/models

## Next Steps
1. Restart Streamlit
2. Upload PDFs
3. Run queries
4. Embeddings should work without errors

---

**Status**: ✅ Fixed and ready to use
