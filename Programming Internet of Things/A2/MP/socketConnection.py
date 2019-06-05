import socket, json, sys
sys.path.append("..")
import socket_utils
from masterMenu import Menu

HOST=""
PORT = 13375
ADDRESS = (HOST,PORT)

def queryConnect():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind(ADDRESS)
        s.listen()

        print("Listening on {}...".format(ADDRESS))
        while True:
            print("Waiting for authentication...")
            conn, addr = s.accept()
            with conn:
                print("Connected to {}".format(addr))
                print()
                
                user = socket_utils.recvJson(conn)
                username = user[0]
                email = user[2]
                Menu().userMenu(username, email)
                socket_utils.sendJson(conn, { "logout": True})

