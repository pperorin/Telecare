import datetime
from datetime import timedelta
import pickle
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request

SCOPES = ['https://www.googleapis.com/auth/calendar']

CREDENTIALS_FILE = 'credentials.json'


def get_calendar_service():
   creds = None
   # The file token.pickle stores the user's access and refresh tokens, and is
   # created automatically when the authorization flow completes for the first
   # time.
   if os.path.exists('token.pickle'):
       with open('token.pickle', 'rb') as token:
           creds = pickle.load(token)
   # If there are no (valid) credentials available, let the user log in.
   if not creds or not creds.valid:
       if creds and creds.expired and creds.refresh_token:
           creds.refresh(Request())
       else:
           flow = InstalledAppFlow.from_client_secrets_file(
               CREDENTIALS_FILE, SCOPES)
           creds = flow.run_local_server(port=0)

       # Save the credentials for the next run
       with open('token.pickle', 'wb') as token:
           pickle.dump(creds, token)

   service = build('calendar', 'v3', credentials=creds)
   return service


def create_event(startdate,starttime):
    service = get_calendar_service()

    start = str(startdate) + 'T' + str(starttime) + ':00:00+07:00'             #'2021-05-27T10:00:00+07:00'
    end = str(startdate) + 'T' + str(starttime+1) + ':00:00+07:00'
    event_result = service.events().insert(calendarId='nuttawat7171@gmail.com',
       body={
           "summary": 'TeleCare Meeting',
           "description": 'Our doctor is waiting for you!',
           "start": {"dateTime": start, "timeZone": 'Asia/Bangkok'},
           "end": {"dateTime": end, "timeZone": 'Asia/Bangkok'},
       }
    ).execute()

    print(event_result)
