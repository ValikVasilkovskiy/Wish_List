FROM python:3.6
MAINTAINER Valik Vasilkovskiy valik.vasilkovskiy@gmail.coms

RUN apt update && apt install -y --no-install-recommends \
    python-dev \
    python-setuptools \
    default-libmysqlclient-dev

COPY . /project
WORKDIR /project

RUN pip install --upgrade pip==10.0.1
RUN pip install -r requirements.txt

EXPOSE 5000
