FROM python:3.7-slim

COPY requirements.txt /

RUN python3 -m pip install -r requirements.txt

COPY . /similarity-service

WORKDIR /similarity-service

ADD . /similarity-service

EXPOSE 5000

CMD ["python3", "main.py"]