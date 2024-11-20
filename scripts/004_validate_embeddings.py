import numpy as np
import json

# Cargar embeddings generados
with open("incidencias_with_embeddings.json", "r") as file:
    data = json.load(file)

# Verificar los embeddings
print(f"Total de registros: {len(data)}")
print(f"Primer embedding: {np.array(data[0]['embedding'])}")

