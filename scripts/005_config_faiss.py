import faiss
import numpy as np
import json
import os

json_path = os.path.join("..", "api", "data", "incidencias_with_embeddings.json")

faiss_index_path = os.path.join("..", "api", "data", "incidencias_index.faiss")

with open(json_path, "r") as file:
    data = json.load(file)

dimension = len(data[0]['embedding'])
index = faiss.IndexFlatL2(dimension)

embeddings = np.array([item['embedding'] for item in data]).astype('float32')

index.add(embeddings)

faiss.write_index(index, faiss_index_path)

print(f"Índice FAISS creado y guardado en {faiss_index_path}.")
