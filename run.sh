#/bin/bash

echo "Starting authentication server..."
node ./authserver/authorization_code/app.js & 
echo "Starting app..."
cd client
npm start 
