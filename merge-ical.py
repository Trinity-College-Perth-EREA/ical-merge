from mergecal import merge_calendars
from icalendar import Calendar
import requests
import os

calendar_urls = os.getenv("CALENDAR_URLS", "")
if not calendar_urls:
    raise ValueError("CALENDAR_URLS environment variable is not set or empty.")
calendar_urls = calendar_urls.split(",")

output_filename = os.getenv("OUTPUT_FILENAME", "combined_calendar.ics")

def fetch_calendar(url):
    response = requests.get(url)
    response.raise_for_status()
    return Calendar.from_ical(response.content)



def main():
    calendar_list = [fetch_calendar(url) for url in calendar_urls]

    try:
        merged_calendar: Calendar = merge_calendars(
            calendar_list)
        with open(output_filename, "wb") as f:
            f.write(merged_calendar.to_ical())
        print(f"Merged calendar saved as {output_filename}")
    except Exception as e:
        print(f"Error merging calendars: {e}")


if __name__ == "__main__":
    main()