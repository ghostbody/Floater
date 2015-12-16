import socket
import time
import json
<<<<<<< HEAD
import time

from config import *
=======
>>>>>>> a9eef65b2b0497f8cf6e04afdd9d68d6959ea53c

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    username = raw_input("Please input your username to find a fellow:\n")
<<<<<<< HEAD
    sock.connect((server_name, server_port))
=======
    sock.connect(('localhost', 8000))
>>>>>>> a9eef65b2b0497f8cf6e04afdd9d68d6959ea53c
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
<<<<<<< HEAD
        time.sleep(5)
=======
        sleep(5)
>>>>>>> a9eef65b2b0497f8cf6e04afdd9d68d6959ea53c

    sock.close()
