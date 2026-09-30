FROM dhi.io/python:3-alpine-dev

ENV PAGE_TITLE="Merged Calendar" \
    OUTPUT_FILENAME="combined_calendar.ics" \
    PORT=8080

COPY . /app

COPY index.html /templates/index.html

WORKDIR /app
    
RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8080

COPY start.sh /

RUN chmod +x /start.sh
 
RUN mkdir -p /var/spool/cron/crontabs \
    && crontab /app/crontab.txt

ENTRYPOINT ["/bin/sh", "/start.sh"]

