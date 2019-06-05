import re

class validateData:
        def __init__(self):
                pass
        #checking the name input against our syntax 
        def nameValidation(self,nameInput):
                if nameInput.isalpha():
                       fixedName = nameInput.lower().capitalize()
                       return fixedName
                else:
                       print("Your name can not contain numbers or spaces")
                       fixedName = "BAD"
                       return fixedName
        #checking the password input against our syntax 
         
        def passwordValidation(self,passwordInput):
                SpecialSym =['$', '@', '#', '%', "!"] 
                if len(passwordInput) < 6:
                    print("Password needs to be at least 6 characters long")  
                elif not any(char.isdigit() for char in passwordInput):
                    print("Password should have at least one numeral")
                elif not any(char.isupper() for char in passwordInput): 
                    print('Password should have at least one uppercase letter') 
                elif not any(char in SpecialSym for char in passwordInput):
                    print('Password should have at least one of the following symbols !,%,$,@,#')
                else:
                    validpassword = True
                    return validpassword 
        #checking the email input against our syntax 

        def emailValidation(self,emailInput):
                if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', emailInput) != None:
                    return True
                else:
                     print ("This is not a valid email address")

 
                