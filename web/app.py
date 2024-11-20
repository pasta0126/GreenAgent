import streamlit as st
import requests

API_URL = "http://192.168.1.20:8000"  # URL de tu API

st.title("Green Agent - Bsqueda de Incidencias")
st.write("Introduce una descripcin para buscar soluciones basadas en incidencias previas.")

query = st.text_input("Descripcin del problema:")
top_k = st.slider("Nmero de resultados", 1, 10, 3)

if st.button("Buscar"):
    if query:
        response = requests.post(f"{API_URL}/search", json={"query": query, "top_k": top_k})
        if response.status_code == 200:
            results = response.json().get("results", [])
            if results:
                st.write("### Resultados Encontrados:")
                for result in results:
                    st.write(f"**Descripcin**: {result['descripcion']}")
                    st.write(f"**Resolucin**: {result['resolucion'] or 'No disponible'}")
                    st.write("---")
            else:
                st.warning("No se encontraron resultados.")
        else:
            st.error("Error al conectar con la API.")
    else:
        st.warning("Por favor, introduce una descripcin del problema.")

