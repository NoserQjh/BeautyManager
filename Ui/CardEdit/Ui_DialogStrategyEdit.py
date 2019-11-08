# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Coding\Projects\BeautyManager\Ui\CardEdit\DialogStrategyEdit.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogStrategyEdit(object):
    def setupUi(self, DialogStrategyEdit):
        DialogStrategyEdit.setObjectName("DialogStrategyEdit")
        DialogStrategyEdit.resize(334, 357)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogStrategyEdit)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(DialogStrategyEdit)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_cardNum = QtWidgets.QLabel(DialogStrategyEdit)
        self.label_cardNum.setObjectName("label_cardNum")
        self.horizontalLayout_2.addWidget(self.label_cardNum)
        self.comboBox = QtWidgets.QComboBox(DialogStrategyEdit)
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_2.addWidget(self.comboBox)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_3 = QtWidgets.QLabel(DialogStrategyEdit)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_5.addWidget(self.label_3)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableView = QtWidgets.QTableView(DialogStrategyEdit)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_2 = QtWidgets.QLabel(DialogStrategyEdit)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.plainTextEdit = QtWidgets.QPlainTextEdit(DialogStrategyEdit)
        self.plainTextEdit.setObjectName("plainTextEdit")
        self.verticalLayout.addWidget(self.plainTextEdit)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.pushButtonOk = QtWidgets.QPushButton(DialogStrategyEdit)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout_4.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogStrategyEdit)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout_4.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.retranslateUi(DialogStrategyEdit)
        QtCore.QMetaObject.connectSlotsByName(DialogStrategyEdit)

    def retranslateUi(self, DialogStrategyEdit):
        _translate = QtCore.QCoreApplication.translate
        DialogStrategyEdit.setWindowTitle(_translate("DialogStrategyEdit", "优惠编辑"))
        self.label.setText(_translate("DialogStrategyEdit", "优惠方式："))
        self.label_cardNum.setText(_translate("DialogStrategyEdit", "优惠类型："))
        self.label_3.setText(_translate("DialogStrategyEdit", "优惠参数："))
        self.label_2.setText(_translate("DialogStrategyEdit", "优惠描述："))
        self.pushButtonOk.setText(_translate("DialogStrategyEdit", "确定"))
        self.pushButtonCancel.setText(_translate("DialogStrategyEdit", "取消"))
