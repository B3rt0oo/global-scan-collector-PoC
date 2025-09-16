FROM python:3.11-slim

WORKDIR /app
COPY ids_collector.py .

RUN pip install --no-cache-dir fastapi uvicorn psycopg2-binary pydantic

EXPOSE 8000

CMD ["uvicorn", "ids_collector:app", "--host", "0.0.0.0", "--port", "8000"]

