from sqlalchemy import create_engine
import pandas as pd
import os

engine = create_engine("mysql+pymysql://testuser:testpassword@localhost:3333/testdb")

query = "SELECT id, usuario, area, criticidad, descripcion, fecha_incidencia, resolucion, fecha_resolucion, comentarios FROM incidencias"

data = pd.read_sql(query, engine)

output_path = os.path.join("..", "api", "data", "incidencias.csv")

data.to_csv(output_path, index=False)

print(f"Datos extraídos y guardados en {output_path}")
