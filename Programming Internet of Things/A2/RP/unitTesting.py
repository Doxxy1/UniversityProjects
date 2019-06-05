import unittest
import sqlite3
import re
DB_NAME = "customers.db"

class testing(unittest.TestCase):
 

        #unit testing of the username 
        def test_UserName1(self):
            with sqlite3.connect(DB_NAME) as connection:
                      cursor = connection.cursor()
                      cursor.execute("Select username from customer_data")
                      userID = cursor.fetchall()   
            cursor.close()
            connection.close()
            result = userID
            for x in result:
                str =  ''.join(x) 
                self.assertTrue(str.islower())

        #testing that username is all lowercase
        def test_Username2(self):
            with sqlite3.connect(DB_NAME) as connection:
                      cursor = connection.cursor()
                      cursor.execute("Select username, firstName, lastName from customer_data")
                      userID = cursor.fetchall()   
            cursor.close()
            connection.close()
            result = userID
            for x in result:
                string1 = x[0]
                string2 = x[1][0] + x[2]
                string2=string2.lower()
                if(string2 == string1):
                    self.assertTrue(string2)
                else:
                    self.assertFalse(string2)    
            #testing if firstname and last name has been corretly converted to our username syntax
            
        def test_Email(self):
            with sqlite3.connect(DB_NAME) as connection:
                      cursor = connection.cursor()
                      cursor.execute("Select email from customer_data")
                      userID = cursor.fetchall()   
            cursor.close()
            connection.close()    
            result = userID
            for x in result:
                x =  ''.join(x) 
                if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', x) != None:
                    self.assertTrue(x)
                else:
                    self.assertFalse(x)

            #checking if there email is to our syntax

        def test_firstandlast(self):
                with sqlite3.connect(DB_NAME) as connection:
                        cursor = connection.cursor()
                        cursor.execute("Select firstName, lastName from customer_data")
                        userID = cursor.fetchall()   
                cursor.close()
                connection.close()    
                result = userID
                for x in result:
                    firstname = x[0]
                    firstname = ''.join(firstname)
                    lastname =  x[1]
                    lastname = ''.join(lastname)
                    if(firstname[0].isupper and lastname[0].isupper):
                        self.assertTrue(x)
                    else:
                        self.assertFalse(x)
            #Testing if first and last name are capitals

    

if __name__ == '__main__':
    unittest.main()


