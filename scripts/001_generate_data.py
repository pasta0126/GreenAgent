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

faker = Faker('es_ES')

areas = [
    'Minería Espacial', 'Colonización Planetaria', 'Gestión de Oxígeno',
    'Mantenimiento de Naves', 'Agricultura en Marte', 'Control de Radiación',
    'Terraformación', 'Defensa Planetaria', 'Exploración Intergaláctica',
    'Logística Espacial', 'Tecnología Cuántica', 'Bioingeniería Espacial',
    'Robótica Avanzada', 'Simulación Gravitatoria', 'Sostenibilidad Lunar'
]

criticidades = ['Muy Baja', 'Baja', 'Media', 'Alta', 'Muy Alta', 'Crítica']

descripciones = [
    f"Fallo detectado en el sistema de {area.lower()} debido a sobrecarga térmica."
    f"Error crítico en la calibración de sensores en {area.lower()}."
    f"Interferencia electromagnética afecta la operación en {area.lower()}."
    f"Fallo en la conexión de datos con el módulo de {area.lower()}."
    f"Anomalía detectada en los sistemas de comunicación de {area.lower()}."
    f"Desviación en los parámetros de presión en el sistema de {area.lower()}."
    f"Bloqueo en la unidad de control principal de {area.lower()}."
    f"Corrupción de datos en los registros del sistema de {area.lower()}."
    f"Temperaturas fuera del rango permitido en el área de {area.lower()}."
    f"Pérdida de energía en el módulo de soporte de {area.lower()}."
    f"Fuga detectada en los conductos de refrigeración de {area.lower()}."
    f"Retraso significativo en la sincronización de {area.lower()}."
    f"Error en la secuencia de arranque del sistema de {area.lower()}."
    f"Desalineación de componentes estructurales en {area.lower()}."
    f"Impacto inesperado afecta la estabilidad de {area.lower()}."
    f"Oscilaciones gravitatorias detectadas en el entorno de {area.lower()}."
    f"Incompatibilidad entre módulos de {area.lower()} tras actualización."
    f"Fallo en el suministro de oxígeno en la zona de {area.lower()}."
    f"Radiación cósmica afecta las operaciones en {area.lower()}."
    f"Error en la transmisión de comandos al sistema de {area.lower()}."
    f"Aumento inesperado de la presión en el módulo de {area.lower()}."
    f"Desactivación involuntaria del sistema automatizado de {area.lower()}."
    f"Contaminación biológica detectada en el área de {area.lower()}."
    f"Fallo en el módulo de terraformación asociado a {area.lower()}."
    f"Inestabilidad del reactor de energía afecta {area.lower()}."
    f"Errores repetidos en los sensores de monitoreo de {area.lower()}."
    f"Interferencia de ondas gravitatorias en el sistema de {area.lower()}."
    f"Anomalía en la distribución de recursos para {area.lower()}."
    f"Mal funcionamiento en el sistema de soporte vital de {area.lower()}."
    f"Problemas de navegación afectan las operaciones en {area.lower()}."
    f"Inconsistencias detectadas en los datos de {area.lower()}."
    f"Fallo en el mecanismo de extracción de {area.lower()}."
    f"Despresurización parcial en el entorno de {area.lower()}."
    f"Problemas en la gestión de residuos en el módulo de {area.lower()}."
    f"Obstrucción en los sistemas de ventilación de {area.lower()}."
    f"Problemas de aislamiento térmico en la zona de {area.lower()}."
    f"Fallo crítico en los sistemas de propulsión asociados a {area.lower()}."
    f"Desgaste acelerado en componentes esenciales de {area.lower()}."
    f"Señales espurias detectadas en los sistemas de {area.lower()}."
    f"Errores en el software de control de {area.lower()}."
    f"Fallo en el protocolo de emergencia en {area.lower()}."
    f"Obstrucción de los conductos de oxígeno en el módulo de {area.lower()}."
    f"Sobrecalentamiento en los sistemas principales de {area.lower()}."
    f"Interrupción en el flujo de energía hacia {area.lower()}."
    f"Contaminación detectada en el área de cultivo de {area.lower()}."
    f"Error en la simulación de gravedad artificial en {area.lower()}."
    f"Desgaste en los sistemas de blindaje de {area.lower()}."
    f"Problemas en el mantenimiento de drones en {area.lower()}."
    f"Fallo en la transmisión de telemetría desde {area.lower()}."
    f"Anomalías en la gestión de almacenamiento en {area.lower()}."
    f"Malfuncionamiento en los mecanismos robóticos de {area.lower()}."
    f"Fallo en el sistema de anclaje en la estación de {area.lower()}."
    f"Desajuste en los controles de presión de {area.lower()}."
    f"Problemas de latencia en la red de comunicación de {area.lower()}."
    f"Radiación cósmica impacta el núcleo operativo de {area.lower()}."
    f"Interferencia magnética en los módulos críticos de {area.lower()}."
    f"Pérdida de conexión con la nave asignada a {area.lower()}."
    f"Problemas de calibración en los instrumentos de {area.lower()}."
    f"Errores recurrentes en el módulo de inteligencia artificial de {area.lower()}."
    f"Fallo en la compuerta de acceso del módulo de {area.lower()}."
    f"Aumento de vibraciones en los sistemas estructurales de {area.lower()}."
    f"Fuga de gas inerte en el entorno de {area.lower()}."
    f"Problemas de redundancia en los sistemas de respaldo de {area.lower()}."
    f"Desincronización en los relojes de misión en {area.lower()}."
    f"Impacto de micrometeoritos afecta la operatividad de {area.lower()}."
    f"Problemas en el despliegue de paneles solares en {area.lower()}."
    f"Oscilaciones de temperatura extrema en el módulo de {area.lower()}."
    f"Fallo en el ensamblaje de piezas críticas para {area.lower()}."
    f"Obstrucción en los sistemas de filtrado de aire en {area.lower()}."
    f"Error en la calibración del espectrómetro de {area.lower()}."
    f"Pérdida temporal de control sobre los mecanismos de {area.lower()}."
    f"Fallo en los sistemas de reciclaje en el módulo de {area.lower()}."
    f"Problemas en el sistema de inteligencia predictiva de {area.lower()}."
    f"Impacto inesperado de ondas de choque en {area.lower()}."
    f"Error crítico en los sistemas de almacenamiento de datos en {area.lower()}."
    f"Mal funcionamiento en los protocolos de terraformación de {area.lower()}."
    f"Fallo en el suministro de energía al área de {area.lower()}."
    f"Problemas en la gestión de tráfico interplanetario para {area.lower()}."
    f"Daños estructurales en la estación principal de {area.lower()}."
    f"Sobrecalentamiento de componentes electrónicos en {area.lower()}."
    f"Fallo en los sistemas de monitoreo ambiental de {area.lower()}."
    f"Interferencia de partículas subatómicas afecta {area.lower()}."
    f"Problemas de actualización en los sistemas operativos de {area.lower()}."
    f"Fallo en la sincronización de flotas asignadas a {area.lower()}."
    f"Incompatibilidad de versiones en el software de {area.lower()}."
    f"Mal funcionamiento en los mecanismos de seguridad de {area.lower()}."
    f"Pérdida de señal en el sistema de radar para {area.lower()}."
    f"Errores en el control remoto de drones asignados a {area.lower()}."
    f"Problemas en la emisión de permisos de acceso en {area.lower()}."
    for area in areas
] * 10

resoluciones = [
    "Ajuste de parámetros térmicos realizados con éxito.",
    "Se reconfiguró el sistema para evitar interferencias.",
    "El módulo dañado fue reemplazado y validado.",
    "Se reemplazaron los conductos de refrigeración afectados.",
    "Reparación completa del sistema de control automatizado.",
    "Actualización de software implementada en los sistemas principales.",
    "Componentes desgastados fueron reemplazados por nuevas unidades.",
    "Se restableció la conexión de datos con el módulo afectado.",
    "Instalación de redundancia en los sistemas críticos completada.",
    "Se recalibraron los sensores de presión para normalizar las operaciones.",
    "El equipo técnico aplicó medidas para estabilizar el reactor.",
    "Se ajustaron los protocolos de comunicación en la red de control.",
    "El módulo afectado fue retirado y puesto en mantenimiento.",
    "Los parámetros de aislamiento térmico fueron optimizados.",
    "Se desplegó un equipo de drones para reparar el área dañada.",
    "El software de gestión fue reinstalado y probado con éxito.",
    "Módulo de energía restaurado tras identificar la causa raíz.",
    "Se repararon los daños en la compuerta de acceso.",
    "El sistema de monitoreo ambiental fue reseteado.",
    "Implementación de medidas para prevenir futuras fallas similares.",
    "Se aplicó un parche de seguridad en el sistema de control.",
    "Los niveles de oxígeno fueron normalizados manualmente.",
    "Se retiró la obstrucción en los sistemas de ventilación.",
    "La calibración del espectrómetro fue realizada con éxito.",
    "Se desplegó un protocolo de emergencia para estabilizar las operaciones.",
    "Reemplazo inmediato de paneles solares dañados.",
    "Se resolvió el error de software mediante un rollback de versión.",
    "El sistema de navegación fue recalibrado y testeado.",
    "Se ajustaron los niveles de presión en los conductos críticos.",
    "Reparación de sensores gravimétricos completada.",
    "Se instaló un nuevo sistema de anclaje para reforzar la estructura.",
    "Revisión exhaustiva del sistema de reciclaje realizada.",
    "Se eliminaron las partículas contaminantes en el área afectada.",
    "Reparación del módulo robótico realizada sin complicaciones.",
    "El fallo en el suministro de energía fue resuelto tras inspección.",
    "Se instalaron refuerzos en los sistemas estructurales.",
    "La interferencia electromagnética fue neutralizada con filtros avanzados.",
    "Se restableció la sincronización en los relojes de misión.",
    "El reactor de energía fue enfriado utilizando protocolos de emergencia.",
    "El equipo técnico aisló la sección afectada para evitar daños mayores.",
    "El módulo de terraformación fue recalibrado con parámetros óptimos.",
    "Se solucionó la despresurización en el módulo de trabajo.",
    "Se incrementaron las medidas de aislamiento contra radiación cósmica.",
    "El flujo de datos fue optimizado eliminando cuellos de botella.",
    "Se repararon los mecanismos de soporte vital afectados.",
    "El sistema de inteligencia artificial fue reentrenado con nuevos datos.",
    "Los problemas de redundancia fueron solucionados actualizando el hardware.",
    "Se implementó un nuevo protocolo de seguridad en la red.",
    "El sistema de control remoto fue restaurado tras un reseteo general.",
    "Los módulos incompatibles fueron actualizados para evitar conflictos.",
    "El equipo técnico eliminó las señales espurias detectadas.",
    "Se desplegaron refuerzos temporales en el área afectada.",
    "Los mecanismos de seguridad fueron reconfigurados con éxito.",
    "El fallo en el sistema de filtrado de aire fue resuelto.",
    "La energía fue redirigida a los sistemas críticos para estabilizar la nave.",
    "El error de sincronización fue solucionado tras una revisión de hardware.",
    "El módulo afectado fue despresurizado y puesto en cuarentena.",
    "Se repararon los mecanismos de propulsión dañados.",
    "El sistema de gestión de residuos fue optimizado para mayor eficiencia.",
    "Se actualizaron los protocolos de monitoreo ambiental.",
    "La contaminación biológica fue contenida mediante protocolos de limpieza.",
    "Se implementaron nuevas medidas de redundancia en los sistemas eléctricos.",
    "Se realizó un análisis de causa raíz para evitar futuras fallas.",
    "Los niveles de presión fueron estabilizados mediante ajustes manuales.",
    "El sistema de radar fue recalibrado tras identificar interferencias.",
    "Los datos corruptos fueron recuperados desde copias de seguridad.",
    "El fallo en los mecanismos robóticos fue solucionado tras mantenimiento.",
    "La sincronización de flotas fue restaurada manualmente.",
    "Se reemplazaron los cables afectados por desgaste.",
    "El sistema de terraformación fue puesto en modo seguro para revisión.",
    "Se rediseñaron los paneles de control para mayor estabilidad.",
    "El software de predicción fue actualizado con nuevos modelos.",
    "El módulo de minería fue ajustado para operar con eficiencia.",
    "Los sensores de radiación fueron recalibrados tras detectar anomalías.",
    "La obstrucción en los conductos fue eliminada y sellada.",
    "Se implementaron algoritmos mejorados en el sistema de inteligencia.",
    "El fallo en los protocolos de emergencia fue solucionado.",
    "Los sistemas de soporte vital fueron revisados y optimizados.",
    "Se instalaron nuevos filtros para reducir interferencias gravitatorias.",
    "El equipo técnico reforzó la estructura del módulo afectado.",
    "La temperatura de operación fue ajustada para evitar sobrecalentamiento.",
    "Se actualizaron los sistemas operativos con nuevas versiones seguras.",
    "Los sistemas de almacenamiento fueron optimizados para mayor capacidad.",
    "El daño por impacto de micrometeoritos fue reparado por drones.",
    "Los conductos de oxígeno fueron inspeccionados y reparados.",
    "El sistema de simulación gravitatoria fue ajustado para evitar oscilaciones.",
    "La fuga de gas fue contenida con medidas de emergencia.",
    "El software de análisis de datos fue mejorado con mayor precisión.",
    "Los daños estructurales fueron reparados por robots autónomos.",
    "El fallo en los protocolos de anclaje fue resuelto."
] * 10

comentarios = [
    "Se requiere revisión periódica del equipo afectado.",
    "El sistema se encuentra en estado de observación.",
    "El equipo técnico ha iniciado el análisis de la causa raíz.",
    "Se recomienda reforzar las medidas preventivas en esta área.",
    "La anomalía ha sido documentada para futuras investigaciones.",
    "Se notificó a los responsables del área para tomar acción inmediata.",
    "El problema será monitoreado durante las próximas 24 horas.",
    "Se están realizando pruebas adicionales para validar la solución propuesta.",
    "El equipo técnico ha solicitado piezas de reemplazo para la reparación.",
    "La situación está bajo control, pero se requieren más análisis.",
    "Se identificaron posibles factores que contribuyeron al problema.",
    "La operación fue restablecida, pero el sistema sigue en monitoreo.",
    "Se ha escalado el problema al equipo de ingeniería avanzada.",
    "El área afectada está siendo aislada para evitar daños colaterales.",
    "Se detectaron inconsistencias en los datos de monitoreo recientes.",
    "El incidente fue reportado al centro de comando para revisión adicional.",
    "Se inició una auditoría del sistema para identificar vulnerabilidades.",
    "El equipo de mantenimiento recomendó realizar una inspección profunda.",
    "La reparación ha sido temporal; se requiere una solución definitiva.",
    "Se están revisando los protocolos de emergencia para evitar futuras fallas.",
    "El equipo de supervisión recomendó implementar redundancia adicional.",
    "Se ha programado una revisión completa del módulo afectado.",
    "El sistema se está estabilizando, pero se requiere más tiempo para análisis.",
    "Los parámetros operativos han sido ajustados para evitar recaídas.",
    "Se solicitó una actualización del software de monitoreo.",
    "El impacto fue menor, pero las medidas preventivas serán reforzadas.",
    "Se registraron datos del evento para mejorar futuros diagnósticos.",
    "El equipo técnico reporta progresos en la solución del problema.",
    "Se está desarrollando un informe técnico para la alta dirección.",
    "La causa probable ha sido identificada, pero se requieren más pruebas.",
    "Se programaron simulaciones para validar los cambios realizados.",
    "El incidente será cerrado una vez se confirme la estabilidad del sistema.",
    "El módulo afectado estará fuera de servicio hasta nuevo aviso.",
    "Se detectaron patrones similares en otros módulos del mismo tipo.",
    "El problema parece ser intermitente; se monitoreará a largo plazo.",
    "Se implementaron medidas temporales para mantener la operatividad.",
    "El equipo de terraformación ha sido alertado sobre posibles impactos.",
    "Se están analizando los registros históricos para determinar el origen.",
    "El módulo será sometido a pruebas de estrés para verificar su integridad.",
    "El incidente fue clasificado como de baja prioridad tras evaluación inicial.",
    "Se envió una alerta a todas las áreas para prevenir problemas similares.",
    "El fallo se encuentra contenido, pero se requiere inspección detallada.",
    "Se ordenaron piezas críticas para garantizar la estabilidad futura.",
    "El sistema automatizado detectó fallas previas relacionadas con este problema.",
    "Se recomendó realizar mantenimiento preventivo en otros módulos.",
    "El incidente está siendo evaluado por expertos externos.",
    "El equipo de control está desarrollando nuevos protocolos de seguridad.",
    "Se iniciará un proyecto de mejora para mitigar problemas similares.",
    "El análisis preliminar indica que fue un fallo humano.",
    "El incidente fue documentado como parte de las lecciones aprendidas.",
    "El problema está siendo discutido en el comité técnico interdepartamental.",
    "El equipo de soporte está proporcionando asistencia remota al módulo afectado.",
    "Se reportaron anomalías similares en módulos cercanos.",
    "El sistema ha sido actualizado para incluir nuevas medidas de seguridad.",
    "Se registraron mejoras tras los ajustes iniciales realizados por el equipo.",
    "Se solicitó una inspección independiente para garantizar la solución.",
    "El equipo de operaciones recomendó aumentar los intervalos de revisión.",
    "Se estableció un plan de acción para abordar problemas potenciales.",
    "El problema fue menor, pero se revisarán los procedimientos estándar.",
    "Se emitió un comunicado interno sobre la resolución del incidente.",
    "El equipo técnico está evaluando medidas adicionales de mitigación.",
    "El incidente será cerrado tras una última revisión programada.",
    "Se detectaron pequeños daños colaterales que serán abordados a continuación.",
    "El análisis muestra que el fallo se debió a condiciones externas extremas.",
    "El área afectada será monitoreada durante los próximos días.",
    "El fallo está relacionado con una actualización reciente del sistema.",
    "El equipo de robótica recomendó ajustar los parámetros de operación.",
    "Se confirmó que el problema no afecta a otras operaciones.",
    "El módulo afectado volverá a estar operativo tras pruebas adicionales.",
    "El equipo ha sugerido mejorar el entrenamiento del personal para evitar errores.",
    "Se está desarrollando una solución permanente para problemas recurrentes.",
    "El incidente fue resuelto parcialmente, pero persisten algunos riesgos.",
    "El análisis indica que el problema fue causado por vibraciones externas.",
    "Se notificó al equipo de soporte avanzado para asistencia adicional.",
    "El incidente fue reportado como cerrado tras verificaciones exhaustivas.",
    "Se inició un monitoreo extendido para prevenir problemas futuros.",
    "El análisis final será enviado al comité de revisión técnica.",
    "Se detectaron fallas menores que podrían evolucionar a problemas graves.",
    "Se están desarrollando herramientas específicas para abordar este tipo de fallos.",
    "El sistema ha mostrado mejoras tras el ajuste de parámetros clave.",
    "El equipo de ingeniería ha sugerido reforzar los sistemas afectados.",
    "Se confirmó que el fallo no fue causado por un ataque externo.",
    "Se asignó un equipo adicional para acelerar la resolución del problema.",
    "El incidente fue clasificado como crítico tras una evaluación más detallada.",
    "Se está preparando un protocolo específico para manejar esta situación.",
    "El equipo técnico reportó que el módulo está listo para volver a operar.",
    "Se sugirió realizar simulacros para mejorar la respuesta ante este tipo de eventos.",
    "El fallo fue contenido rápidamente, minimizando el impacto general.",
    "Se solicitó una evaluación del equipo de terraformación para verificar compatibilidad.",
    "El análisis final confirmó que el problema fue causado por desgaste natural.",
    "El incidente está en espera de aprobación para cerrar oficialmente.",
    "Se desarrollaron mejoras temporales mientras se planifica una solución a largo plazo.",
    "El problema se solucionó, pero se planean revisiones regulares para evitar su recurrencia.",
    "El módulo afectado estará en observación intensiva durante los próximos días.",
    "Se identificaron posibles riesgos asociados que serán investigados a fondo."
] * 10

cursor = connection.cursor()

for _ in range(5000):
    nombre = faker.first_name()
    apellido = faker.last_name()
    usuario = (nombre[:3] + apellido[:3]).lower()

    area = random.choice(areas)
    criticidad = random.choice(criticidades)
    descripcion = random.choice(descripciones)
    fecha_incidencia = faker.date_time_between(start_date="-2y", end_date="now")
    resolucion = random.choice(resoluciones) if random.random() > 0.5 else None
    fecha_resolucion = (fecha_incidencia + timedelta(days=random.randint(1, 30))) if resolucion else None

    comentarios_finales = random.choice(comentarios) if random.random() > 0.3 else None

    query = """
    INSERT INTO incidencias (usuario, area, criticidad, descripcion, fecha_incidencia, resolucion, fecha_resolucion, comentarios)
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
    """
    cursor.execute(query, (usuario, area, criticidad, descripcion, fecha_incidencia, resolucion, fecha_resolucion, comentarios_finales))

connection.commit()
cursor.close()
connection.close()
