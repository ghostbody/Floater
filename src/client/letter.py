import json
import time
import user

class letter(object):
    def __init__(self):
        self.message = {
            "version"  : 1.0,
            "date"     : time.ctime(),
            "srcuser"  : "",
            "destuser" : "",
            "close"    : False,
            "open"     : False,
            "contentT" : "",
            "content"  : "",
        }

    def set_user(self, srcuser, destuser):
        self.message["srcuser"] = "%s" % srcuser
        self.message["destuser"] = "%s" % destuser

    def serialize(self):
        return str(json.dumps(self.message))

    def materialize(self, jsonStr):
        data = json.loads(jsonStr)
        self.message["version"] = data["version"]
        self.message["date"] = data["date"]
        self.message["srcuser"] = data["srcuser"]
        self.message["destuser"] = data["destuser"]
        self.message["close"] = data["close"]
        self.message["contentT"] = data["contentT"]
        self.message["content"] = data["content"]
        self.message["open"] = data["open"]

    def set_message(self, message):
        self.message["date"] = time.ctime()
        self.message["close"] = False
        self.message["contentT"] = "Text"
        self.message["content"] = message

    def set_Image(self, picture_path):
        self.message["date"] = time.ctime()
        self.message["close"] = False
        self.message["contentT"] = "Image"
        self.message["content"] = picture_path

    def set_audio(self, audio_path):
        pass

    def set_file(self, file_path):
        pass
