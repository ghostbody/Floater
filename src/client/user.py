class user(object):
    def __init__(self):
        super(user, self).__init__()
        self.uid = -1
        self.username = ""
        self.ip = ""
        self.fellow = -1

    def set(self, userData):
        self.uid = userData["uid"]
        self.username = userData["username"]
        self.ip = userData["ip"]
        self.fellow = userData["fellow"]
