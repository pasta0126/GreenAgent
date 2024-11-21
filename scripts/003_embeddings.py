from sentence_transformers import SentenceTransformer
import numpy as np
import pandas as pd
import os

csv_path = os.path.join("..", "api", "data", "incidencias.csv")

data = pd.read_csv(csv_path)

model = SentenceTransformer('all-MiniLM-L6-v2')

data['embedding'] = data['descripcion'].apply(lambda x: model.encode(x).tolist())

json_path = os.path.join("..", "api", "data", "incidencias_with_embeddings.json")

data.to_json(json_path, orient="records")

print(f"Embeddings generados y guardados en {json_path}")
