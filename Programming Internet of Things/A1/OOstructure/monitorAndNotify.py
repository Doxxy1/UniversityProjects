from sense_hat import SenseHat
import sqlite3
import time
import sys
import json
import requests
import os
from Readings import getReadings
from CompareData import Compare
from Database import DatabaseInfo
# Main function.
def main():
    while True:
        DatabaseInfo().createDatabase()
        getReadings().getSenseHatData()
        Compare().compareData()
        time.sleep(60) #change this to 60 after testing
        
#create deeamon processes to start on pi boot and to restart when script finishes 

# Execute program.
if __name__ == "__main__":
    main()
