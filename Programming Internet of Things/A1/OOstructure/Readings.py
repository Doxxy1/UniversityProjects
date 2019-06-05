from sense_hat import SenseHat
from Database import DatabaseInfo
import sqlite3
import time
import sys
import json
import requests
import os
DB_NAME = "sensehat.db"

class getReadings:
    def __init__(self):
        pass
        # Get data from SenseHat sensor.
    def getSenseHatData(self):
        sense = SenseHat()
        temperature = sense.get_temperature()
        humidity = sense.get_humidity()

        if temperature and humidity is not None:
                temperature = round(temperature, 2)
                humidity = round(humidity, 2)
                DatabaseInfo().logData(temperature,humidity)
