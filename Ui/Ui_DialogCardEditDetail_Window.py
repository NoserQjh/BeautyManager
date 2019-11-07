'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-07 11:02:29
@Description:
'''

from Ui.Ui_DialogCardEditDetail import Ui_DialogCardEditDetail
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from cardClass import writeCardClass
from cardClass import readCardClassIndex, writeCardClassIndex


class DialogCardEditDetail_Window(QtWidgets.QDialog):
    def __init__(self, cardClass, fatherWindow):
        QtWidgets.QDialog.__init__(self)

        self.cardClass = cardClass
        self.fatherWindow = fatherWindow

        self.ui = Ui_DialogCardEditDetail()
        self.ui.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.ui.label_cardNum.setText(
            _translate("DialogCardEditDetail", str(cardClass.cardClassNum)))
        self.ui.lineEdit_cardName.setText(
            _translate("DialogCardEditDetail", cardClass.cardClassName))
        self.ui.textEdit_cardDescription.setPlainText(
            _translate("DialogCardEditDetail", cardClass.cardClassDescription))
        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.ui.pushButtonOk.clicked.connect(self.buttonOkClicked)

    def buttonOkClicked(self):
        self.cardClass.cardClassName = self.ui.lineEdit_cardName.text()
        self.cardClass.cardClassDescription = self.ui.textEdit_cardDescription.toPlainText(
        )
        writeCardClass(self.cardClass)
        index = readCardClassIndex()
        index[str(self.cardClass.cardClassNum)]=self.cardClass.cardClassDescription
        writeCardClassIndex(index)
        self.fatherWindow.setTableView()
        self.close()
