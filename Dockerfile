FROM python:3.6
MAINTAINER Valik Vasilkovskiy valik.vasilkovskiy@gmail.com
RUN apt-get update -y
RUN apt-get install -y --no-install-recommends python-setuptools python-dev
COPY . /project
WORKDIR /project

RUN pip install --upgrade pip==10.0.1
RUN pip install -r requirements.txt

EXPOSE 5000