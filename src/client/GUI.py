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

	#add a button to send image, you should get the image_path of the image you decide to send first.
	def send_(self, image_path):
		self.postMan.post_image(image_path)
	
    @QtCore.pyqtSlot()
    def receive(self):
        # if chat.receive_queue.empty():
        #     return ""
        # message = chat.receive_queue.get()
        # chat.receive_queue.task_done()
        # message = message.decode('utf-8')
        # return message
        message = self.postMan.get()#if the object is image, the result of get will be a pathname.You can load it easily.
        if(message == None):
            return ""
        else:
            return message
	
    receiveMsg = QtCore.pyqtProperty(str, fget=receive)
    username = QtCore.pyqtProperty(str, fget=getUsername)
    remotename = QtCore.pyqtProperty(str, fget=getRemotename)
    isLogin = QtCore.pyqtProperty(bool, fget=getRemote)
