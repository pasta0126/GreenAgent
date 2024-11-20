import pymysql
from faker import Faker
import random
from datetime import datetime, timedelta

connection = pymysql.connect(
    host='localhost',
    user='testuser',
    password='testpassword',
    database='testdb',
    port=3333
)

faker = Faker()

areas = ['IT', 'Finanzas', 'Recursos Humanos', 'Logstica']
criticidades = ['Baja', 'Media', 'Alta']

cursor = connection.cursor()

for _ in range(500):
    usuario = faker.name()
    area = random.choice(areas)
    criticidad = random.choice(criticidades)
    descripcion = faker.sentence()
    fecha_incidencia = faker.date_time_this_year()
    resolucion = faker.sentence() if random.random() > 0.5 else None
    fecha_resolucion = (fecha_incidencia + timedelta(days=random.randint(1, 30))) if resolucion else None
    comentarios = faker.text() if random.random() > 0.3 else None

    query = """
    INSERT INTO incidencias (usuario, area, criticidad, descripcion, fecha_incidencia, resolucion, fecha_resolucion, comentarios)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (usuario, area, criticidad, descripcion, fecha_incidencia, resolucion, fecha_resolucion, comentarios))

connection.commit()
cursor.close()
connection.close()

