from typing import List, Dict
import os

try:
    import cohere
except ImportError:
    cohere = None

try:
    from rank_bm25 import BM25Okapi
except ImportError:
    BM25Okapi = None

COHERE_API_KEY = os.getenv("COHERE_API_KEY")
RERANKER_MODEL = "rerank-english-v3.0"
TOP_K_RETRIEVAL = 20
TOP_K_RERANKED = 5
TOP_DOCUMENTS = 5
HYBRID_SEARCH_WEIGHT = 0.5

class RetrieverWithReranking:
    def __init__(self, vector_store, embeddings_manager):
        self.vector_store = vector_store
        self.embeddings_manager = embeddings_manager
        
        if cohere:
            try:
                self.cohere_client = cohere.ClientV2(api_key=COHERE_API_KEY)
            except:
                self.cohere_client = None
        else:
            self.cohere_client = None
        
        self.bm25_index = None
        self.documents_corpus = []

    def build_bm25_index(self, chunks: List[Dict]):
        """Build BM25 index for keyword search"""
        if BM25Okapi is None:
            return
        
        corpus = [chunk["content"].split() for chunk in chunks]
        self.bm25_index = BM25Okapi(corpus)
        self.documents_corpus = chunks

    def hybrid_search(self, query: str, top_k: int = TOP_K_RETRIEVAL) -> List[Dict]:
        """Perform hybrid search combining dense and sparse retrieval"""
        query_embedding = self.embeddings_manager.embed_query(query)
        
        dense_results = self.vector_store.search(query_embedding, top_k)
        
        sparse_results = []
        if self.bm25_index:
            query_tokens = query.split()
            bm25_scores = self.bm25_index.get_scores(query_tokens)
            
            top_indices = sorted(
                range(len(bm25_scores)),
                key=lambda i: bm25_scores[i],
                reverse=True
            )[:top_k]
            
            for idx in top_indices:
                if idx < len(self.documents_corpus):
                    chunk = self.documents_corpus[idx]
                    sparse_results.append({
                        "id": f"{chunk['document']}_{chunk['chunk_id']}",
                        "score": bm25_scores[idx],
                        "document": chunk["document"],
                        "content": chunk["content"],
                        "page": chunk.get("page", 0),
                        "chunk_id": chunk["chunk_id"]
                    })
        
        combined_results = self._combine_results(dense_results, sparse_results)
        return combined_results[:top_k]

    def _combine_results(self, dense: List[Dict], sparse: List[Dict]) -> List[Dict]:
        """Combine dense and sparse results with weighted scoring"""
        result_map = {}
        
        for i, result in enumerate(dense):
            normalized_score = (1 - (i / len(dense))) if dense else 0
            result_map[result["id"]] = {
                **result,
                "dense_score": normalized_score,
                "sparse_score": 0,
                "combined_score": normalized_score * HYBRID_SEARCH_WEIGHT
            }
        
        for i, result in enumerate(sparse):
            normalized_score = (1 - (i / len(sparse))) if sparse else 0
            if result["id"] in result_map:
                result_map[result["id"]]["sparse_score"] = normalized_score
                result_map[result["id"]]["combined_score"] = (
                    result_map[result["id"]]["dense_score"] * HYBRID_SEARCH_WEIGHT +
                    normalized_score * (1 - HYBRID_SEARCH_WEIGHT)
                )
            else:
                result_map[result["id"]] = {
                    **result,
                    "dense_score": 0,
                    "sparse_score": normalized_score,
                    "combined_score": normalized_score * (1 - HYBRID_SEARCH_WEIGHT)
                }
        
        sorted_results = sorted(
            result_map.values(),
            key=lambda x: x["combined_score"],
            reverse=True
        )
        
        return sorted_results

    def rerank_results(self, query: str, results: List[Dict], 
                      top_k: int = TOP_K_RERANKED) -> List[Dict]:
        """Rerank results using Cohere Rerank API"""
        if not results or self.cohere_client is None:
            return results[:top_k]
        
        try:
            documents = [result["content"] for result in results]
            
            reranked = self.cohere_client.rerank(
                model=RERANKER_MODEL,
                query=query,
                documents=documents,
                top_n=top_k
            )
            
            reranked_results = []
            for rank_result in reranked.results:
                original_result = results[rank_result.index]
                reranked_results.append({
                    **original_result,
                    "rerank_score": rank_result.relevance_score,
                    "rerank_position": rank_result.index
                })
            
            return reranked_results
        except Exception as e:
            print(f"Reranking error: {e}")
            return results[:top_k]

    def retrieve_with_reranking(self, query: str, 
                               top_k: int = TOP_K_RERANKED) -> List[Dict]:
        """Full retrieval pipeline with hybrid search and reranking"""
        hybrid_results = self.hybrid_search(query, TOP_K_RETRIEVAL)
        reranked_results = self.rerank_results(query, hybrid_results, top_k)
        return reranked_results

    def retrieve_from_documents(self, query: str, 
                               document_names: List[str] = None) -> Dict[str, List[Dict]]:
        """Retrieve top results from each document"""
        query_embedding = self.embeddings_manager.embed_query(query)
        
        results_by_doc = {}
        
        if document_names:
            for doc_name in document_names:
                doc_results = self.vector_store.search_by_document(
                    query_embedding, doc_name, TOP_DOCUMENTS
                )
                results_by_doc[doc_name] = doc_results
        
        return results_by_doc
