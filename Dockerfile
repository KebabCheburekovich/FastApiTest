FROM python:3.11

ENV PYTHONUNBUFFERED 1

WORKDIR /app

EXPOSE 8000

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . /app

CMD ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
