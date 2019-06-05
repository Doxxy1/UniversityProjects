# MENU FOR MASTER MENU
from libOptions import libOpt
import speechRec
import bannerMenu


ERRORRED = '\033[1;31;40m'
RESETTEXT = '\033[m'
greenArrow = '\033[92m' + '>>'
colours = {
        'blue': '\033[94m',
        'pink': '\033[95m',
        'green': '\033[92m',
        'white' : '\033[97m',
        }

class  Menu:
    def __init__(self):
        pass

    def colourize(self, string, colour):
        if not colour in colours: return string
        return colours[colour] + string + '\033[0m'

    def userMenu(self, username, email):
        #libOpt().buildDatabase()
        uE = libOpt().checkUserExist(username)
        if(uE is None):
            libOpt().insertUserName(username, email)
        else:
            pass
        bannerMenu.runBanner()
        print('You are logged in as: ' + self.colourize(username, 'blue'))
        while(True):
            print(greenArrow + self.colourize(' 1. List All Books', 'white'))
            print(greenArrow + self.colourize(' 2. Search For Book(s)', 'white'))
            print(greenArrow + self.colourize(' 3. Borrow Book(s)', 'white'))
            print(greenArrow + self.colourize(' 4. Return Book(s)', 'white'))
            print(greenArrow + self.colourize(' 5. Logout', 'white'))
            selection = input("Select an option: ")
            print()

            if(selection == "1"):
                libOpt().listBooks()
            elif(selection == "2"):
                
                choice = self.searchChoice()
                if(choice == 'speech'):
                    self.voiceSearch()
                elif(choice == 'text'):
                    self.searchMenu()

            elif(selection == "3"):
                self.borrowMenu(username)
            elif(selection == "4"):
                self.returnMenu(username)
            elif(selection == "5"):
                print("Logging Out, Goodbye.")
                break
            else:
                print(ERRORRED +  selection + ' is not an option. Please try again. \n' + RESETTEXT)

    def searchChoice(self):
        while(True):
            selection = input(greenArrow + self.colourize(' Would you like to search by speech or text?: ', 'white'))
            if(selection == 'speech'):
                return selection
            elif(selection == 'text'):
                return selection
            elif(selection == 'quit'):
                print()
                return
            else:
                print(ERRORRED +  selection + ' is not an option. Please try again. \n' + RESETTEXT)

    
    def searchMenu(self):
        while(True):
            print(greenArrow + self.colourize(' You may search by: ', 'white') + '\n' +
                greenArrow + self.colourize(" 1. ID ", 'white') +  '\n' +
                greenArrow + self.colourize(" 2. Title ", 'white') + '\n' +
                greenArrow + self.colourize(" 3. Author ", 'white') + '\n' +
                greenArrow + self.colourize(" 4. Return To Menu ", 'white') + '\n')

            selection = input("Select an option: ")
            if(selection == '1'):
                s1 = input('Which ID Would You Like To Search For?: ')
                print()
                libOpt().idSearch(s1)
                
            elif(selection == '2'):
                s2 = input('Which Title Would You Like To Search For?: ')
                print()
                libOpt().titleSearch(s2)

            elif(selection == '3'):
                s3 = input('Which Author Would You Like To Search For?: ')
                print()
                libOpt().authorSearch(s3)

            elif(selection == '4'):
                print('Returning To Menu...')
                print()
                break
            else:
                print(ERRORRED +  selection + ' is not an option. Please try again. \n' + RESETTEXT)

    def voiceSearch(self):
        while(True):
            print(greenArrow + self.colourize(' You may search by: ', 'white') + '\n' +
                greenArrow + self.colourize(" 1. Title ", 'white') + '\n' +
                greenArrow + self.colourize(" 2. Author ", 'white') + '\n' +
                greenArrow + self.colourize(" 3. Return To Menu ", 'white') + '\n')
            selection = input('What would you like to search by? ')
            if(selection == '1'):
                audio = speechRec.speechSearch()
                if(audio is not None):
                    libOpt().titleSearch(audio)
            elif(selection == '2'):
                audio = speechRec.speechSearch()
                if(audio is not None):
                    libOpt().authorSearch(audio)
            elif(selection == '3'):
                print()
                return
            elif(selection == 'quit'):
                return
            else:
                print(ERRORRED +  selection + ' is not an option. Please try again. \n' + RESETTEXT)



    def borrowMenu(self, username):
        while(True):
            print(greenArrow + self.colourize(' The rules for borrowing a book are: ', 'white') + '\n' +
                greenArrow + self.colourize(" 1. A book must be returned one week after it is borrowed", 'white') +  '\n' +
                greenArrow + self.colourize(" 2. A Google calender event will be made for the date", 'white') + '\n' +
                greenArrow + self.colourize(" 3. You may borrow as many books as you would like.", 'white') + '\n' +
                greenArrow + self.colourize(" 4. Return To Menu ", 'white') + '\n')
            select = input('Would you like to continue? Y/n: ')
            if(select == 'y' or select == 'Y'):
                    libOpt().borrowBook(username)
            elif(select == 'n' or select == 'N'):
                print()
                return
            elif(select == '4'):
                return
            else:
                print(ERRORRED +  select + ' is not an option. Please try again. \n' + RESETTEXT)
    
    def returnMenu(self, username):
        while(True):
            print(greenArrow + self.colourize(' Would you like to return the book with a QR code or the ID? ', 'white') + '\n' +
                greenArrow + self.colourize(' Enter quit to return to menu', 'white'))
            selection = input('Selection: ')

            if(selection == 'id' or selection == 'ID'):
                libOpt().returnBook(username)
            elif(selection == 'QR' or selection == 'qr'):
                libOpt().returnByQR(username)
            elif(selection == 'quit'):
                return
            else:
                print(ERRORRED +  selection + ' is not an option. Please try again. \n' + RESETTEXT)
    