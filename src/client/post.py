# coding=utf-8

import socket
import json
import time
import threading
import Queue

import letter
import user

import config
from info import info

# message sending queue
send_queue = Queue.Queue()
# message receive queue
receive_queue = Queue.Queue()

username_local = ""
username_remote = ""
server_name_remote = ""
server_name_local  = socket.gethostbyname(socket.gethostname())

class ServerPostOffice(object):
    """docstring for ServerPostOffice"""
    def __init__(self):
        super(ServerPostOffice, self).__init__()
        self.sock = None
        self.user = None

    def getUser(self, username, server):
    	#连接服务器
    	try:
    		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    		sock.connect((config.server_name, config.remote_server_port))
    		sock.settimeout(15)
    	#检测服务器是否关闭
        except Exception:
    		info("connection error", "error")
    		return None
    	sock.send('{"action":"login","uid":0,"username":"%s","ip":"%s"}' %(username, server))
    	userdata = sock.recv(1024)
    	print userdata
    	u = user.user()
    	u.set(json.loads(userdata))
    	while True:
    		print "[FLOATER FIND] try to find fellow"
    		sock.send('{"action":"find"}')
    		fellow = sock.recv(1024)
    		if fellow != "None":
    			print "[FLOATER FOUND]", fellow
    			userData = json.loads(fellow)
    			u.set(userData)
    			break
    		time.sleep(5)
    	sock.send('{"action":"close"}')
    	sock.close()
        global username_remote
        username_remote = userData["username"]
        global server_name_remote
        server_name_remote = userData["ip"]

class ClientPostOffice(object):
    """docstring for PostOffice"""
    def __init__(self):
        pass

    def send(self, username, server_name_remote):
        """This function is use for sending threading"""
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # wait 1 second before connection
        time.sleep(1)

        while True:
            try:
                mySocket.connect((server_name_remote, config.server_port))
                break;
            except socket.error, msg:
                info('connect failed. Error Code : %s %s' % (str(msg[0]), msg[1]), "error")
                time.sleep(1)
        info("start send thread", "info")
        while True:
            # get a message from the send_queue and then send the message to remote
            message = send_queue.get()
            send_queue.task_done()
            try:
                mySocket.send(message)
                info("a message has sent to remote", "info")
            except Exception as e:
                info(e, "error")
                break

    def receive(self, username, server_name_remote):
        mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        time.sleep(1)
        try:
            mySocket.bind((server_name_remote, config.server_port))
        except socket.error, msg:
            info('connect failed. Error Code : %s %s' % (str(msg[0]), msg[1]), "error")
            return False
        mySocket.listen(100)
        info("start receive thread", "info")
        connection, address = mySocket.accept()
        info("connection accepted", "info")
        while True:
            try:
                message = connection.recv(1024)
                info("receive message from remote: %s" % message, "info")
                receive_queue.put("%s" % (message))
            except Exception as e:
                info(e, "error")
                return

class PostMan(object):
    """docstring for PostMan"""
    clientPostOffice = ClientPostOffice()
    serverPostOffice = ServerPostOffice()

    def __init__(self):
        super(PostMan, self).__init__()

    def start_chat(self):
        self.chart_t1 = threading.Thread(target=self.clientPostOffice.receive,\
        args=(username_remote, server_name_local))
        self.chart_t2 = threading.Thread(target=self.clientPostOffice.send, \
        args=(username_local, server_name_remote))
        self.chart_t1.start()
        self.chart_t2.start()

    def start_search(self):
        self.server_t = threading.Thread(target=self.serverPostOffice.getUser, args=(username_local, server_name_local))
        self.server_t.start()

    def stop_work(self):
        pass

    def post_message(self, text):
        package = letter.letter()
        package.set_user(username_local, username_remote)
        package.set_message(text)
        send_queue.put(package.serialize())

    def post_image(self, image_path, username_local, user_remote):
        pass

    def get(self):
        if receive_queue.empty():
            return None
        remote_message = receive_queue.get()
        receive_queue.task_done()
        package = letter.letter()
        package.materialize(remote_message)
        if package.message["close"] == True:
            stop_work()
        elif package.message["contentT"] == "text":
            return package["content"]
        elif package.message["contentT"] == "image":
            # here need to be modified
            return None
        else:
            return None
