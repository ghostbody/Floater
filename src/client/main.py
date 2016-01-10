import sys
from PyQt4 import QtCore, QtGui, QtWebKit

from config import *
import post
import GUI
from info import info

import threading
import os

def main():
    info("client online", "info")

    app = QtGui.QApplication(sys.argv)
    myObj = GUI.Floater()
    webView = QtWebKit.QWebView()
    # Make myObj exposed as JavaScript object named 'pyObj'
    webView.page().mainFrame().addToJavaScriptWindowObject("pyObj", myObj)
    webView.setUrl(QtCore.QUrl('./front/index.html'))

    window = QtGui.QMainWindow()
    window.setMaximumSize(700, 700)
    window.setMinimumSize(700, 700)
    window.setCentralWidget(webView)
    window.show()

    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
