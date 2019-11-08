'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-08 17:06:21
@Description:
'''

from Ui.CardEdit.Ui_DialogCardEditDetail import Ui_DialogCardEditDetail
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import json

from cardClass import writeCardClass
from cardClass import readCardClassIndex, writeCardClassIndex
from strategy import strategyNum2Name

from Ui.CardEdit.Ui_DialogStrategyEdit_Window import DialogStrategyEdit_Window


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
        self.setTableView()

        self.ui.pushButton_StrategyAdd.clicked.connect(
            self.buttonAddStrategyClicked)
        self.ui.pushButton_StrategyEdit.clicked.connect(
            self.buttonEditStrategyClicked)
        self.ui.pushButton_StrategyDelete.clicked.connect(
            self.buttonDeleteStrategyClicked)
        self.ui.tableView_cardStrategy.doubleClicked.connect(self.buttonEditStrategyClicked)

    def setTableView(self):
        strategies = self.cardClass.cardClassStrategies
        self.model = QtGui.QStandardItemModel(len(strategies), 3)
        self.model.setHorizontalHeaderLabels(['优惠名称', '优惠描述', '优惠参数'])
        num = 0
        for strategy in strategies:
            self.model.setItem(
                num, 0,
                QtGui.QStandardItem(
                    strategyNum2Name.get(strategy.get('strategyNum'))))
            self.model.setItem(
                num, 1, QtGui.QStandardItem(
                    strategy.get('strategyDescription')))
            self.model.setItem(
                num, 2,
                QtGui.QStandardItem(
                    json.dumps(strategy.get('strategyParams'))))
            num += 1
        self.ui.tableView_cardStrategy.setModel(self.model)
        self.ui.tableView_cardStrategy.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.tableView_cardStrategy.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView_cardStrategy.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    def buttonAddStrategyClicked(self):
        self.dialogStrategyEdit = DialogStrategyEdit_Window(self,
            self.cardClass.cardClassStrategies, -1)
        self.dialogStrategyEdit.show()

    def buttonEditStrategyClicked(self):
        selectStrategy = self.ui.tableView_cardStrategy.currentIndex().row()
        self.dialogStrategyEdit = DialogStrategyEdit_Window(self,
            self.cardClass.cardClassStrategies, selectStrategy)
        self.dialogStrategyEdit.show()

    def buttonDeleteStrategyClicked(self):
        selectStrategy = self.ui.tableView_cardStrategy.currentIndex().row()
        self.cardClass.cardClassStrategies.pop(selectStrategy)
        self.setTableView()

    def buttonOkClicked(self):
        self.cardClass.cardClassName = self.ui.lineEdit_cardName.text()
        self.cardClass.cardClassDescription = self.ui.textEdit_cardDescription.toPlainText(
        )
        writeCardClass(self.cardClass)
        index = readCardClassIndex()
        index[str(
            self.cardClass.cardClassNum)] = self.cardClass.cardClassDescription
        writeCardClassIndex(index)
        self.fatherWindow.setTableView()
        self.close()
