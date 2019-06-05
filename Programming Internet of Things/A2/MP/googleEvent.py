from __future__ import print_function
from datetime import datetime
from datetime import timedelta
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = "https://www.googleapis.com/auth/calendar"
store = file.Storage("token.json")
creds = store.get()
if(not creds or creds.invalid):
    flow = client.flow_from_clientsecrets("credentials.json", SCOPES)
    creds = tools.run_flow(flow, store)
service = build("calendar", "v3", http=creds.authorize(Http()))
class googleE:

    def __init__(self):
        pass
        
    def insert(self, username, bookTitle, email, eventID):
        date = datetime.now()
        bDate = (date + timedelta(days = 0)).strftime("%Y-%m-%d")
        rDate = (date + timedelta(days = 7)).strftime("%Y-%m-%d")
        time_start = "{}T06:00:00+10:00".format(bDate)
        time_end = "{}T07:00:00+10:00".format(rDate)
        description = '{} borrowed {}. Please return by: {}'.format(username, bookTitle, time_end)
            
        event = {
            "id": eventID,
            "summary": "Book Borrowed",
            "location": "The Library",
            "description": description,
            "start": {
                "dateTime": time_start,
                "timeZone": "Australia/Melbourne",
            },
            "end": {
                "dateTime": time_end,
                "timeZone": "Australia/Melbourne",
            },
            "attendees": [
                { "email": email },

            ],
            "reminders": {
                "useDefault": False,
                "overrides": [
                    { "method": "email", "minutes": 5 },
                    { "method": "popup", "minutes": 10 },
                ],
            }
        }

        event = service.events().insert(calendarId = 'primary', body = event).execute()
        print("An event has been created with your return date of: {}".format(time_end))

    def removeEvent(self, eventID):
        service.events().delete(calendarId= 'primary', eventId= eventID[0]).execute()
    
    def calendarList(self):
        page_token = None
        while True:
            calendar_list = service.calendarList().list(pageToken=page_token).execute()
            for calendar_list_entry in calendar_list['items']:
                print(calendar_list_entry['summary'])
            page_token = calendar_list.get('nextPageToken')
            if not page_token:
                break
