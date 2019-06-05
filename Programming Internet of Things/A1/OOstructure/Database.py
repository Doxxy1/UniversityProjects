from sense_hat import SenseHat
import sqlite3
import time
import sys
import json
import requests
import os
DB_NAME = "sensehat.db"


class DatabaseInfo:
        def __init__(self):
                pass

                # Create the Database
        def createDatabase(self):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("CREATE TABLE IF NOT EXISTS sensehat_data(timestamp DATETIME, temperature NUMERIC, humidity NUMERIC)")  
                        #cursor.execute("CREATE TABLE IF NOT EXISTS report_data(date DATETIME, status TEXT, error TEXT)")
                        cursor.execute("CREATE TABLE IF NOT EXISTS notification_data(date DATETIME)")

                cursor.close()
                connection.close()

        #creates second table as if i added it to the above it would lock the database for some reason
        def addTable(self):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("CREATE TABLE IF NOT EXISTS report_data(date DATETIME, status TEXT, error TEXT)")
                cursor.close()
                connection.close()


        # Log data on database.
        def logData(self,temperature, humidity):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO sensehat_data (timestamp, temperature, humidity) VALUES (DATETIME('now', 'localtime'), ?, ?)",
                        (temperature, humidity))
                cursor.close()
                connection.close()

        def logDataReport(self, date, status, error):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO report_data (date, status,error) VALUES (?, ?, ?)",
                        (date,status,error))
                cursor.close()
                connection.close()
                
        def getDate(self):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        row = cursor.execute("select count(*) from notification_data where date = DATE(DATETIME('now', 'localtime'))").fetchone()
                cursor.close()
                connection.close()

                date = row[0] >= 1
                return date

        def logDate(self):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("INSERT INTO notification_data (date) values (DATE(DATETIME('now', 'localtime')))")
                cursor.close()    
                connection.close()