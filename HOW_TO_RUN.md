# HOW TO RUN - Multi-Document RAG Research Assistant

## Quick Start (3 Steps)

### Step 1: Install Dependencies
```bash
cd c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT
pip install -r requirements.txt
```

### Step 2: Verify .env File
Make sure your `.env` file contains:
```
GEMINI_API_KEY=AIzaSyAPch7yvp7ooD_zvvsBTMd3BpoiND6p7_c
EMBEDDING_PROVIDER=gemini
LLM_PROVIDER=gemini
PINECONE_API_KEY=pcsk_6WtNic_UZRP92Wt2SKFmaxDowKV3W71HUT8BdNZwStFbWZUo2rKEneJBSxicDheBrMbZeA
PINECONE_ENVIRONMENT=us-east-1
COHERE_API_KEY=n7OhwCRKEsbeewGACqTe3PHoZnnaHerRavnsRoFJ
```

### Step 3: Run the Application
```bash
streamlit run app.py
```

OR simply double-click: **RUN_APP.bat**

---

## Alternative: Manual Steps

### Option A: Using Command Prompt
1. Open Command Prompt (cmd)
2. Navigate to project folder:
   ```
   cd c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

### Option B: Using PowerShell
1. Open PowerShell
2. Navigate to project folder:
   ```
   cd c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT
   ```
3. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
4. Run the app:
   ```
   streamlit run app.py
   ```

### Option C: Using the Batch File
1. Navigate to: `c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT`
2. Double-click: **RUN_APP.bat**

---

## What Happens When You Run

1. **Browser Opens**: Streamlit will automatically open your default browser
2. **URL**: Usually http://localhost:8501
3. **Interface**: You'll see the AI Research Assistant Pro interface

---

## Using the Application

### 1. Upload Documents
- Click on **"📤 Upload"** tab in the sidebar
- Choose **"PDF Files"** or **"ZIP Archive"**
- Select your PDF files
- Click **"🚀 Process PDFs"**

### 2. Ask Questions
- Enter your research question in the main text area
- Choose search type: Hybrid Search, Semantic Search, or Per-Document
- Adjust number of results (5-50)
- Click **"🚀 Search & Synthesize"**

### 3. View Results
- **Synthesis**: AI-generated answer from all documents
- **Agreements**: Points where documents agree
- **Contradictions**: Conflicting information between documents
- **Retrieved Chunks**: Source text excerpts

### 4. Generate Reports (Optional)
- Check **"📄 Report"** before searching
- Download the generated Word document

---

## Troubleshooting

### Issue: "No module named 'google.genai'"
**Solution:**
```bash
pip install google-genai
```

### Issue: "No module named 'streamlit'"
**Solution:**
```bash
pip install -r requirements.txt
```

### Issue: "API Keys Not Configured"
**Solution:**
1. Check if `.env` file exists in project folder
2. Verify API keys are correct
3. Restart the application

### Issue: Port Already in Use
**Solution:**
```bash
streamlit run app.py --server.port 8502
```

### Issue: Browser Doesn't Open
**Solution:**
Manually open: http://localhost:8501

---

## Stopping the Application

- Press **Ctrl+C** in the terminal/command prompt
- Or close the terminal window

---

## System Requirements

- **Python**: 3.8 or higher
- **RAM**: 4GB minimum (8GB recommended)
- **Internet**: Required for API calls (Gemini, Pinecone, Cohere)
- **Browser**: Chrome, Firefox, Edge, or Safari

---

## File Structure

```
PROJECT_28_RAG_ASSISTANT/
├── app.py                  # Main Streamlit application
├── config.py               # Configuration settings
├── requirements.txt        # Python dependencies
├── .env                    # API keys (DO NOT SHARE)
├── RUN_APP.bat            # Quick start script
├── src/                    # Source code modules
│   ├── document_processor.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── retrieval.py
│   ├── synthesis.py
│   └── report_generator.py
└── data/                   # Data storage
    ├── uploads/            # Uploaded PDFs
    └── indexes/            # Generated reports
```

---

## Next Steps After Running

1. **Upload Test Documents**: Start with 2-3 PDFs
2. **Try Sample Queries**:
   - "Summarize the main topics"
   - "Compare the different approaches"
   - "What are the key findings?"
3. **Explore Features**: Try different search types and report generation
4. **Check Analytics**: View collection statistics in sidebar

---

## Support

For issues or questions:
1. Check TROUBLESHOOTING.md
2. Review error messages in terminal
3. Verify API keys are valid
4. Ensure all dependencies are installed

---

**Ready to Start?**

Run: `streamlit run app.py` or double-click **RUN_APP.bat**
