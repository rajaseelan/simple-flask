# simple-flask
simple flask example  

Simple flask example.  
Listens on Port 80 (default) or environment variable SIMPLE_FLASK_PORT  
Returns hostname or environment variable SIMPLE_FLASK_HOSTNAME  
Returns current time on server in epoch.      


## How to launch

`docker run -d -e SIMPLE_FLASK_PORT=8080 -e SIMPLE_FLASK_MESSAGE='hello worlds' -p 8080:8080 simple-flask:v0.0.1`

## Environment Variables
Env | Purporse
--- | ---
SIMPLE_FLASK_PORT | flask listening port
SIMPLE_FLASK_MESSAGE | the custom message to display
SIMPLE_FLASK_HOSTNAME | the hostname value displayed by the app
