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
        # Generar embedding de la consulta
        query_embedding = self.model.encode([query])[0].astype("float32")
        # Realizar la búsqueda
        distances, indices = self.index.search(np.array([query_embedding]), k=top_k)
        # Retornar resultados
        results = [
            {
                "descripcion": self.data[idx]["descripcion"],
                "resolucion": self.data[idx]["resolucion"],
                "comentarios": self.data[idx]["comentarios"],
                "distancia": dist,
            }
            for idx, dist in zip(indices[0], distances[0])
        ]
        return results
