FROM python:alpine

WORKDIR /app

COPY ./app /app

RUN pip install flask

RUN pip install jinja2

CMD ["python", "index.py"]