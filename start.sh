#!/bin/sh

crond -f -l 8 > /dev/stdout &

cd /app && python3 -m http.server 8080 > /dev/stdout 2> /dev/stderr