import sys
from PyQt4 import QtCore, QtGui, QtWebKit

import chat

import threading
import os

import sys
reload(sys)
sys.setdefaultencoding('utf8')

username_local = ""
username_remote = ""

html = open(os.path.join("front", "index.html")).read()

class Floater(QtCore.QObject):
    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        """Open a message box and display the specified message."""
        QtGui.QMessageBox.information(None, "hahhahah", msg)

    def getUsername(self):
        return username_local

    @QtCore.pyqtSlot(str)
    def send(self, message):
        chat.send_queue.put("%s" % (message))

    @QtCore.pyqtSlot()
    def receive(self):
        if chat.receive_queue.empty():
            return ""
        message = chat.receive_queue.get()
        chat.receive_queue.task_done()
        message = message.decode('utf-8')
        return username_remote + " :" + message

    receiveMsg = QtCore.pyqtProperty(str, fget=receive)
    username = QtCore.pyqtProperty(str, fget=getUsername)
