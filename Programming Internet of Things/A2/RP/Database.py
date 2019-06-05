import sqlite3
import time
import sys
import json
import os
DB_NAME = "customers.db"


class DatabaseInfo:
        def __init__(self):
                pass
                # Create the Database
        def createDatabase(self):

                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("CREATE TABLE IF NOT EXISTS customer_data(username VARCHAR, password VARCHAR,firstName VARCHAR, lastName VARCHAR, email VARCHAR)")  
                cursor.close()
                connection.close()

#add a customer to the datebase with all information
        def addCustomer(self,username,hashedPassword,vfirstName,vlastName,email):

                with sqlite3.connect(DB_NAME) as connection:
                      cursor = connection.cursor()
                      cursor.execute("INSERT INTO customer_data(username, password, firstName, lastName, email) VALUES (?, ? , ? , ? , ?)",
                        (username, hashedPassword,vfirstName, vlastName,email))
                cursor.close()
                connection.close()
#Login function used to return an exisiting user so that they can be logged in
        def login(self,loginUser):
                with sqlite3.connect(DB_NAME) as connection:
                      cursor = connection.cursor()
                      cursor.execute("Select username, password, email FROM customer_data WHERE username =?",(loginUser,))
                      userID = cursor.fetchone()   
                cursor.close()
                connection.close()
                return userID
              