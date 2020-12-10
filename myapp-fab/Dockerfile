FROM ubuntu:latest

RUN apt-get update -y
RUN apt-get install -y python3 python3-pip python3-dev

COPY ./requirements.txt /requirements.txt

WORKDIR /

RUN pip3 install -r requirements.txt

COPY ./myapp /

ENTRYPOINT [ "gunicorn" ]

CMD [ "--log-file=-", "--workers=2", "--bind=0.0.0.0:5500", "wsgi:app" ]