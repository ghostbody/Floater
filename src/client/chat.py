import socket
import json
import user
import time

from config import *
import threading

def send(username, server_name):
    #server_name = "192.168.1.102"
    server_port = 8001
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    try:
        mySocket.connect((server_name, server_port))
    except socket.error, msg:
        print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' ' + msg[1]
        return

    while True:
        message = raw_input()
        print "[%s]: %s" % (username, message)
        try:
            mySocket.send(message)
        except Exception as e:
            print "[FLOATER ERROR] ", e
            break

def receive(username, server_name):
    #server_name = "192.168.1.207"
    server_port = 8001
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    try:
        mySocket.bind((server_name, server_port))
    except socket.error, msg:
        print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        return False
    mySocket.listen(100)

    connection, address = mySocket.accept()
    print "[FLOATER ACCEPT CONNECTION] ", address

    while True:
        message = connection.recv(1024)
        print "[%s]: %s" % (username, message)

def test():
    print  "[FLOATER CHATER 1.0] Online line"
    # remote server
    server_name_remote = "192.168.1.102"
    server_name_local  = "192.168.1.207"
    # username
    username = "Alice"

    t1 = threading.Thread(target=receive, args=(username, server_name_local))
    t2 = threading.Thread(target=send, args=(username, server_name_remote))

    t1.start()
    t2.start()


if __name__ == '__main__':
    test()
