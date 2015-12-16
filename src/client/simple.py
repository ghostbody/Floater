import socket
import time
import json
import time

from config import *


if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    username = raw_input("Please input your username to find a fellow:\n")
    sock.connect((server_name, server_port))
    sock.send('{"action":"login", "username": "%s"}' % username)
    user = sock.recv(1024)
    print user

    while True:
        print "try to find fellow"
        sock.send('{"action":"find", "user": %s}' % user)
        fellow = sock.recv(1024)
        if fellow != "None":
            print fellow
            break
        time.sleep(5)

    sock.close()
