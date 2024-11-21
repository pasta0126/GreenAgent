from sentence_transformers import SentenceTransformer
import faiss
import numpy as np
import os

faiss_index_path = os.path.join("..", "api", "data", "incidencias_index.faiss")

model = SentenceTransformer('all-MiniLM-L6-v2')

index = faiss.read_index(faiss_index_path)

query = "Error al iniciar sesión"
query_embedding = model.encode([query])[0].astype('float32')

distances, indices = index.search(np.array([query_embedding]), k=3)

print("Resultados más similares:")
for idx, dist in zip(indices[0], distances[0]):
    print(f"Índice: {idx}, Distancia: {dist}")
