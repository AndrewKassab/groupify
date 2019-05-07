#!/bin/sh

docker/wait-for database:25569 -t 60 -- echo Connected!

python app/app.py
