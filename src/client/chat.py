import socket
import json
import time

from config import *
import threading
import Queue

send_queue = Queue.Queue()
receive_queue = Queue.Queue()

def send(username, server_name):
    #server_name = "192.168.1.102"
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(5)
    while True:
        try:
            mySocket.connect((server_name, server_port))
            break;
        except socket.error, msg:
            print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' ' + msg[1]
            time.sleep(1)

    while True:
        message = send_queue.get()
        send_queue.task_done()
        try:
            mySocket.send(message)
        except Exception as e:
            print "[FLOATER ERROR] ", e
            break
        # if user send close close message, close the connection
        if message == "$$CLOSE$$":
            print "[FLOATER CLOSE CONNECTION] connection closed by you"
            break
        print "[%s]: %s" % (username, message)

def receive(username, server_name):
    #server_name = "192.168.1.207"
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
        try:
            message = connection.recv(1024)
        except Exception as e:
            print "[FLOATER ERROR] ", e
            return

        # if get close messge from remote, then close connection
        if message == "$$CLOSE$$" or message == "":
            print "[FLOATER CLOSE CONNECTION] connection closed by remote"
            connection.close()
            return
        q.put("%s: %s" % (username, messge))

def test():
    print  "[FLOATER CHATER 1.0] Online line"
    # remote server
    server_name_remote = "192.168.1.147"
    server_name_local  = "192.168.1.207"
    # username
    username_local = "Alice"
    username_remote = "Bob"

    # start two thread
    # thread t1 is a scoket that connect to the remote peer, and receive messgae from remote
    t1 = threading.Thread(target=receive, args=(username_remote, server_name_local))
    # thread t2 is a socket that listen a port in local and send message to remote
    t2 = threading.Thread(target=send, args=(username_local, server_name_remote))

    t1.start()
    t2.start()


if __name__ == '__main__':
    test()
