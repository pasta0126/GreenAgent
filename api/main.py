from fastapi import FastAPI
from api.models import Query
from api.faiss_service import FaissService

app = FastAPI()

# Inicializar el servicio FAISS
faiss_service = FaissService(
    index_path="api/data/incidencias_index.faiss",
    data_path="api/data/incidencias_with_embeddings.json"
)

@app.get("/")
def read_root():
    return {"message": "API para bsqueda de incidencias"}

@app.post("/search")
def search(query: Query):
    results = faiss_service.search_similar(query.query, query.top_k)
    return {"results": results}

