FROM python:3.9.0-buster

ENV FLASK_APP=hello.py
WORKDIR /code
COPY . /code/

RUN pip install -r requirements.txt

ENTRYPOINT [ "/code/entrypoint.sh" ]