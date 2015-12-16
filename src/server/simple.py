import socket
import user
import json
import traceback

import sys

from config import *
from thread import *

def clientthread(connection, address):
    #infinite loop so that function do not terminate and thread do not end.
    while True:
        try:
            buf = connection.recv(1024)
            data = json.loads(buf)
            if data["action"] == "login":
                auser = user.user()
                newUser = auser.login(data["username"], address[0])
                connection.send(json.dumps(newUser))
            elif data["action"] == "find":
                auser = user.user()
                print data["user"]
                auser.set(data["user"])
                result = auser.findFellow()
                print result
                connection.send(str(result))
        except Exception as e:
            print e
            print traceback.print_exc()
        time.sleep(1)
    #came out of loop
    conn.close()

def test():
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    #Bind socket to local host and port
    try:
        mySocket.bind((server_name, server_port))
    except socket.error, msg:
        print 'Bind failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        sys.exit()

    #Start listening on socket
    mySocket.listen(10)

    while True:
        connection, address = mySocket.accept()
        print address
        #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
        start_new_thread(clientthread ,(connection,address,))


if __name__ == "__main__":
    test ()
