import sys
from PyQt4 import QtCore, QtGui, QtWebKit

from config import *
import chat
import GUI
import threading
import os

def main():

    print  "[FLOATER CHATER 1.0] Online line"
    # remote server
    GUI.server_name_remote = "192.168.1.102"
    GUI.server_name_local  = "192.168.1.207"

    # start two thread
    # thread t1 is a scoket that connect to the remote peer, and receive messgae from remote
    t1 = threading.Thread(target=chat.receive, args=(GUI.username_remote, GUI.server_name_local))
    # thread t2 is a socket that listen a port in local and send message to remote
    t2 = threading.Thread(target=chat.send, args=(GUI.username_local, GUI.server_name_remote))

    t1.start()
    t2.start()

    app = QtGui.QApplication(sys.argv)
    myObj = GUI.Floater()
    webView = QtWebKit.QWebView()
    # Make myObj exposed as JavaScript object named 'pyObj'
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
    webView.setHtml(GUI.html, QtCore.QUrl(system_path));

    window = QtGui.QMainWindow()
    window.setMaximumSize(700, 700)
    window.setMinimumSize(700, 700)
    window.setCentralWidget(webView)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
