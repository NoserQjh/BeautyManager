'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-07 11:01:26
@Description:
'''

from Ui.Ui_DialogCardEdit import Ui_DialogCardEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from cardClass import readCardClasses, readCardClass, CardClass
from Ui.Ui_DialogCardEditDetail_Window import DialogCardEditDetail_Window


class DialogCardEdit_Window(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_DialogCardEdit()
        self.ui.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setTableView()
        self.ui.pushButtonEdit.clicked.connect(self.buttonEditClicked)
        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.ui.pushButtonAddNew.clicked.connect(self.buttonAddNewClicked)

    def setTableView(self):
        cardClasses = readCardClasses()
        self.model = QtGui.QStandardItemModel(len(cardClasses), 3)
        self.model.setHorizontalHeaderLabels(['卡类编号', '卡类名称', '卡类描述'])
        num = 0
        for cardClass in cardClasses.values():
            self.model.setItem(
                num, 0, QtGui.QStandardItem(str(cardClass.cardClassNum)))
            self.model.setItem(num, 1,
                               QtGui.QStandardItem(cardClass.cardClassName))
            self.model.setItem(
                num, 2, QtGui.QStandardItem(cardClass.cardClassDescription))
            num += 1
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

    def buttonEditClicked(self):
        selectCardClassNum = self.model.data(
            self.model.index(self.ui.tableView.currentIndex().row(), 0))
        selectCardClass = readCardClass(selectCardClassNum)
        self.dialogCardEditDetail = DialogCardEditDetail_Window(
            selectCardClass, self)
        self.dialogCardEditDetail.show()

    def buttonAddNewClicked(self):
        self.dialogCardEditDetail = DialogCardEditDetail_Window(
            CardClass(), self)
        self.dialogCardEditDetail.show()
