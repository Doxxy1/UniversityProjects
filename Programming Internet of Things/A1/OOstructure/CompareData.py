from sense_hat import SenseHat
from Database import DatabaseInfo
from NotificationSender import Sender
import sqlite3
import time
import sys
import json
import requests
import os
DB_NAME = "sensehat.db"


class Compare:
        def __init__(self):
                pass
                # Compare database data.
        def compareData(self):
                        with open('config.json', 'r') as f:
                                databaseData = json.load(f)
                        with sqlite3.connect(DB_NAME) as connection:
                                connection.row_factory = sqlite3.Row # Use this if you want to use column names over indexes.
                                cursor = connection.cursor()
                                cursor.execute("SELECT timestamp, temperature, humidity FROM sensehat_data")
                                print("Database content:")
                                for row in cursor:                

                                        if databaseData['max_temperature'] > row["temperature"] > databaseData['min_temperature']: # do for humidity as well
                                                print("Good", row["temperature"])

                                        elif databaseData['max_humidity'] > row["humidity"] > databaseData['min_humidity']:
                                                print("Good", row["humidity"])
                                                
                                        elif databaseData['max_humidity'] < row["humidity"] < databaseData['min_humidity']:
                                                print("Bad", row["humidity"])
                                                if(DatabaseInfo().getDate() == False):
                                                        DatabaseInfo().logDate()
                                                        Sender().send_notification_via_pushbullet("Humidity is outside of the Configured range", "From Raspberry Pi")               
                                        else:
                                                print("Bad", row["temperature"])
                                                if(DatabaseInfo().getDate() == False):
                                                        DatabaseInfo().logDate()
                                                        Sender().send_notification_via_pushbullet("Temperature is outside of the Configured range", "From Raspberry Pi")
                        cursor.close()
                        connection.close() 

