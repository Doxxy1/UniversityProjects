import sqlite3

from menuRP import Menu
from Database import DatabaseInfo
# Main function.
def main():
    
        DatabaseInfo().createDatabase()
        Menu().runMenu()
# Execute program.
if __name__ == "__main__":
    main()

