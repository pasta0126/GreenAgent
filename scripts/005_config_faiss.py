import faiss
import numpy as np
import json

# Cargar embeddings
with open("incidencias_with_embeddings.json", "r") as file:
    data = json.load(file)

# Crear ndice FAISS
dimension = len(data[0]['embedding'])
index = faiss.IndexFlatL2(dimension)

# Convertir embeddings a matriz NumPy
embeddings = np.array([item['embedding'] for item in data]).astype('float32')

# Agregar embeddings al ndice
index.add(embeddings)

# Guardar ndice
faiss.write_index(index, "incidencias_index.faiss")

print("ndice FAISS creado y guardado.")

