from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd

# Cargar datos
data = pd.read_csv("incidencias.csv")

# Modelo para embeddings
model = SentenceTransformer('all-MiniLM-L6-v2')

# Generar embeddings para descripciones y resoluciones
data['embedding'] = data['descripcion'].apply(lambda x: model.encode(x).tolist())

# Guardar embeddings en un archivo
data.to_json("incidencias_with_embeddings.json", orient="records")

print("Embeddings generados y guardados en incidencias_with_embeddings.json")

