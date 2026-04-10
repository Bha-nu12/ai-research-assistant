# 🚀 QUICK START GUIDE

## Run the Application (Choose ONE method)

### Method 1: Double-Click (Easiest)
1. Double-click **RUN_APP.bat**
2. Wait for browser to open automatically

### Method 2: Command Line
```bash
cd c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT
streamlit run app.py
```

### Method 3: PowerShell
```powershell
cd c:\Users\Dell\Documents\KUNFU\PROJECT_28_RAG_ASSISTANT
streamlit run app.py
```

---

## What to Expect

✅ Terminal/Command window opens  
✅ "You can now view your Streamlit app in your browser"  
✅ Browser opens to http://localhost:8501  
✅ AI Research Assistant Pro interface loads  

---

## First Time Use

1. **Upload Documents** (Sidebar → 📤 Upload tab)
   - Click "Select PDF files"
   - Choose 2-5 PDF documents
   - Click "🚀 Process PDFs"
   - Wait for "✅ Processed X documents" message

2. **Ask a Question** (Main area)
   - Type your research question
   - Example: "What are the main topics discussed?"
   - Click "🚀 Search & Synthesize"

3. **View Results**
   - Read the AI synthesis
   - Check agreements and contradictions
   - Review source chunks

---

## Troubleshooting

**Problem**: "No module named 'streamlit'"  
**Fix**: Run `pip install -r requirements.txt`

**Problem**: Browser doesn't open  
**Fix**: Manually go to http://localhost:8501

**Problem**: Port already in use  
**Fix**: Run `streamlit run app.py --server.port 8502`

**Problem**: API error  
**Fix**: Check .env file has valid GEMINI_API_KEY

---

## Stop the Application

Press **Ctrl+C** in the terminal window

---

## Need Help?

- Check **HOW_TO_RUN.md** for detailed instructions
- Check **TROUBLESHOOTING.md** for common issues
- Verify .env file has all API keys

---

**Ready? Run:** `streamlit run app.py`
