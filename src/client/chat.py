import socket
import json
import user
import time

from config import *
import threading

def me(username):
    server_name = "localhost"
    server_port = 8002
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    try:
        mySocket.connect((server_name, server_port))
    except socket.error, msg:
        print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        return False

    while True:
        message = raw_input()
        print "[%s]: %s" % (username, message)
        try:
            mySocket.send(message)
        except Exception as e:
            print "[FLOATER ERROR] ", e
            break

def far(username):
    server_name = "localhost"
    server_port = 8001
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    try:
        mySocket.bind((server_name, server_port))
    except socket.error, msg:
        print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' Message ' + msg[1]
        return False

    connection, address = mySocket.accept()
    print "[FLOATER ACCEPT CONNECTION] ", address

    while True:
        message = connection.recv(1024)
        print "[%s]: %s" % (username, message)

def test():
    print  "[FLOATER CHATER 1.0] Online line"
    t1 = threading.Thread(target=me, args=("Alice",))
    t2 = threading.Thread(target=far, args=("Bob",))
    t1.start()
    t2.start()


if __name__ == '__main__':
    test()
