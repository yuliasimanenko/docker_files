FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN apk update \
    && apk add postgresql-dev gcc python3-dev musl-dev

RUN pip install --trusted-host pypi.python.org -r requirements.txt

EXPOSE 80

CMD ["python", "app.py"]