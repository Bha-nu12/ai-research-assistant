# 🚀 START HERE - Multi-Document RAG Research Assistant

Welcome! This guide will help you get started in 5 minutes.

## ⏱️ Quick Start (5 minutes)

### Step 1: Setup Virtual Environment
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # macOS/Linux
```

### Step 2: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 3: Configure API Keys
```bash
cp .env.example .env
# Edit .env and add your API keys
```

### Step 4: Run Application
```bash
streamlit run app.py
```

**Done!** Open http://localhost:8501

---

## 📚 Documentation Guide

Choose your path based on your needs:

### 👤 I'm New to This Project
1. Read [README.md](README.md) - 5 min overview
2. Follow [SETUP_GUIDE.md](SETUP_GUIDE.md) - Detailed setup
3. Try [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Common commands

### 🔑 I Need to Setup API Keys
1. Read [SECURITY_GUIDE.md](SECURITY_GUIDE.md) - Best practices
2. Get keys from:
   - Gemini: https://makersuite.google.com/app/apikey
   - Pinecone: https://app.pinecone.io
   - Cohere: https://dashboard.cohere.com
3. Add to `.env` file

### 🐛 I'm Having Issues
1. Check [TROUBLESHOOTING.md](TROUBLESHOOTING.md) - Common problems
2. Search for your error message
3. Follow the solution steps

### 🚢 I Want to Deploy
1. Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
2. Choose your platform
3. Follow step-by-step instructions

### 💻 I Want to Understand the Code
1. Read [README.md](README.md) - Architecture section
2. Review `src/` folder structure
3. Check [QUICK_REFERENCE.md](QUICK_REFERENCE.md) - Configuration

---

## 🎯 Common Tasks

### Upload and Query Documents
```
1. Open http://localhost:8501
2. Sidebar → Upload tab
3. Select PDF files
4. Click "Process PDFs"
5. Enter research question
6. Click "🚀 Search & Synthesize"
```

### Generate a Report
```
1. Upload documents (see above)
2. Check "Generate Report" checkbox
3. Click "🚀 Search & Synthesize"
4. Click "📥 Download Report"
```

### Change Configuration
```
1. Edit config.py
2. Restart Streamlit (Ctrl+C, then streamlit run app.py)
3. Changes take effect
```

### Add New API Keys
```
1. Edit .env file
2. Add your API key
3. Restart Streamlit
4. Check sidebar for status
```

---

## 📋 File Overview

### Essential Files
- **app.py** - Main application (don't edit unless you know what you're doing)
- **.env** - Your API keys (KEEP SECRET, don't commit)
- **config.py** - Settings you can customize
- **requirements.txt** - Python dependencies

### Documentation
- **README.md** - Project overview
- **SETUP_GUIDE.md** - Installation guide
- **QUICK_REFERENCE.md** - Common commands
- **TROUBLESHOOTING.md** - Problem solutions
- **SECURITY_GUIDE.md** - API key management
- **DEPLOYMENT_GUIDE.md** - Production deployment

### Source Code
- **src/document_processor.py** - PDF processing
- **src/embeddings.py** - Vector generation
- **src/vector_store.py** - Vector database
- **src/retrieval.py** - Search & reranking
- **src/synthesis.py** - Answer generation
- **src/report_generator.py** - Report creation

### Data Folders
- **data/uploads/** - Your uploaded PDFs
- **data/indexes/** - Generated reports

---

## ✅ Checklist: First Time Setup

- [ ] Python 3.8+ installed
- [ ] Virtual environment created
- [ ] Dependencies installed (`pip install -r requirements.txt`)
- [ ] `.env` file created from `.env.example`
- [ ] API keys added to `.env`
- [ ] Streamlit running (`streamlit run app.py`)
- [ ] App opens at http://localhost:8501
- [ ] Can upload a PDF
- [ ] Can run a query

---

## 🔑 API Keys Needed

### Required
- **Google Gemini** (Free tier available)
  - Get: https://makersuite.google.com/app/apikey
  - Used for: Embeddings & synthesis

### Optional (System works without them)
- **Pinecone** (Free tier available)
  - Get: https://app.pinecone.io
  - Used for: Vector storage

- **Cohere** (Free tier available)
  - Get: https://dashboard.cohere.com
  - Used for: Result reranking

---

## 🆘 Quick Troubleshooting

### "API Keys Not Configured"
```bash
cp .env.example .env
# Edit .env with your API keys
streamlit run app.py
```

### "ModuleNotFoundError"
```bash
pip install -r requirements.txt --upgrade
```

### "Port 8501 already in use"
```bash
streamlit run app.py --server.port 8502
```

### "PDF upload fails"
- Check PDF is not corrupted
- Try a smaller PDF first
- Check `data/uploads/` folder exists

**More issues?** → See [TROUBLESHOOTING.md](TROUBLESHOOTING.md)

---

## 📞 Getting Help

1. **Setup Issues** → [SETUP_GUIDE.md](SETUP_GUIDE.md)
2. **API Key Issues** → [SECURITY_GUIDE.md](SECURITY_GUIDE.md)
3. **Errors/Bugs** → [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
4. **Deployment** → [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
5. **Commands** → [QUICK_REFERENCE.md](QUICK_REFERENCE.md)

---

## 🎓 Learning Path

### Beginner (30 minutes)
1. Read this file (5 min)
2. Read [README.md](README.md) (5 min)
3. Follow [SETUP_GUIDE.md](SETUP_GUIDE.md) (10 min)
4. Try uploading a PDF (10 min)

### Intermediate (1 hour)
1. Complete Beginner path
2. Read [QUICK_REFERENCE.md](QUICK_REFERENCE.md) (10 min)
3. Try different search types
4. Generate a report
5. Customize config.py

### Advanced (2+ hours)
1. Complete Intermediate path
2. Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
3. Read [SECURITY_GUIDE.md](SECURITY_GUIDE.md)
4. Review source code in `src/`
5. Deploy to cloud platform

---

## 🚀 Next Steps

### Option 1: Get Started Now
```bash
# 1. Setup
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt

# 2. Configure
cp .env.example .env
# Edit .env with your API keys

# 3. Run
streamlit run app.py
```

### Option 2: Learn More First
- Read [README.md](README.md) for overview
- Read [SETUP_GUIDE.md](SETUP_GUIDE.md) for details
- Then follow Option 1

### Option 3: Deploy to Cloud
- Read [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- Choose your platform
- Follow deployment steps

---

## 💡 Pro Tips

1. **Start Small**: Test with 1-2 PDFs first
2. **Check Logs**: Streamlit shows errors in terminal
3. **Restart Often**: Restart Streamlit after changing `.env`
4. **Read Docs**: Most issues are covered in documentation
5. **Monitor Usage**: Check API usage regularly

---

## 🎯 Success Criteria

You're ready when you can:
- ✅ Run `streamlit run app.py` without errors
- ✅ Upload a PDF successfully
- ✅ Enter a research question
- ✅ Get synthesis results
- ✅ Generate a report

---

## 📞 Support

- **Documentation**: See links above
- **API Issues**: Check provider status pages
- **Code Issues**: Review [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
- **Security**: Read [SECURITY_GUIDE.md](SECURITY_GUIDE.md)

---

## 🎉 You're All Set!

You now have everything you need to:
- ✅ Process multiple PDFs
- ✅ Search across documents
- ✅ Generate AI-powered insights
- ✅ Create research reports
- ✅ Deploy to production

**Happy researching!** 🚀

---

**Questions?** Check the relevant guide above or review [TROUBLESHOOTING.md](TROUBLESHOOTING.md)
