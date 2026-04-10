from typing import List, Dict
import os
from dotenv import load_dotenv

load_dotenv()

try:
    import google.genai as genai
    GENAI_AVAILABLE = True
except ImportError:
    genai = None
    GENAI_AVAILABLE = False

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if GEMINI_API_KEY and GENAI_AVAILABLE:
    try:
        client = genai.Client(api_key=GEMINI_API_KEY)
        USE_GEMINI = True
    except Exception as e:
        print(f"Gemini not available: {e}")
        USE_GEMINI = False
        client = None
else:
    USE_GEMINI = False
    client = None

class CrossDocumentSynthesis:
    def __init__(self):
        self.use_gemini = USE_GEMINI
        self.client = client
        
        if self.use_gemini:
            print("[OK] Using Gemini for synthesis")
        else:
            print("[INFO] No LLM provider configured")

    def synthesize_answer(self, query: str, retrieved_chunks: List[Dict]) -> Dict:
        """Synthesize answer from multiple document chunks"""
        
        if not retrieved_chunks:
            return {
                "query": query,
                "synthesis": "No relevant documents found for your query.",
                "source_chunks": 0,
                "documents_cited": []
            }
        
        context_text = self._format_context(retrieved_chunks)
        
        prompt = f"""You are a research assistant analyzing multiple documents.

Research Question: {query}

Document Excerpts:
{context_text}

Task:
1. Answer the research question based ONLY on the provided excerpts
2. Cite every statement with (Document Name, Page Number)
3. Identify agreements between documents
4. Identify contradictions between documents
5. Note unique insights from individual documents

Format your response as:

ANSWER:
[Your synthesized answer with citations]

AGREEMENTS:
- [Point] (Doc1, Page X) & (Doc2, Page Y)

CONTRADICTIONS:
- [Conflict] (Doc1 vs Doc2)

UNIQUE INSIGHTS:
- [Insight] (Document Name, Page)

SOURCES:
- Document Name, Page Number"""
        
        if self.use_gemini and self.client:
            try:
                response = self.client.models.generate_content(
                    model='gemini-2.0-flash-thinking-exp-1219',
                    contents=prompt
                )
                synthesis_text = response.text if response and response.text else "Error: No response from Gemini"
            except Exception as e:
                synthesis_text = f"Error generating synthesis: {str(e)}"
        else:
            synthesis_text = "No LLM provider configured"
        
        return {
            "query": query,
            "synthesis": synthesis_text,
            "source_chunks": len(retrieved_chunks),
            "documents_cited": self._extract_documents(retrieved_chunks)
        }

    def detect_contradictions(self, query: str, retrieved_chunks: List[Dict]) -> List[str]:
        """Detect contradictions between documents"""
        
        if not retrieved_chunks:
            return []
        
        context_text = self._format_context(retrieved_chunks)
        
        prompt = f"""Analyze the following document excerpts for contradictions.

Research Question: {query}

Document Excerpts:
{context_text}

Identify any contradictions, conflicting claims, or differing perspectives between documents.
Return as a simple list of strings, one contradiction per line."""
        
        if self.use_gemini and self.client:
            try:
                response = self.client.models.generate_content(
                    model='gemini-2.0-flash-thinking-exp-1219',
                    contents=prompt
                )
                text = response.text if response and response.text else ""
                return [line.strip() for line in text.split('\n') if line.strip() and not line.startswith('*')]
            except Exception as e:
                return []
        else:
            return []

    def identify_agreements(self, query: str, retrieved_chunks: List[Dict]) -> List[str]:
        """Identify agreements between documents"""
        
        if not retrieved_chunks:
            return []
        
        context_text = self._format_context(retrieved_chunks)
        
        prompt = f"""Analyze the following document excerpts for agreements and consensus.

Research Question: {query}

Document Excerpts:
{context_text}

Identify points where multiple documents agree or support the same conclusion.
Return as a simple list of strings, one agreement per line."""
        
        if self.use_gemini and self.client:
            try:
                response = self.client.models.generate_content(
                    model='gemini-2.0-flash-thinking-exp-1219',
                    contents=prompt
                )
                text = response.text if response and response.text else ""
                return [line.strip() for line in text.split('\n') if line.strip() and not line.startswith('*')]
            except Exception as e:
                return []
        else:
            return []

    def _format_context(self, chunks: List[Dict]) -> str:
        """Format retrieved chunks as context"""
        context_parts = []
        
        for chunk in chunks:
            doc_name = chunk.get("document", "Unknown")
            page = chunk.get("page", "Unknown")
            content = chunk.get("content", "")
            
            context_parts.append(
                f"[{doc_name}, Page {page}]\n{content}\n"
            )
        
        return "\n---\n".join(context_parts)

    def _extract_documents(self, chunks: List[Dict]) -> List[str]:
        """Extract unique document names from chunks"""
        docs = set()
        for chunk in chunks:
            if "document" in chunk:
                docs.add(chunk["document"])
        return list(docs)
