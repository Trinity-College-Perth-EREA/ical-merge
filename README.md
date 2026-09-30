# iCal Merge App

This docker app runs a small python script to host a merged ical feed of provided calendars. The script is run every hour by cron to regenerate calendar feed, and can be subscribed to or downloaded in your preferred calendar.

## Quick start

Docker standalone:

```docker run -d -p 8080:8080 -e CALENDAR_URLS="<comma separated url list>" -e PAGE_TITLE="<html page title>" -e OUTPUT_FILENAME="<ics filename>" --name ical-merge ical-merge:latest```

Docker compose:
```
services:
  ical-merge:
    image: ghcr.io/trinity-college-perth-erea/ical-merge:latest
    container_name: ical-merge
    restart: unless-stopped
    ports:
      - "${PORT}:${PORT}"
    environment:
      CALENDAR_URLS: ${CALENDAR_URLS}
      OUTPUT_FILENAME: ${OUTPUT_FILENAME}
      PAGE_TITLE: ${PAGE_TITLE}
      PORT: ${PORT}
```

## Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `CALENDAR_URLS` | *(required)* | Comma-separated list of iCal URLs to merge. |
| `OUTPUT_FILENAME` | `combined_calendar.ics` | File name of the merged calendar served by the app. |
| `PAGE_TITLE` | `Merged Calendar` | Title and heading shown on the landing page. |
| `PORT` | `8080` | Port the web server listens on inside the container. |


## Building the Image

To build the image locally, run:

```docker build -t ical-merge .```
