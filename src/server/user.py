from config import *

lock = 0

def inlock():
    lock = 1

def unlock():
    lock = 0

class user(object):
    """docstring for user"""
    count = 0
    users = []
    def __init__(self):
        super(user, self).__init__()
        self.uid = -1
        self.username = ""
        self.ip = ""
        self.fellow = -1
        #self.storage = data()

    def set(self, userData):
        self.uid = userData["uid"]
        self.username = userData["username"]
        self.ip = userData["ip"]
        self.fellow = userData["fellow"]
        
    def login(self, username, ip):
        while lock:
            pass
        inlock()
        self.uid = self.count + 1
        newUser = { "uid" : self.count+ 1,
                    "username": username,
                    "ip" : ip,
                    "fellow" : -1,
                  }
        self.users.append(newUser)
        self.count += 1
        unlock()
        return newUser

    def logout(self):
        while lock:
            pass
        inlock()
        for each in self.users:
            if each["uid"] == self.uid:
                self.users.remove(each)
        self.count -= 1;
        unlock()

    def findFellow(self):
        while lock:
            pass
        inlock()
        for each in self.users:
            if each["uid"] != self.uid and each['fellow'] == -1:
                unlock()
                return each
        unlock()

        return None
