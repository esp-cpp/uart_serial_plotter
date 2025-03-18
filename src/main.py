#!/usr/bin/python
from main_window import MainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtGui
import signal

from list_serial_ports import add_port_descriptor

signal.signal(signal.SIGINT, signal.SIG_DFL)
import sys

from resource_helpers import path

def main():
    # get the arguments, and if there are any, add them as allowed port descriptors
    for arg in sys.argv[1:]:
        print("Adding port descriptor: '{}'".format(arg))
        add_port_descriptor(arg)

    app = QApplication(sys.argv)
    app.setWindowIcon(QtGui.QIcon(path("images/icon.png")))
    MainWindow()
    sys.exit(app.exec_())


if __name__ == "__main__":
    main()
