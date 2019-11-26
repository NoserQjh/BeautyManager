'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:55:41
@LastEditTime: 2019-11-26 18:37:55
@Description:
'''

from Ui.ProductEdit.Ui_DialogProductEditDetail import Ui_DialogProductEditDetail
from PyQt5 import QtCore, QtGui, QtWidgets

import sys
import json
import copy
import time

from Class.product import writeProduct, readProductIndex, writeProductIndex, product2Dict


class DialogProductEditDetail_Window(QtWidgets.QDialog):
    def __init__(self, product, fatherWindow):
        QtWidgets.QDialog.__init__(self)

        self.product = product
        self.productBackup = copy.deepcopy(product)
        self.fatherWindow = fatherWindow

        self.ui = Ui_DialogProductEditDetail()
        self.ui.setupUi(self)
        _translate = QtCore.QCoreApplication.translate
        self.ui.label_productNum.setText(
            _translate("DialogCardEditDetail", str(product.productNum)))

        self.ui.lineEdit_productName.setText(
            _translate("DialogCardEditDetail", product.productName))
        self.ui.lineEdit_productCost.setText(
            _translate("DialogCardEditDetail", str(product.productCost)))

        self.ui.textEdit_productDescription.setPlainText(
            _translate("DialogCardEditDetail", product.productDescription))

        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.ui.pushButtonOk.clicked.connect(self.buttonOkClicked)

    def buttonOkClicked(self):
        self.product.productName = self.ui.lineEdit_productName.text()

        self.product.productDescription = self.ui.textEdit_productDescription.toPlainText(
        )
        try:
            self.product.productCost = float(
                self.ui.lineEdit_productCost.text())
        except:
            QtWidgets.QMessageBox.warning(self, '非法输入', '输入价格不符合规则')
            return
        changed = False
        if self.productBackup.productName != self.product.productName:
            changed = True
        if self.productBackup.productCost != self.product.productCost:
            changed = True
        if self.productBackup.productDescription != self.product.productDescription:
            changed = True
        if changed:
            writeProduct(self.product)
            index = readProductIndex()
            index[str(self.product.productNum)] = self.product.productName
            writeProductIndex(index)
            log = {
                'Type': 'ProductEdit',
                'Backup': product2Dict(self.productBackup),
                'New': product2Dict(self.product),
                'Time': time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
            }
            with open(
                    './Logs/' + str(time.time()).replace('.', '') +
                    '_ProductEdit.json', 'w') as outfile:
                json.dump(log, outfile)
        self.fatherWindow.setTableView()
        self.close()
