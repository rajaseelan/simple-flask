# simple-flask
simple flask example  

Simple flask example.  
Listens on Port 80 (default) or environment variable SIMPLE_FLASK_PORT  
Returns hostname or environment variable SIMPLE_FLASK_HOSTNAME  
Returns current time on server in epoch.      


## How to launch

`docker run -e SIMPLE_FLASK_PORT=8080 simple-flask:v0.0.1`