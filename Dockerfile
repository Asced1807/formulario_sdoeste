# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de tu aplicación al contenedor
COPY . /app

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requerimientos.txt

# Exponer el puerto de la aplicación (cambiar si es necesario)
EXPOSE 8000

# comando para correr nuestra aplciacion de fastapi 
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
