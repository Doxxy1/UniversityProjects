from databaseManiuplator import cloudDatabase
import datetime
from googleEvent import googleE
import random
from scanQR import qrScan
from prettytable import PrettyTable 

ERRORRED = '\033[1;31;40m'
RESETTEXT = '\033[m'

class libOpt:
    def __init__(self):
        pass

    def buildDatabase(self):
        cloudDatabase().createUser()
        cloudDatabase().createBook()
        cloudDatabase().createBorrowed()
        cloudDatabase().populateUser()
        cloudDatabase().populateBooks()
        cloudDatabase().populateBookBorrowed()
        cloudDatabase().populateBookReturned()

    def idSearch(self, id):
        book_id_table = PrettyTable()
        book = cloudDatabase().searchByID(id)
        book_id_table.field_names = ["BookID", "Title", "Author", "Published Date"]
        if(book):
            book_id_table.add_row(book)
            print(book_id_table)
            print()
        else:
            print(ERRORRED + 'Sorry, The ID: ' + id + ' was not found, please try again.' + RESETTEXT)
    
    def titleSearch(self, title):
        book_title = PrettyTable()
        book_title.field_names = ["BookID", "Title", "Author", "Published Date"]
        books = cloudDatabase().searchByTitle(title)
        if(books):
            for book in  books:
                book_title.add_row(book)
            print(book_title)
            print()
        else:
            print(ERRORRED + 'Sorry, The Title: ' + title + ' was not found, please try again.' + RESETTEXT)

    def authorSearch(self, author):
        book_author = PrettyTable()
        book_author.field_names = ["BookID", "Title", "Author", "Published Date"]
        books = cloudDatabase().searchByAuthor(author)
        if(books):
            for book in  books:
                book_author.add_row(book)
            print(book_author)
            print()
        else:
            print(ERRORRED + 'Sorry, The Author: ' + author + ' was not found, please try again.' + RESETTEXT)

    #BORROWING FUNCTIONS

    def borrowBook(self, username):
        while(True):
            selection = input('Please enter the ID of the book you would like to borrow: ')
            bookSearch = cloudDatabase().searchByID(selection)
            if(bookSearch is not None):
                select = input("{}. Is this the book you would like to borrow?: Y/n: ".format(bookSearch[1]))
                if(select == 'y' or select == 'Y'):
                    status = cloudDatabase().checkIfBorrowed(selection)
                    if(status is None or status[0] == 'returned'):
                        date = self.getDate()
                        userID = cloudDatabase().getUserID(username)
                        bookID = cloudDatabase().getBookID(selection)
                        booktitle = cloudDatabase().getTitle(selection)
                        email = cloudDatabase().getEmail(userID)
                        eventID = self.generateEventID()
                        googleE().insert(username, booktitle[0], email[0], eventID)
                        cloudDatabase().insertToBorrow(userID, bookID, 'borrowed', date, eventID)
                        inp = input('Would you like to borrow another? Y/n: ')
                        if(inp == 'y' or inp == 'Y'):
                            pass
                        else:
                            return
                    elif(status[0] == 'borrowed'):
                        print( ERRORRED + 'Sorry, this book isnt available' + RESETTEXT)
                        print()
                        return
                    else:
                        print('Error')
                        return
                else:
                    print()
                    return
            else:
                print(ERRORRED + 'Sorry, this book doesnt exist.' + RESETTEXT)


    def getDate(self):
        now = datetime.datetime.now()
        year = '{:02d}'.format(now.year)
        month = '{:02d}'.format(now.month)
        day = '{:02d}'.format(now.day)
        date = '{}-{}-{}'.format(year, month, day)
        return date

    def generateEventID(self):
        for x in range(1):
            eventID =  (random.randint(10000,99999))
            return eventID

    def insertUserName(self, username, email):
        cloudDatabase().insertUser(username, email)
    
    def checkUserExist(self, username):
        return cloudDatabase().userExist(username)


    #RETURNING FUNCTIONS

    def returnBook(self,username):
        while(True):
            userID = cloudDatabase().getUserID(username)
            book = cloudDatabase().listBorrowedBooksForUser(userID)
            if(book):
                print('These are the books you have on loan:')
                self.printReturnList(book)
                selection = input('Which book would you like to return? (By ID): ')
                date = self.getDate()
                eventID = cloudDatabase().getEventID(selection)
                cloudDatabase().setToReturned(selection, 'returned', date)
                googleE().removeEvent(eventID)

                inp = input('Would you like to return another? Y/n ')
                if(inp == 'y' or inp == 'Y'):
                    pass
                elif(inp == 'n' or inp == 'N'):
                    return
                else:
                    print(ERRORRED + inp + ' isnt a valid option, please try again.' + RESETTEXT)
                    print()
            else:
                print(ERRORRED + 'You havent borrowed any books' + RESETTEXT)
                return
    
    def printReturnList(self, book):
        book_return = PrettyTable()
        book_return.field_names = ["BookID", "Title"]
        for books in book:
            book_return.add_row(books)
        print(book_return)
        print()


    def returnByQR(self, username):
        while(True):
            userID = cloudDatabase().getUserID(username)
            book = cloudDatabase().listBorrowedBooksForUser(userID)
            if(book):
                bookBorrowID = qrScan().scanCode()
                date = self.getDate()
                eventID = cloudDatabase().getEventID(bookBorrowID)
                cloudDatabase().setToReturned(bookBorrowID, 'returned', date)
                googleE().removeEvent(eventID)
                inp = input('Would you like to return another? Y/n ')
                if(inp == 'y' or inp == 'Y'):
                    pass
                elif(inp == 'n' or inp == 'N'):
                        return
                else:
                        print(ERRORRED + inp + ' isnt a valid option, please try again.' + RESETTEXT)
                        print()
            else:
                print(ERRORRED + 'You havent borrowed any books' + RESETTEXT)
                return   





    #Test Functions

    def insertBook(self):
        title = input('Title: ')
        author = input('Author: ')
        date = input('Published Date: ')
        cloudDatabase().insertBook(title,author,date)
    
    def listBooks(self):
        cloudDatabase().listBook()
        print()

    def userNamePrint(self):
        with cloudDatabase() as cD:
            user = cD.listUsers()
            print(user)

    def bbPrint(self):
        print("{:<10}{:<10}{:<10}{:<10}{:<10}{}".format('BBID', 'UserID', 'BookID', 'Staus', 'BorrowedDate', 'ReturnedDate'))
        with cloudDatabase() as cD:
            for book in cD.listBB():
                print("{:<10}{:<10}{:<10}{:<10}{}        {}".format(book[0], book[1], book[2], book[3], book[4], book[5]))
                print()
    
    def listCalendarEvents(self):
        googleE().calendarList()