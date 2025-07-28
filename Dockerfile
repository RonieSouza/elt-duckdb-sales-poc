FROM python:3.13-slim

# Evita que o Python grave arquivos .pyc
ENV PYTHONDONTWRITEBYTECODE=1

# Evita buffering do Python (útil para logs)
ENV PYTHONUNBUFFERED=1

RUN pip install --no-cache-dir --upgrade pip duckdb

WORKDIR /app

CMD ["python", "run_scripts.py"]