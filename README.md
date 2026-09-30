# TC Libcal Calendar Merge App

This docker app runs a small python script to host a merged ical feed of both the Trinity College Parents and Staff Libcal Calendars. The script is run evey hour by cron to regenerate the tc-calendar from Libcal. It is designed to be used as the source for importing into outlook for staff.

## Building the Image

To build the image locally, run:

```docker build -t ical-merge .```

## Running the image

The script defaults to port `8080`. This can be adjusted in the run command.

```docker run -d -p 8080:8080 --name ical-merge ical-merge:latest```
## Environment variables

| Variable | Default | Description |
| --- | --- | --- |
| `CALENDAR_URLS` | *(required)* | Comma-separated list of iCal URLs to merge. |
| `OUTPUT_FILENAME` | `combined_calendar.ics` | File name of the merged calendar served by the app. |
| `PAGE_TITLE` | `Merged Calendar` | Title and heading shown on the landing page. |
| `PORT` | `8080` | Port the web server listens on inside the container. |

Example:

```docker run -d -p 8080:8080 -e CALENDAR_URLS="https://example.com/a.ics,https://example.com/b.ics" -e PAGE_TITLE="Staff Calendar" -e OUTPUT_FILENAME="staff-calendar.ics" --name ical-merge ical-merge:latest```
