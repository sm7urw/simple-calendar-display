import os
import json
from datetime import datetime, timezone
from icalevents.icalevents import events

# Konfiguration
ICAL_URL = "https://calendar.google.com/calendar/ical/154d3b9d01134c0d6a73e1e0aefefdf8d168c5cb2d10fc430544064bbbbe2d5f@group.calendar.google.com/public/basic.ics"
OUTPUT_FILE = "event.js"

def fetch_next_event():
    try:
        now = datetime.now(timezone.utc)
        # Hämtar händelser för de närmaste 30 dagarna
        es = events(url=ICAL_URL, start=now)
        
        if not es:
            save_json({"error": "Inga kommande aktiviteter"})
            return

        # Sortera händelserna så att den som är närmast i tiden kommer först
        es.sort(key=lambda x: x.start)
        next_event = es[0]

        # Formatera datan snyggt (och strunta i plats/location)
        event_data = {
            "title": next_event.summary if next_event.summary else "Utan titel",
            "start": next_event.start.isoformat(),
            "end": next_event.end.isoformat(),
            "all_day": next_event.all_day,
            "desc": next_event.description if next_event.description else ""
        }
        
        save_json(event_data)
        print(f"Uppdaterad! Nästa aktivitet: {event_data['title']}")

    except Exception as e:
        print(f"Fel vid hämtning: {e}")
        # Om filen inte finns alls, skapa en felstatus, annars behåller vi förra fungerande filen
        if not os.path.exists(OUTPUT_FILE):
            save_json({"error": "Kunde inte hämta kalender"})

def save_json(data):
    with open(OUTPUT_FILE, "w", encoding="utf-8") as f:
        f.write("var calendarData = " + json.dumps(data, ensure_ascii=False, indent=2) + ";")

if __name__ == "__main__":
    fetch_next_event()
