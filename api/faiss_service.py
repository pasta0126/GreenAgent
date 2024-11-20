import faiss
import numpy as np
import json
from sentence_transformers import SentenceTransformer

class FaissService:
    def __init__(self, index_path, data_path):
        self.index = faiss.read_index(index_path)
        with open(data_path, "r") as f:
            self.data = json.load(f)
        self.model = SentenceTransformer("all-MiniLM-L6-v2")

    def search_similar(self, query, top_k):
        query_embedding = self.model.encode([query])[0].astype("float32")
        distances, indices = self.index.search(np.array([query_embedding]), k=top_k)
        results = [self.data[idx] for idx in indices[0]]
        return results

