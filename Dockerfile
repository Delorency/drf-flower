FROM python:3.11.2

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

CMD python ./app/manage.py runserver 0.0.0.0:8000