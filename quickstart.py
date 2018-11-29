#!/usr/bin/python
from __future__ import print_function
import datetime
from googleapiclient.discovery import build
from httplib2 import Http
from oauth2client import file, client, tools
import commands
import os
import requests 
from time import sleep 
import subprocess


#Write your param
token = '632930553:AAGpRuN7d_0bDMu3yxH2D3Sw-ofuROkVbmg'
chat_id = '-186086416'

#your bot path (ex : /home/visudo/bot_keprof/)
foo = "/home/visudo/bot_keprof/foo.txt"

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/calendar.readonly'
os.remove(foo.txt)

class BotHandler:
  def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot" + token + "/"

  def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

def write_file(text):
    fo = open(foo, "a")
    fo.write(text)
    fo.close()


def main():
    store = file.Storage('/home/visudo/bot_keprof/token.json')
    creds = store.get()
    if not creds or creds.invalid:
        flow = client.flow_from_clientsecrets('/home/visudo/bot_keprof/credentials.json', SCOPES)
        creds = tools.run_flow(flow, store)
    service = build('calendar', 'v3', http=creds.authorize(Http()))

    #Calling the Calendar API
    now = datetime.datetime.now().isoformat() + 'Z' # 'Z' indicates UTC time
    events_result = service.events().list(calendarId='ko1kpnsdepp79v6q0je21r2u3g@group.calendar.google.com', timeMin=now,
                                        maxResults=10, singleEvents=True,
                                        orderBy='startTime').execute()
    events = events_result.get('items', [])

    #preparing the message
    write_file('Agenda Departemen Keprofesian IMT Signum :)')
    write_file('\n')

    if not events:
        write_file('lagi gaada apa-apa ternyata')

    for event in events:
        start = event['start'].get('dateTime', event['start'].get('date'))
        fo = open(foo.txt, "a")
        write_file(start + ' ');
        write_file(event['summary'])
        fo.write('\n')

    kirim = BotHandler(token)
    msg = commands.getoutput('cat /home/visudo/bot_keprof/foo.txt')
    kirim.send_message(chat_id, msg)
    os.remove (foo);

if __name__ == '__main__':