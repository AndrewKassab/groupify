#!/bin/sh

wait-for database:25569 -t 60 -- echo Connected!

host=${HOST:-localhost}
port=${PORT:-5000}
export FLASK_APP=flask_start.py

exec flask run -h $host -p $port
