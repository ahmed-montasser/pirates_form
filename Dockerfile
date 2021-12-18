# pull official base image
FROM python:3.10-alpine

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install psycopg2 dependencies & openssl
RUN apk update \
    && apk add --no-cache postgresql-dev gcc python3-dev musl-dev openssl

# install dockerize
ENV DOCKERIZE_VERSION v0.6.1
RUN wget https://github.com/jwilder/dockerize/releases/download/$DOCKERIZE_VERSION/dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && tar -C /usr/local/bin -xzvf dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz \
    && rm dockerize-alpine-linux-amd64-$DOCKERIZE_VERSION.tar.gz

# set working directory
WORKDIR /usr/src/app

# copy requirements.txt into working directory 
COPY requirements.txt ./

# install dependencies
RUN pip install -r requirements.txt

# copy project
COPY . .

# expose port
EXPOSE 8000

# run app
CMD dockerize -wait tcp://db:5432 -timeout 60m python app/manage.py migrate && python app/manage.py collectstatic && python app/manage.py runserver 0.0.0.0:8000
