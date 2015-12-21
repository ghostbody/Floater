import sys
from PyQt4 import QtCore, QtGui, QtWebKit

import chat

import threading
import os

html = open(os.path.join("front", "index.html")).read()

class Floater(QtCore.QObject):
    """Simple class with one slot and one read-only property."""

    @QtCore.pyqtSlot(str)
    def showMessage(self, msg):
        """Open a message box and display the specified message."""
        QtGui.QMessageBox.information(None, "hahhahah", msg)

    def getUsername(self):
        """Return the Python version."""
        return "Bob"

    @QtCore.pyqtSlot(str)
    def send(self, message):
        chat.send_queue.put("%s: %s" % ("Bob", message))

    @QtCore.pyqtSlot()
    def receive(self):
        if chat.receive_queue.empty():
            return ""
        message = chat.receive_queue.get()
        chat.receive_queue.task_done()
        print "receive ", message
        return message

    """Python interpreter version property."""
    receiveMsg = QtCore.pyqtProperty(str, fget=receive)
    username = QtCore.pyqtProperty(str, fget=getUsername)

def main():

    print  "[FLOATER CHATER 1.0] Online line"
    # remote server
    server_name_remote = "192.168.1.102"
    server_name_local  = "192.168.1.207"
    # username
    username_local = "Alice"
    username_remote = "Bob"

    # start two thread
    # thread t1 is a scoket that connect to the remote peer, and receive messgae from remote
    t1 = threading.Thread(target=chat.receive, args=(username_remote, server_name_local))
    # thread t2 is a socket that listen a port in local and send message to remote
    t2 = threading.Thread(target=chat.send, args=(username_local, server_name_remote))

    t1.start()
    t2.start()

    app = QtGui.QApplication(sys.argv)

    myObj = Floater()

    webView = QtWebKit.QWebView()
    # Make myObj exposed as JavaScript object named 'pyObj'
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
    webView.setHtml(html)

    window = QtGui.QMainWindow()
    window.setCentralWidget(webView)
    window.show()

    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
