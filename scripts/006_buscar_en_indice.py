from sentence_transformers import SentenceTransformer
import faiss
import numpy as np

# Cargar modelo de embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Cargar ndice FAISS
index = faiss.read_index("incidencias_index.faiss")

# Consulta
query = "Error al iniciar sesin"
query_embedding = model.encode([query])[0].astype('float32')  # Generar embedding

# Buscar en el ndice
distances, indices = index.search(np.array([query_embedding]), k=3)

# Mostrar resultados
print("Resultados ms similares:")
for idx, dist in zip(indices[0], distances[0]):
    print(f"ndice: {idx}, Distancia: {dist}")

