import numpy as np
import json
import os

json_path = os.path.join("..", "api", "data", "incidencias_with_embeddings.json")

with open(json_path, "r") as file:
    data = json.load(file)

print(f"Total de registros: {len(data)}")
print(f"Primer embedding: {np.array(data[0]['embedding'])}")
