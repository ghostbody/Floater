import socket
import time
import json

if __name__ == "__main__":
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    username = raw_input("Please input your username to find a fellow:\n")
    sock.connect(('localhost', 8000))
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
        sleep(5)

    sock.close()
