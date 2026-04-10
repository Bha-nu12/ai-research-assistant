# ⚡ Quick Fix Guide

## What Was Wrong
1. Embedding model `models/embedding-001` - Deprecated
2. LLM model `gemini-pro` - Deprecated

## What's Fixed
1. Embedding model → `models/text-embedding-004` ✅
2. LLM model → `gemini-1.5-flash` ✅

## What You Need to Do

### Step 1: Restart Streamlit
```bash
# Press Ctrl+C in terminal to stop current process

# Then run:
streamlit run app.py
```

### Step 2: Test It
1. Upload a PDF
2. Enter a question: "what is big data?"
3. Click "Search & Synthesize"
4. Should work now!

---

## Files Changed
- ✅ `src/embeddings.py` - Updated embedding model
- ✅ `src/synthesis.py` - Updated LLM model
- ✅ `src/report_generator.py` - Updated LLM model

---

## Expected Output After Fix

### When Starting
```
✅ Using Gemini for embeddings
Using Gemini for synthesis
Using Gemini for report generation
```

### When Querying
```
📊 Synthesis Results
[Your answer here with citations]

✅ Agreements
[Points of agreement]

⚠️ Contradictions
[Conflicting points]
```

---

## If Still Having Issues

1. **Check Streamlit restarted**: Look for "✅ Using Gemini" messages
2. **Check API key**: Verify `.env` has valid GEMINI_API_KEY
3. **Check internet**: Ensure connection to Gemini API
4. **Check logs**: Look for error messages in terminal

---

## That's It!

Just restart Streamlit and you're good to go. The models are now updated to the current available versions.

**Happy researching!** 🚀
