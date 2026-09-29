FROM dhi.io/python:3-alpine-dev

COPY . /app

WORKDIR /app
    
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY start.sh /

RUN chmod +x /start.sh
 
RUN mkdir -p /var/spool/cron/crontabs \
    && crontab /app/crontab.txt

RUN python merge-ical.py

ENTRYPOINT ["/bin/sh", "/start.sh"]

