from typing import List, Dict
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer

class RAGHandler:
    def __init__(self, debug=True):
        self.debug = debug
        self.model = SentenceTransformer('all-MiniLM-L6-v2')
        self.dimension = 384
        self.index = faiss.IndexFlatL2(self.dimension)
        self.passages = []
        self.book_metadata = []

    def add_book_content(self, book_title: str, content: str):
        passages = self._split_into_passages(content)
        embeddings = self.model.encode(passages)
        
        # Add to FAISS index
        self.index.add(np.array(embeddings).astype('float32'))
        
        # Store passages and metadata
        start_idx = len(self.passages)
        self.passages.extend(passages)
        self.book_metadata.extend([{"book_title": book_title, "index": i} 
                                 for i in range(start_idx, start_idx + len(passages))])

    def retrieve_relevant_passages(self, query: str, k: int = 3) -> List[str]:
        query_embedding = self.model.encode([query])[0].reshape(1, -1).astype('float32')
        if self.index.ntotal == 0:
            return []
            
        distances, indices = self.index.search(query_embedding, k)
        
        if self.debug:
            print("\nRAG Debug Info:")
            print(f"Query: {query}")
            print(f"Found {len(indices[0])} relevant passages")
            print(f"Similarity scores: {distances[0]}")
            
        return [self.passages[i] for i in indices[0]]

    def _split_into_passages(self, text: str, max_length: int = 512) -> List[str]:
        sentences = text.split('.')
        passages = []
        current_passage = ""
        
        for sentence in sentences:
            if len(current_passage) + len(sentence) < max_length:
                current_passage += sentence + "."
            else:
                passages.append(current_passage)
                current_passage = sentence + "."
                
        if current_passage:
            passages.append(current_passage)
            
        return passages