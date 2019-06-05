from sense_hat import SenseHat
import sqlite3
import time
import sys
import json
import requests
import os
DB_NAME = "sensehat.db"
ACCESS_TOKEN = "o.mBOI0UBaZ3sAc7D9PV5Q0xP07NXxb1Ue"


class Sender:
        
    def __init__(self):
        pass

  #Allowing pushbullet to work

    def send_notification_via_pushbullet(self, title, body):
        """ Sending notification via pushbullet.
                Args:
                title (str) : Title of text.
                body (str) : Body of text.
        """
        data = { "type": "note", "title": title, "body": body }

        response = requests.post("https://api.pushbullet.com/v2/pushes", data = json.dumps(data),
                headers = { "Authorization": "Bearer " + ACCESS_TOKEN, "Content-Type": "application/json" })

        if(response.status_code != 200):
                raise Exception()


