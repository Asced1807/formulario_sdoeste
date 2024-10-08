import os

class Config:
    # Los valores de las variables de entorno ahora se establecen a partir de las variables que Railway proporciona
    DB_NAME = os.getenv('DB_NAME', 'railway')  # Nombre de la base de datos proporcionada por Railway
    DB_USER = os.getenv('DB_USER', 'postgres')  # Usuario de PostgreSQL proporcionado por Railway
    DB_PASSWORD = os.getenv('DB_PASSWORD', 'DDGbJwlwTxIfkogqoLakllnwAkmKyMgp')  # Contraseña de PostgreSQL proporcionada por Railway
    DB_HOST = os.getenv('DB_HOST', 'postgres-olkg.railway.internal')  # Host de PostgreSQL en Railway
    DB_PORT = os.getenv('DB_PORT', '5432')  # Puerto proporcionado por Railway

