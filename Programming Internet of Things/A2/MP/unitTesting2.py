import unittest
import MySQLdb
from prettytable import PrettyTable 
from prettytable import from_db_cursor

class testing2(unittest.TestCase):
    HOST = "35.201.3.196"
    USER = "root"
    PASSWORD = "password"
    DATABASE = "iotA2"

    def __init__(self, connection = None):
        if(connection == None):
            connection = MySQLdb.connect(testing2.HOST, testing2.USER, testing2.PASSWORD, testing2.DATABASE)
        self.connection = connection

    def close(self):
        self.connection.close()
    
    def __enter__(self):
        return self

    def __exit__(self, type, value, traceback):
        self.close()
    
    def testingID(self):
        for x in range(20):
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT * from Book WHERE BookID = %s", (id,))
                rows = cursor.fetchone()
                self.assertTrue(rows[0])
            return rows
            
#should produce 15 valid and 5 invalid 
 


if __name__ == '__main__':
    unittest.main()
