# Green Agent

## **1. Estructura General del Proyecto**

- **Base de Datos Relacional (MariaDB)**:
  - Contiene incidencias almacenadas con campos como descripcin, resolucin, etc.
  - Es el punto de partida para generar los datos que alimentan el sistema de bsqueda basado en IA.

- **API (FastAPI)**:
  - Acta como una capa intermedia entre la base de datos y la interfaz web.
  - Proporciona un endpoint `/search` que recibe consultas en lenguaje natural y devuelve resultados relevantes.

- **IA Implementada (FAISS + SentenceTransformers)**:
  - Usa un modelo de lenguaje preentrenado (`sentence-transformers`) para convertir texto (descripciones de problemas) en **vectores**.
  - Estos vectores se indexan en **FAISS**, una biblioteca optimizada para bsquedas rpidas de similitud.

- **Interfaz Web (Streamlit)**:
  - Proporciona una interfaz sencilla para que los usuarios interacten con el sistema.
  - Permite ingresar descripciones de problemas y visualizar resultados relevantes.

---

## **2. Cmo Funciona la IA?**

La IA implementada utiliza tcnicas de **aprendizaje automtico** y **procesamiento de lenguaje natural (NLP)** para encontrar incidencias similares. Aqu tienes los pasos clave:

### **2.1. Generacin de Embeddings**

- **Embeddings** son representaciones numricas de texto que capturan su significado.
- Usamos el modelo `sentence-transformers` para convertir cada descripcin de la base de datos en un vector de alta dimensin.

### **2.2. Indexacin con FAISS**

- **FAISS** (Facebook AI Similarity Search) permite buscar rpidamente vectores similares en una base de datos grande.
- Todos los embeddings generados se almacenan en un ndice FAISS. Esto hace que las bsquedas sean rpidas incluso si hay millones de registros.

### **2.3. Proceso de Bsqueda**

- Cuando un usuario ingresa una consulta, esta tambin se convierte en un embedding usando el mismo modelo.
- FAISS busca en el ndice los vectores ms cercanos (similares) al embedding de la consulta.
- Los resultados (descripciones y resoluciones) se devuelven como respuesta.

---

## **3. Qu Sucede si la Base de Datos Crece?**

Cuando la base de datos crece, surgen dos retos principales:

1. **Actualizar el ndice FAISS con Nuevos Registros**:
   - FAISS no detecta automticamente los cambios en la base de datos.
   - Necesitas regenerar los embeddings para los nuevos registros y aadirlos al ndice.

2. **Escalabilidad**:
   - Si la base de datos crece mucho, el ndice FAISS puede volverse demasiado grande para caber en memoria.

---

## **4. Cmo Actualizar el ndice FAISS?**

Para integrar nuevos registros en el ndice FAISS:

1. **Detectar Cambios en la Base de Datos**:
   - Implementa un proceso que detecte registros nuevos o actualizados (por ejemplo, usando un campo `updated_at` en la base de datos).

2. **Generar Nuevos Embeddings**:
   - Solo calcula embeddings para los registros nuevos o modificados:

     ```python
     new_embeddings = model.encode(new_descriptions)
     ```

3. **Aadir Embeddings al ndice FAISS**:
   - Aade los nuevos vectores al ndice:

     ```python
     faiss_index.add(new_embeddings)
     ```

4. **Guardar el ndice Actualizado**:
   - Guarda el ndice actualizado en disco:

     ```python
     faiss.write_index(faiss_index, "incidencias_index.faiss")
     ```

---

## **5. Automatizacin**

Puedes automatizar el proceso de actualizacin del ndice usando un script programado. Aqu tienes cmo hacerlo:

1. **Escribir un Script de Actualizacin**:
   - Un script Python que detecte nuevos registros, genere embeddings y actualice el ndice.

2. **Programar el Script con Cron o Similar**:

   - En macOS/Linux, usa `cron` para ejecutar el script peridicamente:

     ```bash
     crontab -e
     ```

     Aade una lnea para ejecutar el script, por ejemplo, cada hora:

     ```bash
     0 * * * * /path/to/venv/bin/python /path/to/update_index.py
     ```

3. **Alternativa en Produccin: RabbitMQ o Kafka**:
   - Si necesitas actualizaciones en tiempo real, usa un sistema de mensajera como RabbitMQ para procesar los cambios en cuanto ocurren.

---

## **6. Escalabilidad**

Para manejar un crecimiento significativo en la base de datos:

1. **Dividir el ndice**:
   - Divide el ndice FAISS en varias partes (shards) y usa un sistema distribuido.

2. **Almacenamiento Hbrido**:
   - Usa un sistema hbrido como FAISS + Annoy o ElasticSearch para manejar ndices grandes que no caben en memoria.

3. **Optimizar el Modelo**:
   - Usa un modelo ms ligero para reducir el tamao de los embeddings.

---

## **7. Puntos Clave del Proyecto**

- **Ventajas**:
  - Responde consultas en lenguaje natural de forma rpida.
  - Escalable y extensible.

- **Limitaciones Actuales**:
  - La actualizacin del ndice no es automtica.
  - Si el ndice crece demasiado, puede ser necesario escalar el sistema.

- **Pasos Futuros**:
  - Agregar autenticacin y seguridad a la API.
  - Desplegar en Docker para facilitar el mantenimiento.
  - Implementar una solucin distribuida si el ndice FAISS crece ms all de los lmites de memoria.

---

## Levantar servicios

   ./run_services.sh

## Detener servicios

   ./stop_services.sh
