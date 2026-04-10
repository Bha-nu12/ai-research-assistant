# Multi-Document RAG Research Assistant - Prompt Guide

## System Overview

This is a production-ready Multi-Document RAG (Retrieval-Augmented Generation) system designed for researchers, lawyers, consultants, and analysts who need to extract insights from large document collections.

## Getting Started

### Step 1: Installation
```bash
cd PROJECT_28_RAG_ASSISTANT
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### Step 2: API Configuration
1. Create `.env` file from `.env.example`
2. Add your API keys:
   - OpenAI API key (for GPT-4o)
   - Pinecone API key and environment
   - Cohere API key

### Step 3: Launch Application
```bash
streamlit run app.py
```

The application will open at `http://localhost:8501`

---

## Core Workflows

### Workflow 1: Document Upload & Indexing

**Scenario**: You have 50+ research papers on AI ethics

**Steps**:
1. Prepare documents (PDF format)
2. Create ZIP archive or select individual PDFs
3. Click "Upload Documents" in sidebar
4. Select upload type (PDF Files or ZIP Archive)
5. Click "Process PDFs" or "Process ZIP"
6. Wait for processing (shows progress)
7. System automatically:
   - Extracts text and metadata
   - Creates hierarchical chunks
   - Generates embeddings
   - Indexes in Pinecone
   - Builds BM25 index

**Expected Output**:
- ✅ Processed X documents with Y chunks
- Collection metadata saved
- Ready for queries

---

### Workflow 2: Research Query with Synthesis

**Scenario**: "What are the main ethical concerns about AI across all these papers?"

**Steps**:
1. Enter research question in text area
2. Choose search type:
   - **Hybrid Search**: Combines semantic + keyword matching (recommended)
   - **Semantic Search**: Vector similarity only
   - **Per-Document**: Top results from each document
3. Adjust top_k slider (5-20 results)
4. Click "Search & Synthesize"
5. System performs:
   - Hybrid search across all documents
   - Cohere reranking for precision
   - Cross-document synthesis
   - Agreement detection
   - Contradiction identification

**Output Sections**:
- **Synthesis Results**: Comprehensive answer with citations
- **Agreements**: Points where documents align
- **Contradictions**: Conflicting claims between sources
- **Retrieved Chunks**: Source material (expandable)

---

### Workflow 3: Research Report Generation

**Scenario**: Create a publication-ready report on AI ethics

**Steps**:
1. Enter research question
2. Check "Generate Report" checkbox
3. Click "Search & Synthesize"
4. System generates:
   - Executive summary
   - Key findings
   - Cross-document analysis
   - Consensus areas
   - Disagreement areas
   - Research gaps
   - Conclusion
   - References
5. Click "Download Report" to get Word document

**Report Includes**:
- Structured sections
- Proper citations (Document, Page)
- Professional formatting
- Timestamp

---

## Advanced Prompts & Queries

### Academic Research
```
"Synthesize the main findings on climate change impacts from all documents. 
Identify which documents agree on key points and which contradict each other."
```

### Legal Research
```
"Compare the legal precedents cited across these case documents. 
What are the most frequently cited cases and what contradictions exist?"
```

### Competitive Intelligence
```
"What are the strategic differences between Company A and Company B 
based on their annual reports? Highlight areas of agreement and conflict."
```

### Policy Analysis
```
"Identify the consensus on healthcare policy across these government reports. 
What are the main areas of disagreement between agencies?"
```

### Literature Review
```
"Create a systematic review of research methodologies used in these papers. 
Which approaches are most common and which are unique?"
```

---

## Configuration Customization

### Adjust Retrieval Quality

**In `config.py`**:

```python
# For more precise results
TOP_K_RETRIEVAL = 30  # Retrieve more candidates
TOP_K_RERANKED = 5    # Keep top 5 after reranking

# For faster processing
TOP_K_RETRIEVAL = 10
TOP_K_RERANKED = 3

# Adjust hybrid search balance
HYBRID_SEARCH_WEIGHT = 0.5  # 0.5 = equal weight to dense + sparse
HYBRID_SEARCH_WEIGHT = 0.7  # 0.7 = favor semantic search
HYBRID_SEARCH_WEIGHT = 0.3  # 0.3 = favor keyword search
```

### Adjust Chunking Strategy

```python
# For detailed analysis (smaller chunks)
CHUNK_SIZE = 500
CHUNK_OVERLAP = 100

# For broader context (larger chunks)
CHUNK_SIZE = 2000
CHUNK_OVERLAP = 300
```

---

## Performance Optimization

### For Large Collections (100+ documents)

1. **Batch Processing**:
   - Upload in batches of 20-30 documents
   - Monitor Pinecone index size

2. **Retrieval Optimization**:
   - Use hybrid search (faster than semantic alone)
   - Reduce top_k if processing is slow
   - Enable reranking for precision

3. **Memory Management**:
   - Process documents in separate sessions
   - Clear cache between large uploads
   - Monitor system resources

### For Real-Time Queries

1. **Pre-index Documents**:
   - Upload and index all documents upfront
   - Queries will be instant

2. **Optimize Reranking**:
   - Reduce TOP_K_RETRIEVAL if reranking is slow
   - Use Cohere's faster reranker model

---

## Common Use Cases & Prompts

### 1. Systematic Literature Review
```
Query: "Summarize the research methodologies, sample sizes, and key findings 
across all papers. Identify methodological gaps."

Expected Output:
- Methodology comparison table
- Sample size ranges
- Key findings synthesis
- Identified gaps
```

### 2. Competitive Analysis
```
Query: "Compare the product features, pricing strategies, and market positioning 
of all companies in these documents."

Expected Output:
- Feature comparison
- Pricing analysis
- Market positioning
- Competitive advantages
```

### 3. Policy Synthesis
```
Query: "What are the recommended actions across all policy documents? 
Where do they agree and disagree?"

Expected Output:
- Recommended actions list
- Areas of consensus
- Areas of disagreement
- Implementation challenges
```

### 4. Risk Assessment
```
Query: "Identify all risks mentioned across these documents. 
Categorize by severity and frequency of mention."

Expected Output:
- Risk inventory
- Severity classification
- Frequency analysis
- Mitigation strategies
```

### 5. Trend Analysis
```
Query: "What are the emerging trends mentioned across these reports? 
How do different sources view these trends?"

Expected Output:
- Trend identification
- Source perspectives
- Consensus on trends
- Divergent views
```

---

## Troubleshooting Guide

### Issue: "API Key Error"
**Solution**:
1. Verify `.env` file exists in project root
2. Check API keys are correct (no extra spaces)
3. Verify API key permissions in respective dashboards
4. Restart Streamlit app

### Issue: "Slow Processing"
**Solution**:
1. Reduce CHUNK_SIZE in config.py
2. Increase BATCH_SIZE for embeddings
3. Use fewer documents initially
4. Check internet connection for API calls

### Issue: "Low Quality Results"
**Solution**:
1. Increase TOP_K_RETRIEVAL parameter
2. Adjust HYBRID_SEARCH_WEIGHT
3. Check document quality (OCR issues?)
4. Try more specific queries

### Issue: "Memory Error"
**Solution**:
1. Process documents in smaller batches
2. Reduce CHUNK_SIZE
3. Clear Pinecone index and restart
4. Use machine with more RAM

---

## Output Interpretation

### Synthesis Results
- **Citations**: (Document Name, Page Number) format
- **Accuracy**: Based on source documents only
- **Completeness**: Depends on retrieval quality

### Agreements
- **Strong Consensus**: Multiple documents cite same point
- **Weak Consensus**: Few documents mention point
- **Implicit Agreement**: Inferred from similar statements

### Contradictions
- **Direct Contradiction**: Explicit conflicting claims
- **Methodological Difference**: Different approaches to same topic
- **Temporal Difference**: Outdated vs. current information

---

## Best Practices

1. **Document Quality**
   - Use high-quality PDFs (avoid scanned images)
   - Ensure text is extractable
   - Remove corrupted files

2. **Query Formulation**
   - Be specific and clear
   - Use domain terminology
   - Ask one main question per query

3. **Result Validation**
   - Always verify citations
   - Check source documents
   - Validate contradictions

4. **Report Generation**
   - Review generated reports
   - Add additional context if needed
   - Cite original sources

---

## Advanced Features

### Document-Level Filtering
```python
# In retrieval.py
results = retriever.retrieve_from_documents(
    query="Your question",
    document_names=["Document1.pdf", "Document2.pdf"]
)
```

### Custom Metadata Filtering
```python
# Filter by date range, author, etc.
filter_dict = {"author": {"$eq": "Smith"}}
results = vector_store.search(query_embedding, filter=filter_dict)
```

### Batch Query Processing
```python
queries = [
    "Question 1?",
    "Question 2?",
    "Question 3?"
]

for query in queries:
    result = synthesis.synthesize_answer(query, retrieved_chunks)
    # Process result
```

---

## Integration Examples

### With External Systems
```python
# Export to database
import sqlite3
conn = sqlite3.connect('research.db')
# Store synthesis results

# Export to API
import requests
requests.post('https://api.example.com/research', json=synthesis_result)
```

### Batch Processing
```bash
# Process multiple query sets
python batch_processor.py --queries queries.json --output results.json
```

---

## Support & Resources

- **Documentation**: See README.md
- **Configuration**: Edit config.py
- **Troubleshooting**: See Troubleshooting Guide above
- **API Docs**:
  - OpenAI: https://platform.openai.com/docs
  - Pinecone: https://docs.pinecone.io
  - Cohere: https://docs.cohere.com

---

## Next Steps

1. ✅ Install dependencies
2. ✅ Configure API keys
3. ✅ Launch application
4. ✅ Upload test documents
5. ✅ Run sample queries
6. ✅ Generate reports
7. ✅ Customize configuration
8. ✅ Deploy to production

Happy researching! 🚀
