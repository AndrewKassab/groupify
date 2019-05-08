#!/bin/sh

docker/wait-for database:25569 -t 60 -- echo Connected!

cd app

host=${HOST:-localhost}
port=${PORT:-5000}
export FLASK_APP=flask_start.py
flask run -h $host -p $port
