import pandas as pd
from sqlalchemy import create_engine

# Conexión a la base de datos MySQL
db_user = 'root'
db_password = '30102001'
db_host = 'localhost'
db_name = 'db2_practica1_g18'

engine = create_engine(f'mysql+mysqlconnector://{db_user}:{db_password}@{db_host}/{db_name}')

log_habitacion_df = pd.read_csv('./CSV/LogHabitacion.csv')
log_habitacion_df.to_sql('log_habitacion', con=engine, if_exists='append', index=False)

# log_actividad_df = pd.read_csv('./CSV/LogActividades2.csv')
# log_actividad_df.to_sql('log_actividad', con=engine, if_exists='append', index=False)

# paciente_df = pd.read_csv('./CSV/Pacientes.csv', sep=';')
# paciente_df.to_sql('paciente', con=engine, if_exists='append', index=False)

# habitacion_df = pd.read_csv('./CSV/Habitaciones.csv')
# habitacion_df.to_sql('habitacion', con=engine, if_exists='append', index=False)
                        
print("Datos cargados exitosamente.")
