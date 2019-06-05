from Database import DatabaseInfo
from customerOptions import Options
from RP.Fdata.face_recognition import Recognition
class Menu:
        def __init__(self):
                pass

        def runMenu(self):
                print("---Welcome to the Recpection Desk please select an option---")
                while(True):
                    print("")
                    print(" 1. Register with Command Line ")
                    print(" 2. Register with Facial Recognition")
                    print(" 3. Login with Command Line")
                    print(" 4. Login with Facial Recognition")
                    print(" 5. Quit")
                    print("")
                    selection = input("Select an option: ")
                  
                    print("")

                    if(selection == "1"):
                        Options().registerCustomer()
                    elif(selection == "2"):
                        Options().registerCustomer()
                        username = input("Please enter your username that you just created: ")
                        Options().registerFace(username)
                        Recognition().new_user_reg(username)
                        Recognition().face_encode()
                    elif(selection == "3"):
                       Options().loginCustomer()
                    elif(selection == "4"):
                        user = Recognition().face_recongnition()
                        if user:
                            Options().loginFace(user[0])
                        else:
                            print("Your face was not recognized. Please try again")
                    elif(selection == "5"):
                        print("Goodbye!")
                        break
                    else:
                        print("Invalid input - please try again.")
                        print("")
