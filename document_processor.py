import os
import json
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

try:
    from PyPDF2 import PdfReader
except ImportError:
    try:
        from pypdf import PdfReader
    except ImportError:
        PdfReader = None

try:
    from langchain_text_splitters import RecursiveCharacterTextSplitter
except ImportError:
    try:
        from langchain.text_splitter import RecursiveCharacterTextSplitter
    except ImportError:
        RecursiveCharacterTextSplitter = None

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200
HIERARCHICAL_CHUNK_SIZE = 3000
UPLOAD_FOLDER = "data/uploads"

class DocumentProcessor:
    def __init__(self):
        if RecursiveCharacterTextSplitter is None:
            print("Warning: RecursiveCharacterTextSplitter not available, using simple splitting")
            self.chunk_splitter = None
            self.hierarchical_splitter = None
        else:
            self.chunk_splitter = RecursiveCharacterTextSplitter(
                chunk_size=CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                separators=["\n\n", "\n", " ", ""]
            )
            self.hierarchical_splitter = RecursiveCharacterTextSplitter(
                chunk_size=HIERARCHICAL_CHUNK_SIZE,
                chunk_overlap=CHUNK_OVERLAP,
                separators=["\n\n", "\n", " ", ""]
            )
        
        os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    def extract_pdf_metadata(self, pdf_path: str) -> Dict:
        """Extract metadata from PDF file"""
        try:
            if PdfReader is None:
                return {
                    "title": Path(pdf_path).stem,
                    "author": "Unknown",
                    "page_count": 0,
                    "file_size": os.path.getsize(pdf_path),
                    "upload_date": datetime.now().isoformat(),
                    "error": "PyPDF2 not available"
                }
            
            with open(pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                metadata = pdf_reader.metadata or {}
                
                return {
                    "title": metadata.get("/Title", Path(pdf_path).stem),
                    "author": metadata.get("/Author", "Unknown"),
                    "creation_date": metadata.get("/CreationDate", "Unknown"),
                    "page_count": len(pdf_reader.pages),
                    "file_size": os.path.getsize(pdf_path),
                    "upload_date": datetime.now().isoformat()
                }
        except Exception as e:
            return {
                "title": Path(pdf_path).stem,
                "author": "Unknown",
                "page_count": 0,
                "file_size": os.path.getsize(pdf_path),
                "upload_date": datetime.now().isoformat(),
                "error": str(e)
            }

    def extract_text_from_pdf(self, pdf_path: str) -> Tuple[str, List[int]]:
        """Extract text and page numbers from PDF"""
        text = ""
        page_numbers = []
        
        try:
            if PdfReader is None:
                return text, page_numbers
            
            with open(pdf_path, 'rb') as file:
                pdf_reader = PdfReader(file)
                for page_num, page in enumerate(pdf_reader.pages, 1):
                    try:
                        page_text = page.extract_text()
                        text += f"\n--- Page {page_num} ---\n{page_text}"
                        page_numbers.append(page_num)
                    except:
                        pass
        except Exception as e:
            print(f"Error extracting text from {pdf_path}: {e}")
        
        return text, page_numbers

    def _simple_split(self, text: str, chunk_size: int) -> List[str]:
        """Simple text splitting fallback"""
        chunks = []
        for i in range(0, len(text), chunk_size):
            chunks.append(text[i:i + chunk_size])
        return chunks

    def create_chunks_with_metadata(self, text: str, doc_name: str, 
                                   page_numbers: List[int]) -> List[Dict]:
        """Create chunks with document metadata"""
        if self.chunk_splitter:
            chunks = self.chunk_splitter.split_text(text)
        else:
            chunks = self._simple_split(text, CHUNK_SIZE)
        
        chunk_list = []
        for i, chunk in enumerate(chunks):
            page_num = self._estimate_page_number(text, chunk, page_numbers)
            
            chunk_list.append({
                "content": chunk,
                "document": doc_name,
                "chunk_id": i,
                "page": page_num,
                "metadata": {
                    "doc_name": doc_name,
                    "chunk_index": i,
                    "page_number": page_num,
                    "chunk_size": len(chunk)
                }
            })
        
        return chunk_list

    def create_hierarchical_chunks(self, text: str, doc_name: str) -> List[Dict]:
        """Create hierarchical chunks for document-level summaries"""
        if self.hierarchical_splitter:
            chunks = self.hierarchical_splitter.split_text(text)
        else:
            chunks = self._simple_split(text, HIERARCHICAL_CHUNK_SIZE)
        
        chunk_list = []
        for i, chunk in enumerate(chunks):
            chunk_list.append({
                "content": chunk,
                "document": doc_name,
                "chunk_id": f"hierarchical_{i}",
                "level": "document",
                "metadata": {
                    "doc_name": doc_name,
                    "chunk_index": i,
                    "chunk_type": "hierarchical"
                }
            })
        
        return chunk_list

    def process_pdf_collection(self, pdf_paths: List[str]) -> Dict:
        """Process multiple PDFs and return structured data"""
        collection_data = {
            "documents": [],
            "chunks": [],
            "hierarchical_chunks": [],
            "processing_date": datetime.now().isoformat(),
            "total_documents": len(pdf_paths),
            "total_chunks": 0
        }
        
        for pdf_path in pdf_paths:
            print(f"Processing: {pdf_path}")
            
            metadata = self.extract_pdf_metadata(pdf_path)
            doc_name = metadata["title"]
            
            text, page_numbers = self.extract_text_from_pdf(pdf_path)
            
            if text:
                chunks = self.create_chunks_with_metadata(text, doc_name, page_numbers)
                hierarchical_chunks = self.create_hierarchical_chunks(text, doc_name)
            else:
                chunks = []
                hierarchical_chunks = []
            
            collection_data["documents"].append({
                "name": doc_name,
                "metadata": metadata,
                "chunk_count": len(chunks),
                "hierarchical_chunk_count": len(hierarchical_chunks)
            })
            
            collection_data["chunks"].extend(chunks)
            collection_data["hierarchical_chunks"].extend(hierarchical_chunks)
            collection_data["total_chunks"] += len(chunks)
        
        return collection_data

    def _estimate_page_number(self, full_text: str, chunk: str, 
                             page_numbers: List[int]) -> int:
        """Estimate page number for a chunk"""
        try:
            position = full_text.find(chunk)
            if position == -1:
                return page_numbers[0] if page_numbers else 1
            
            page_count = full_text[:position].count("--- Page")
            return page_numbers[page_count] if page_count < len(page_numbers) else page_numbers[-1]
        except:
            return page_numbers[0] if page_numbers else 1

    def save_collection_metadata(self, collection_data: Dict, output_path: str):
        """Save collection metadata to JSON"""
        with open(output_path, 'w') as f:
            json.dump(collection_data, f, indent=2)
