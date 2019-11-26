# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'd:\Documents\Coding\Projects\BeautyManager\Ui\ProductEdit\DialogProductEditDetail.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DialogProductEditDetail(object):
    def setupUi(self, DialogProductEditDetail):
        DialogProductEditDetail.setObjectName("DialogProductEditDetail")
        DialogProductEditDetail.resize(523, 349)
        self.verticalLayout = QtWidgets.QVBoxLayout(DialogProductEditDetail)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label = QtWidgets.QLabel(DialogProductEditDetail)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.label_productNum = QtWidgets.QLabel(DialogProductEditDetail)
        self.label_productNum.setObjectName("label_productNum")
        self.horizontalLayout_2.addWidget(self.label_productNum)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.label_3 = QtWidgets.QLabel(DialogProductEditDetail)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_3.addWidget(self.label_3)
        self.lineEdit_productName = QtWidgets.QLineEdit(DialogProductEditDetail)
        self.lineEdit_productName.setObjectName("lineEdit_productName")
        self.horizontalLayout_3.addWidget(self.lineEdit_productName)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_3.addItem(spacerItem1)
        self.verticalLayout.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.label_5 = QtWidgets.QLabel(DialogProductEditDetail)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout_5.addWidget(self.label_5)
        self.lineEdit_productCost = QtWidgets.QLineEdit(DialogProductEditDetail)
        self.lineEdit_productCost.setObjectName("lineEdit_productCost")
        self.horizontalLayout_5.addWidget(self.lineEdit_productCost)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_5.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout_5)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.label_4 = QtWidgets.QLabel(DialogProductEditDetail)
        self.label_4.setObjectName("label_4")
        self.horizontalLayout_4.addWidget(self.label_4)
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem3)
        self.verticalLayout.addLayout(self.horizontalLayout_4)
        self.textEdit_productDescription = QtWidgets.QTextEdit(DialogProductEditDetail)
        self.textEdit_productDescription.setObjectName("textEdit_productDescription")
        self.verticalLayout.addWidget(self.textEdit_productDescription)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem4 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem4)
        self.pushButtonOk = QtWidgets.QPushButton(DialogProductEditDetail)
        self.pushButtonOk.setObjectName("pushButtonOk")
        self.horizontalLayout.addWidget(self.pushButtonOk)
        self.pushButtonCancel = QtWidgets.QPushButton(DialogProductEditDetail)
        self.pushButtonCancel.setObjectName("pushButtonCancel")
        self.horizontalLayout.addWidget(self.pushButtonCancel)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.retranslateUi(DialogProductEditDetail)
        QtCore.QMetaObject.connectSlotsByName(DialogProductEditDetail)

    def retranslateUi(self, DialogProductEditDetail):
        _translate = QtCore.QCoreApplication.translate
        DialogProductEditDetail.setWindowTitle(_translate("DialogProductEditDetail", "Dialog"))
        self.label.setText(_translate("DialogProductEditDetail", "项目编号："))
        self.label_productNum.setText(_translate("DialogProductEditDetail", "Num"))
        self.label_3.setText(_translate("DialogProductEditDetail", "项目名称："))
        self.lineEdit_productName.setText(_translate("DialogProductEditDetail", "productName"))
        self.label_5.setText(_translate("DialogProductEditDetail", "项目价格："))
        self.lineEdit_productCost.setText(_translate("DialogProductEditDetail", "productCost"))
        self.label_4.setText(_translate("DialogProductEditDetail", "项目描述："))
        self.textEdit_productDescription.setHtml(_translate("DialogProductEditDetail", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">productDescription</p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>"))
        self.pushButtonOk.setText(_translate("DialogProductEditDetail", "确定"))
        self.pushButtonCancel.setText(_translate("DialogProductEditDetail", "取消"))
