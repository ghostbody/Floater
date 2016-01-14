#coding:utf-8

from PyQt4 import QtCore, QtGui, QtWebKit
import threading
import os
import user
import sys
import socket
reload(sys)
sys.setdefaultencoding('utf8')

import post

class Floater(QtCore.QObject):
    postMan = post.PostMan()

    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        """Open a message box and display the specified message."""
        QtGui.QMessageBox.information(None, "FLOATER 1.0", msg)

    @QtCore.pyqtSlot()
    def getUsername(self):
        return post.username_local

    @QtCore.pyqtSlot()
    def getRemotename(self):
        return post.username_remote

    @QtCore.pyqtSlot(str)
    def setUsername(self, username):
        post.username_local = username

    @QtCore.pyqtSlot()
    def getRemote(self):
        if post.username_remote == "":
            return True;
        else:
            return False;

    @QtCore.pyqtSlot()
    def searchThread(self):
        self.postMan.start_search()

    @QtCore.pyqtSlot()
    def setThreads(self):
        self.postMan.start_chat()

    @QtCore.pyqtSlot(str)
    def send(self, message):
        # chat.send_queue.put("%s" % (message))
        self.postMan.post_message("%s" % message)

    @QtCore.pyqtSlot()
    def receive(self):
        message, contentT = self.postMan.get()
        if(message == None):
            return ""
        else:
            if contentT == "Text":
                return '{"message":"%s", "type":"Text"}'
            elif contentT == "Image":
                return '{"path":"%s", "type":"Image"}'

    @QtCore.pyqtSlot()
    def openImage(self):
        filename = QtGui.QFileDialog.getOpenFileName(caption="Iput Image", filter="*.png *.jpg *.bmp")
        if(filename != "" and filename != None):
            self.postMan.post_image(filename)
        return filename

    imageName = QtCore.pyqtProperty(str, fget=openImage)
    receiveMsg = QtCore.pyqtProperty(str, fget=receive)
    username = QtCore.pyqtProperty(str, fget=getUsername)
    remotename = QtCore.pyqtProperty(str, fget=getRemotename)
    isLogin = QtCore.pyqtProperty(bool, fget=getRemote)
