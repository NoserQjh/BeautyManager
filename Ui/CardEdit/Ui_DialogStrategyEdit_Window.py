'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-08 17:04:00
@Description:
'''

from Ui.CardEdit.Ui_DialogStrategyEdit import Ui_DialogStrategyEdit
from PyQt5 import QtCore, QtGui, QtWidgets

import sys

from strategy import strategyNum2Name, strategyNum2Params


class DialogStrategyEdit_Window(QtWidgets.QDialog):
    def __init__(self, parent, strategies, index):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_DialogStrategyEdit()
        self.ui.setupUi(self)

        self.parent = parent
        self.strategies = strategies
        self.strategyIndex = index
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.setComboBox()
        if self.strategyIndex >= 0:
            self.ui.plainTextEdit.setPlainText(
                self.strategies[self.strategyIndex].get('strategyDescription'))
        else:
            self.ui.plainTextEdit.setPlainText('请在此输入优惠描述')
        self.ui.pushButtonOk.clicked.connect(self.buttonOkClicked)

    def setComboBox(self):
        for i in range(len(strategyNum2Name.keys())):
            self.ui.comboBox.addItem(strategyNum2Name.get(i))
        if self.strategyIndex >= 0:
            self.ui.comboBox.setCurrentIndex(
                self.strategies[self.strategyIndex].get('strategyNum'))
        self.setTableView()
        self.ui.comboBox.currentIndexChanged.connect(self.setTableView)

    def setTableView(self):
        params = strategyNum2Params.get(self.ui.comboBox.currentIndex())
        self.model = QtGui.QStandardItemModel(1, len(params))
        self.model.setHorizontalHeaderLabels(params)
        if self.ui.comboBox.currentIndex() == self.strategyIndex:
            for i in range(len(params)):
                self.model.setItem(
                    0, i,
                    QtGui.QStandardItem(
                        str(self.strategies[self.strategyIndex].get(
                            'strategyParams')[i])))
        else:
            for i in range(len(params)):
                self.model.setItem(0, i, QtGui.QStandardItem('0'))
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.verticalHeader().hide()
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)

    def buttonOkClicked(self):
        strategyNum = self.ui.comboBox.currentIndex()
        params = strategyNum2Params.get(strategyNum)
        strategyParams = []
        legalInput = True
        for i in range(len(params)):
            try:
                strategyParams.append(
                    float(self.model.data(self.model.index(0, i))))
            except:
                QtWidgets.QMessageBox.warning(self, '非法输入', '输入优惠参数不符合规则')
        strategyDescription = self.ui.plainTextEdit.toPlainText()
        if self.strategyIndex >= 0:
            self.strategies[self.strategyIndex] = {
                'strategyNum': strategyNum,
                'strategyParams': strategyParams,
                'strategyDescription': strategyDescription
            }
        else:
            self.strategies.append({
                'strategyNum': strategyNum,
                'strategyParams': strategyParams,
                'strategyDescription': strategyDescription
            })
        self.parent.setTableView()
        self.close()
