Google Calendar and Telegram Integration
========================================

## Prerequisite
* Python 2.6 or graeter
* The [pip](https://arm.fedoraproject.org/) package management tool
* A Google account with Google Calendar enabled
* Linux

## Testbed
* Server (Running the bot)

## Quick Start
#### Turn on the Google Calendar API
* Click on Google Calendar API [Enable the google calendar API](https://developers.google.com/calendar/quickstart/python)
* Select + Create a new project
* Download the configuration file
* Move the downloaded file to your working directory and ensure it is named credentials.json
* Install the google client library
    ```
    $ pip install --upgrade google-api-python-client oauth2client
    ```
    
#### Telegram API configuration
Token and chat id (group chat) needed
* Chat BotFather in Telegram (default friend)
* See documentation [BotFather command](https://core.telegram.org/bots#6-botfather)
* get chat id target and your bot token

#### Install and Run
```
$ git clone https://github.com/mhmmdhilmi/telegramBot
$ cd telegramBot
$ chmod +x telegramBot/quickstart.py
$ python quickstart.py
```
before running quictstart.py you need to change the token, chat id, and path of directory on the script.

## TO DO
Activate Cron job to run script automatically