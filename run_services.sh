#!/bin/bash

# Ruta al directorio de la API
API_DIR="/Users/pasta0126/docker/green-agent"
# Ruta al directorio de la Web
WEB_DIR="/Users/pasta0126/docker/green-agent/web"

# Activar entorno virtual
source "$API_DIR/venv/bin/activate"

# Iniciar API con Uvicorn
cd "$API_DIR"
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload &

# Iniciar la interfaz web con Streamlit
cd "$WEB_DIR"
streamlit run app.py --server.port 8501 &

