#!/bin/bash

echo "Deteniendo servicios de Green Agent..."

streamlit_pid=$(ps aux | grep streamlit | grep -v grep | awk '{print $2}')
if [ -n "$streamlit_pid" ]; then
    echo "Deteniendo Streamlit (PID: $streamlit_pid)..."
    kill -9 $streamlit_pid
    echo "Streamlit detenido."
else
    echo "Streamlit no está corriendo."
fi

uvicorn_pid=$(ps aux | grep uvicorn | grep -v grep | awk '{print $2}')
if [ -n "$uvicorn_pid" ]; then
    echo "Deteniendo Uvicorn (PID: $uvicorn_pid)..."
    kill -9 $uvicorn_pid
    echo "Uvicorn detenido."
else
    echo "Uvicorn no está corriendo."
fi

echo "Todos los servicios detenidos."
