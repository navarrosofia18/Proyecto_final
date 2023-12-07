FROM python:3.11

# Establece el directorio de trabajo
WORKDIR /app

COPY Buscador.py .

RUN pip install --no-cache-dir -r requirements.txt

ENV DISPLAY host.docker.internal:0

# Comando para ejecutar tu aplicación
CMD ["python", "Buscador.py"]
