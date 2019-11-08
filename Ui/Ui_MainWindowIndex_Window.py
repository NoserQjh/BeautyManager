'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-08 16:08:29
@Description:
'''

from Ui.Ui_MainWindowIndex import Ui_Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Ui.CardEdit.Ui_DialogCardEdit_Window import DialogCardEdit_Window

class MainWindowIndex_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Index()
        self.ui.setupUi(self)

        self.ui.pushButtonCardEdit.clicked.connect(self.buttonCardEditClicked)
        self.ui.pushButtonExit.clicked.connect(self.close)

    def buttonCardEditClicked(self):
        self.carEdit = DialogCardEdit_Window()
        self.carEdit.show()
