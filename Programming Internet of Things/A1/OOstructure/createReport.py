from Database import DatabaseInfo
import sqlite3
import time
import datetime
import csv
import json
import os
import requests
import sys
import numpy as np
import pandas as pd

DB_NAME = "sensehat.db"

def collectData():

        with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('SELECT timestamp, MIN(temperature) as minTemp, MAX(temperature) as maxTemp, MIN(humidity) as minHumid, MAX(humidity) as maxHumid FROM sensehat_data GROUP BY date(timestamp)')
                results = cursor.fetchall()
                return results
        conn.close()

def generateCSVdata():

        with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('CREATE TABLE IF NOT EXISTS reportDB(date VARCHAR, minTempReport VARCHAR, maxTempReport VARCHAR, minHumidReport VARCHAR, maxHumidReport VARCHAR)')
                rows = cursor.fetchall()
                return rows
        cursor.close()
        conn.close()


def checkStatus():
        data = collectData()
        
        for rows in data:
                time = datetime.datetime.strptime(rows[0], '%Y-%m-%d %H:%M:%f').date()
                tempmintemp = float(rows[1])
                tempmaxtemp = float(rows[2])
                tempminhumid = float(rows[3])
                tempmaxhumid = float(rows[4])

                minimumTemp = temperatureCheck(tempmintemp)
                maximumTemp = temperatureCheck(tempmaxtemp)
                minimumHumid = humidityCheck(tempminhumid)
                maximumHumid = humidityCheck(tempmaxhumid)

                insertCSVData(time, minimumTemp, maximumTemp, minimumHumid, maximumHumid)

def insertCSVData(time, minimumTemp, maximumTemp, minimumHumid, maximumHumid):
        with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                cursor.execute('INSERT INTO reportDB (date, minTempReport, maxTempReport, minHumidReport, maxHumidReport) VALUES (?, ?, ?, ?, ?)',(time,minimumTemp, maximumTemp, minimumHumid, maximumHumid,))
        cursor.close()
        conn.close()

def compileCSV():
        conn = sqlite3.connect("sensehat.db")
        df = pd.read_sql_query("select * from reportDB group by date", conn)
        df.columns = ['Date', 'Status', 'Error','','']
        
        export_csv = df.to_csv ('report.csv', index = None, header=True)
        

def temperatureCheck(temp):
        data = jsonData()
#----------------------------------------------------------------------------
        jsonMinTemp = data['min_temperature']
        jsonMaxTemp = data['max_temperature']
#----------------------------------------------------------------------------
        temp = int(temp)

        if temp < jsonMinTemp:
                return("BAD, Reading is " + str(jsonMinTemp-temp) + " *C below the min temperature")

        elif temp > jsonMaxTemp:
                return("BAD, Reading is " + str(temp-jsonMaxTemp) + " *C above the max temperature")

        else:
                return('OK')
        

def humidityCheck(humid):

        data = jsonData()
#----------------------------------------------------------------------------
        jsonMinHum = data['min_humidity']
        jsonMaxHum = data['max_humidity']
#----------------------------------------------------------------------------
        humid = int(humid)
        differenceMin = humid - jsonMinHum
        differenceMax = humid - jsonMaxHum
#----------------------------------------------------------------------------
        if humid < jsonMinHum:
                return("BAD, Reading is " + str(differenceMin/jsonMinHum*100)  + " % below the min humidity")

        elif humid > jsonMaxHum:
                return("BAD, Reading is " + str(differenceMax/jsonMaxHum*100) + " % above the max humidity")

        else:
                return('OK')

def jsonData():
        with open('config.json', 'r') as f:
                databaseData = json.load(f)
        return databaseData

def main():
        collectData()
        generateCSVdata()
        checkStatus()
        compileCSV()

if __name__ == "__main__":
    main()
