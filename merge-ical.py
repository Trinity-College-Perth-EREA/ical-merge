from mergecal import merge_calendars
from icalendar import Calendar
import requests

parent_calendar_url = "https://example.com"
staff_calendar_url = "https://example.com"

def fetch_calendar(url):
    response = requests.get(url)
    response.raise_for_status()
    return Calendar.from_ical(response.content)



def main():
    parent_calendar = fetch_calendar(parent_calendar_url)
    staff_calendar = fetch_calendar(staff_calendar_url)

    try:
        merged_calendar: Calendar = merge_calendars(
            [parent_calendar, staff_calendar])
        with open("tc-calendar.ics", "wb") as f:
            f.write(merged_calendar.to_ical())
        print("Merged calendar saved as tc-calendar.ics")
    except Exception as e:
        print(f"Error merging calendars: {e}")


if __name__ == "__main__":
    main()