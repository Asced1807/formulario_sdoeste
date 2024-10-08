# Usar una imagen base de Python
FROM python:3.10-slim

# Establecer el directorio de trabajo
WORKDIR /code

# Instalar dependencias del sistema si son necesarias
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        gcc \
        python3-dev \
        libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar solo los requerimientos primero
COPY requerimientos.txt .

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requerimientos.txt

# Copiar el resto de la aplicación
COPY ./app ./app

# El EXPOSE no es necesario en Railway, pero lo mantenemos por documentación
EXPOSE 8000

# Variable de entorno para el puerto
ENV PORT=8000

# Comando para ejecutar la aplicación (corregido para usar el módulo app)
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "${PORT}"]
