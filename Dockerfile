# Dockerfile

# Usamos una imagen oficial de Python 3
FROM python:3.9-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar los archivos de requerimientos
COPY requirements.txt ./

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Agregar argumentos que serán pasados durante la construcción
ARG DB_USER
ARG DB_PASSWORD

# Establecer variables de entorno con los valores de los argumentos
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}

# Exponer el puerto 8000 para la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.TMS.wsgi:application"]
