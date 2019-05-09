#!/bin/sh

wait-for postgres:5432 -t 60

rake db:create db:migrate

echo "Migrated database"

trap goodbye 1 2 3 6 15
goodbye() {
  echo "Goodbye!"
  exit 1
}

# mark that the process is completed
counter=0
while true; do
  nc -lv 25569
  counter=$((counter+1))
  echo "Received status check (#$counter)"
done
