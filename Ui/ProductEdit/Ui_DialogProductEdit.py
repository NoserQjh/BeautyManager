# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Coding\Projects\BeautyManager\Ui\ProductEdit\DialogProductEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogProductEdit(object):
    def setupUi(self, DialogProductEdit):
        DialogProductEdit.setObjectName("DialogProductEdit")
        DialogProductEdit.resize(647, 548)
        DialogProductEdit.setContextMenuPolicy(QtCore.Qt.NoContextMenu)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogProductEdit)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.tableView = QtWidgets.QTableView(DialogProductEdit)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.pushButtonAddNew = QtWidgets.QPushButton(DialogProductEdit)
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
        self.pushButtonEdit = QtWidgets.QPushButton(DialogProductEdit)
        self.pushButtonEdit.setObjectName("pushButtonEdit")
        self.horizontalLayout.addWidget(self.pushButtonEdit)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogProductEdit)
        self.pushButtonCancel.setAutoDefault(True)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogProductEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogProductEdit)

    def retranslateUi(self, DialogProductEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogProductEdit.setWindowTitle(_translate("DialogProductEdit", "项目设置"))
        self.pushButtonAddNew.setText(_translate("DialogProductEdit", "添加新项目"))
        self.pushButtonEdit.setText(_translate("DialogProductEdit", "编辑"))
        self.pushButtonCancel.setText(_translate("DialogProductEdit", "取消"))
