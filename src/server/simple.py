import socket
import user
import json
import traceback

import time
import sys

from config import *
from thread import *

def clientthread(connection, address):
    #infinite loop so that function do not terminate and thread do not end.
    auser = user.user()
    while True:
        try:
            buf = connection.recv(1024)
            data = json.loads(buf)
            if data["action"] == "login":
                newUser = auser.login(data["username"], address[0])
                print "[FLOATER LOGIN] ", address
                connection.send(json.dumps(newUser))
            elif data["action"] == "find":
                result = auser.findFellow()
                print "[FLOATER FIND FELLOW] user:", address, "find", result
                connection.send(str(result))
            elif data["action"] == "logout":
                auser.logout()
                print "[FLOATER FIND FELLOW] user:", address, "find", result
                connection.send(str("{statu: OK}"))
            elif data["action"] == "close":
                print"[FLOATER CLOSE CONNECTION] ", address
                break
            else:
                auser.logout()
                print"[FLOATER CLOSE CONNECTION] ", address
                break
        except Exception as e:
            auser.logout()
            print"[FLOATER CLOSE CONNECTION] ", address
            print e, traceback.print_exc()
            connection.close()
            return
        time.sleep(1)
    #came out of loop
    connection.close()

def test():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind socket to local host and port
    try:
        mySocket.bind((server_name, server_port))
    except socket.error, msg:
        print '[FLOATER ERROR] Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    #Start listening on socket
    mySocket.listen(100)

    while True:
        connection, address = mySocket.accept()
        print "[FLOATER ACCEPT CONNECTION] ", address
        # start new thread takes 1st argument as a function name to be run,
        # second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(connection,address,))

if __name__ == "__main__":
    test ()
