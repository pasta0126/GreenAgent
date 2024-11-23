#!/bin/bash

API_DIR="/Users/pasta0126/docker/GreenAgent"
WEB_DIR="/Users/pasta0126/docker/GreenAgent/web"

source "$API_DIR/venv/bin/activate"

cd "$API_DIR"
uvicorn api.main:app --host 0.0.0.0 --port 8000 --reload &

cd "$WEB_DIR"
streamlit run app.py --server.port 8501 &

