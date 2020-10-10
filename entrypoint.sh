#!/bin/bash

cd /code

if [ -z "$SIMPLE_FLASK_PORT" ]
then
  export SIMPLE_FLASK_PORT=80
fi

/usr/local/bin/flask run -h 0.0.0.0 -p ${SIMPLE_FLASK_PORT}
