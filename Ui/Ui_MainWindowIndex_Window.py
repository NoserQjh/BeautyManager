'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-26 16:42:28
@Description:
'''

from Ui.Ui_MainWindowIndex import Ui_Index
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Ui.CardEdit.Ui_DialogCardEdit_Window import DialogCardEdit_Window
from Ui.ProductEdit.Ui_DialogProductEdit_Window import DialogProductEdit_Window
class MainWindowIndex_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_Index()
        self.ui.setupUi(self)

        self.ui.pushButtonCardEdit.clicked.connect(self.buttonCardEditClicked)
        self.ui.pushButtonProductEdit.clicked.connect(self.buttonProductEditClicked)
        self.ui.pushButtonExit.clicked.connect(self.close)

    def buttonCardEditClicked(self):
        self.cardEdit = DialogCardEdit_Window()
        self.cardEdit.show()

    def buttonProductEditClicked(self):
        self.productEdit = DialogProductEdit_Window()
        self.productEdit.show()
