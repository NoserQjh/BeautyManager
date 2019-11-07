# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Coding\Projects\BeautyManager\Ui\DialogCardEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCardEdit(object):
    def setupUi(self, DialogCardEdit):
        DialogCardEdit.setObjectName("DialogCardEdit")
        DialogCardEdit.resize(646, 548)
        self.gridLayout = QtWidgets.QGridLayout(DialogCardEdit)
        self.gridLayout.setObjectName("gridLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(DialogCardEdit)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAddNew = QtWidgets.QPushButton(DialogCardEdit)
        self.pushButtonAddNew.setAutoDefault(False)
        self.pushButtonAddNew.setObjectName("pushButtonAddNew")
        self.horizontalLayout_2.addWidget(self.pushButtonAddNew)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButtonEdit = QtWidgets.QPushButton(DialogCardEdit)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogCardEdit)
        self.pushButtonCancel.setAutoDefault(True)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.retranslateUi(DialogCardEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogCardEdit)

    def retranslateUi(self, DialogCardEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogCardEdit.setWindowTitle(_translate("DialogCardEdit", "卡类设置"))
        self.pushButtonAddNew.setText(_translate("DialogCardEdit", "添加新卡种"))
        self.pushButtonEdit.setText(_translate("DialogCardEdit", "编辑"))
        self.pushButtonCancel.setText(_translate("DialogCardEdit", "取消"))
