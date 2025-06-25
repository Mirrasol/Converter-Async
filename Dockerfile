FROM python:3.10-slim

RUN mkdir /fastapi_app

WORKDIR /fastapi_app

RUN pip install --upgrade pip

COPY requirements.txt /fastapi_app/

RUN pip install --no-cache-dir -r requirements.txt

COPY . /fastapi_app/

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]