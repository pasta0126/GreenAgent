from sqlalchemy import create_engine
import pandas as pd

# Configuracin de la conexin
engine = create_engine("mysql+pymysql://testuser:testpassword@localhost:3333/testdb")

# Consulta para obtener los datos
query = "SELECT id, descripcion, resolucion FROM incidencias"

# Leer datos
data = pd.read_sql(query, engine)

# Guardar los datos en un archivo CSV para referencia
data.to_csv("incidencias.csv", index=False)

print("Datos extrados y guardados en incidencias.csv")

