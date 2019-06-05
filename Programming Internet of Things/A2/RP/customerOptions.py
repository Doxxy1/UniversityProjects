from Database import DatabaseInfo
from validation import validateData
from socketting import connectionSocket
from passlib.hash import sha256_crypt
import getpass

class Options:

    def __init__(self):
            pass
    
    def registerCustomer(self):
                print("---Register---")
                vfirstName = "BAD"     
                while(vfirstName == "BAD"):
                        firstName = input("Enter your first name: ")
                        vfirstName= validateData().nameValidation(firstName)
                   
                vlastName ="BAD"
                while(vlastName == "BAD"):
                        lastName = input("Enter your last name : ")
                        vlastName= validateData().nameValidation(lastName)
                  
                vpassword = False
                while(vpassword != True):
                        print("Your password must contain:\n at least 6 letters,\n a capital letter,\n a number and one of the following symbols !,%,$,@,#")
                        password = input("Enter your password  : ")
                        vpassword = validateData().passwordValidation(password)

                vemail = False
                while(vemail != True):
                        email = input("Enter your email     : ")
                        vemail= validateData().emailValidation(email)

                hashedPassword = sha256_crypt.hash(password)
                username = vfirstName[0] + vlastName 
                username = username.lower()
                print("Your Username is:" + username)

                DatabaseInfo().addCustomer(username,hashedPassword,vfirstName,vlastName,email)


    def loginCustomer(self):

        print("---Login---")
        loginUser = input("Enter your username:")
        getRegisteredUser = DatabaseInfo().login(loginUser)
        if getRegisteredUser is None:
            print("The username entered: " + loginUser +" does not exist please try again")
        else: 
            verify = False
            while(verify == False):
                loginPassword = getpass.getpass("Enter your password:")
                
                if sha256_crypt.verify(loginPassword, getRegisteredUser[1]):
                    print("Successful Login")
                    verify = True
                    #Connect to masterMP with socket and connect to online database
                    connectionSocket().masterConnection(getRegisteredUser)
                else:
                    print("Incorrect password, please try again") 



    def registerFace(self,username):
         getRegisteredUser = DatabaseInfo().login(username)
         if getRegisteredUser is None:
            print("The username entered: " + username +" does not exist please try again")
         else: 
                 return username

    def loginFace(self,username):
         getRegisteredUser = DatabaseInfo().login(username)
         connectionSocket().masterConnection(getRegisteredUser)
