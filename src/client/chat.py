import socket
import json
import time

from config import *
import threading
import Queue

"""these two queues are use for thread comunication"""
# message sending queue
send_queue = Queue.Queue()
# message receive queue
receive_queue = Queue.Queue()

def send(username, server_name):
    """This function is use for sending threading"""
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # wait 1 second before connection
    time.sleep(1)

    while True:
        try:
            mySocket.connect((server_name, server_port))
            break;
        except socket.error, msg:
            print '[FLOATER ERROR] Connect failed. Error Code : ' + str(msg[0]) + ' ' + msg[1]
            time.sleep(1)

    while True:
        # get a message from the send_queue and then send the message to remote
        message = send_queue.get()
        send_queue.task_done()
        print "[FLOATER ERROR] send message to remote"
        try:
            mySocket.send(message)
        except Exception as e:
            print "[FLOATER ERROR] ", e
            break
        # if user send close message, close the connection
        if message == "$$CLOSE$$":
            print "[FLOATER CLOSE CONNECTION] connection closed by you"
            break
        print "[%s]: %s" % (username, message)

def receive(username, server_name):
    mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    time.sleep(1)
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
            print "[FLOATER RECIEVE] receive message from remote"
        except Exception as e:
            print "[FLOATER ERROR] ", e
            return

        # if get close message from remote, then close connection
        if message == "$$CLOSE$$" or message == "":
            print "[FLOATER CLOSE CONNECTION] connection closed by remote"
            connection.close()
            return

        receive_queue.put("%s" % (message))

if __name__ == '__main__':
    test()
