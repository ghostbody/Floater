# coding=utf-8

import socket
import time
import json
import time
import user
from config import *

#login的格式有待改进
def sendLocal(username_local, server_name_local):
	#连接服务器
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((server_name, server_port))
		sock.settimeout(15)
	#检测服务器是否关闭
	except socket.timeout:
		print "Error:timeout"
	sock.send('{"action":"login","uid":0,"username":"%s","ip":"%s"}' %(username_local,server_name_local))
	sock.send('{"action":"close"}')
	sock.close()

#返回值是user类，通过访问其成员变量可获得用户名和IP
def getUser():
	#连接服务器
	try:
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.connect((server_name, server_port))
		sock.settimeout(15)
	#检测服务器是否关闭
	except socket.timeout:
		print "Error:timeout"
		return None
	u = user.user()
	while True:
		print "[FOATER FIND] try to find fellow"
		sock.send('{"action":"find"}')
		fellow = sock.recv(1024)
		if fellow != "None":
			print "[FLOATER FOUND]", fellow
			userData = json.loads(fellow)
			u.uid = userData["uid"]
			u.username = userData["username"]
			u.ip = userData["ip"]
			u.fellow = userData["fellow"]
			break
		time.sleep(5)
	sock.send('{"action":"close"}')
	sock.close()
	return u
