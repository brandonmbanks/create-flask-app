FROM python:3.6
ENV PYTHONUNBUFFERED 1
ADD . /src/
WORKDIR /src
RUN pip3 install -r requirements.txt
