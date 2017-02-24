FROM python:3.6
ENV PYTHONUNBUFFERED 1
ADD . /var/www
WORKDIR /var/www
RUN pip3 install -r requirements.txt
