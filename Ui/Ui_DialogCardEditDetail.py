# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Coding\Projects\BeautyManager\Ui\DialogCardEditDetail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogCardEditDetail(object):
    def setupUi(self, DialogCardEditDetail):
        DialogCardEditDetail.setObjectName("DialogCardEditDetail")
        DialogCardEditDetail.resize(778, 720)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(DialogCardEditDetail)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DialogCardEditDetail)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_cardNum = QtWidgets.QLabel(DialogCardEditDetail)
        self.label_cardNum.setObjectName("label_cardNum")
        self.horizontalLayout_2.addWidget(self.label_cardNum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(DialogCardEditDetail)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_cardName = QtWidgets.QLineEdit(DialogCardEditDetail)
        self.lineEdit_cardName.setObjectName("lineEdit_cardName")
        self.horizontalLayout_3.addWidget(self.lineEdit_cardName)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(DialogCardEditDetail)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.tableView_cardStrategy = QtWidgets.QTableView(DialogCardEditDetail)
        self.tableView_cardStrategy.setObjectName("tableView_cardStrategy")
        self.verticalLayout.addWidget(self.tableView_cardStrategy)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(DialogCardEditDetail)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.textEdit_cardDescription = QtWidgets.QTextEdit(DialogCardEditDetail)
        self.textEdit_cardDescription.setObjectName("textEdit_cardDescription")
        self.verticalLayout.addWidget(self.textEdit_cardDescription)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonOk = QtWidgets.QPushButton(DialogCardEditDetail)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogCardEditDetail)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(DialogCardEditDetail)
        QtCore.QMetaObject.connectSlotsByName(DialogCardEditDetail)

    def retranslateUi(self, DialogCardEditDetail):
        _translate = QtCore.QCoreApplication.translate
        DialogCardEditDetail.setWindowTitle(_translate("DialogCardEditDetail", "卡类设置"))
        self.label.setText(_translate("DialogCardEditDetail", "卡类编号："))
        self.label_cardNum.setText(_translate("DialogCardEditDetail", "Num"))
        self.label_3.setText(_translate("DialogCardEditDetail", "卡类名称："))
        self.lineEdit_cardName.setText(_translate("DialogCardEditDetail", "cardName"))
        self.label_5.setText(_translate("DialogCardEditDetail", "卡类优惠："))
        self.label_4.setText(_translate("DialogCardEditDetail", "卡类描述："))
        self.textEdit_cardDescription.setHtml(_translate("DialogCardEditDetail", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">cardDescription</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonOk.setText(_translate("DialogCardEditDetail", "确定"))
        self.pushButtonCancel.setText(_translate("DialogCardEditDetail", "取消"))
