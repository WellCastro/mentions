FROM ubuntu:latest
MAINTAINER Wellington Castro "wcesarc@gmail.com"

RUN apt-get update
RUN apt-get install -y python-pip

RUN mkdir -p /opt/deploy/tweets
RUN mkdir -p /var/log/tweets/webserver/
RUN mkdir -p /var/log/tweets/application/

COPY . /opt/deploy/tweets
RUN pip install -r /opt/deploy/tweets/requirements.txt

RUN find . -name \*.pyc -delete

WORKDIR /opt/deploy/tweets

EXPOSE 8001