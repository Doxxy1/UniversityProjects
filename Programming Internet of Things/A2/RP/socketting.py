import socket, json, sqlite3, sys
sys.path.append("..")
import socket_utils 

with open("config.json", "r") as file:
    data = json.load(file)
    
HOST = data["masterpi_ip"] # The server's hostname or IP address.
PORT = 13375               # The port used by the server.
ADDRESS = (HOST, PORT)

class connectionSocket:

    def __init__(self):
            pass
    #waiting and establishing a conenction to the master PI
    def masterConnection(self,loginConnection):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            print("Connecting to {}...".format(ADDRESS))
            s.connect(ADDRESS)
            print("Connected.")

            print("Logging in as {}".format(loginConnection[0]))
            socket_utils.sendJson(s, loginConnection)

            print("Waiting for Master Pi...")
            while(True):
                object = socket_utils.recvJson(s)
                if("logout" in object):
                    print("Master Pi logged out.")
                    print()
                    break 