# Create the docker container for the backend
FROM python:3.7.3-alpine3.9

COPY ./requirements.txt /app/backend/requirements.txt
WORKDIR /app/backend
RUN pip install -r requirements.txt
