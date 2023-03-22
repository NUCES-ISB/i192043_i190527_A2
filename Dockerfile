<<<<<<< HEAD
FROM python:3.10-slim
EXPOSE 5000
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
=======
FROM python:3.10-slim-buster

WORKDIR /app

>>>>>>> 8dd4714fbcdc1e63077b22ba560c9000388d423a
COPY requirements.txt .
RUN python -m pip install -r requirements.txt
WORKDIR /app
COPY . /app
RUN adduser -u 5678 --disabled-password --gecos "" appuser && chown -R appuser /app
USER appuser
CMD [ "python", "app.py" ]