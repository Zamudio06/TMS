# Dockerfile

# Usamos una imagen oficial de Python 3
FROM python:3.7-slim

# Establecer el directorio de trabajo en el contenedor
WORKDIR /usr/src/app

# Copiar los archivos de requerimientos
COPY requirements.txt ./

RUN pip install --upgrade pip

RUN pip install gunicorn

# Instalar las dependencias
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación
COPY . .

# Agregar argumentos que serán pasados durante la construcción
ARG DJANGO_SECRET_KEY
ARG DB_NAME
ARG DB_USER
ARG DB_PASSWORD
ARG DB_HOST
ARG DB_PORT

# Establecer variables de entorno con los valores de los argumentos
ENV DJANGO_SECRET_KEY=${DJANGO_SECRET_KEY}
ENV DB_NAME=${DB_NAME}
ENV DB_USER=${DB_USER}
ENV DB_PASSWORD=${DB_PASSWORD}
ENV DB_HOST=${DB_HOST}
ENV DB_PORT=${DB_PORT}

# Exponer el puerto 8000 para la aplicación
EXPOSE 8000

# Comando por defecto para ejecutar la aplicación usando gunicorn
CMD ["gunicorn", "--bind", "0.0.0.0:8000", "project.TMS.wsgi:application"]
