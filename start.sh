#!/bin/sh

# Save the container environment so cron jobs can see CALENDAR_URLS etc.
export -p > /app/.env

# Render the landing page from the template using the environment variables.
python3 render-landingpage.py

crond -f -l 8 > /dev/stdout &

cd /app && python3 merge-ical.py && python3 -m http.server "$PORT" > /dev/stdout 2> /dev/stderr
