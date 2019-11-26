'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-26 16:04:35
@LastEditTime: 2019-11-26 17:46:39
@Description:
'''

from Ui.ProductEdit.Ui_DialogProductEdit import Ui_DialogProductEdit
from PyQt5 import QtCore, QtGui, QtWidgets
import sys

from Class.product import readProducts, readProduct, Product
from Ui.ProductEdit.Ui_DialogProductEditDetail_Window import DialogProductEditDetail_Window


class DialogProductEdit_Window(QtWidgets.QDialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ui = Ui_DialogProductEdit()
        self.ui.setupUi(self)
        # self.setWindowFlags(QtCore.Qt.WindowStaysOnTopHint)
        self.setTableView()
        self.ui.pushButtonEdit.clicked.connect(self.buttonEditClicked)
        self.ui.pushButtonCancel.clicked.connect(self.close)
        self.ui.pushButtonAddNew.clicked.connect(self.buttonAddNewClicked)
        self.ui.tableView.doubleClicked.connect(self.buttonEditClicked)

    def setTableView(self):
        pass
        products = readProducts()
        self.model = QtGui.QStandardItemModel(len(products), 4)
        self.model.setHorizontalHeaderLabels(['项目编号', '项目名称', '项目描述', '项目价格'])
        num = 0
        for product in products.values():
            self.model.setItem(num, 0,
                               QtGui.QStandardItem(str(product.productNum)))
            self.model.setItem(num, 1,
                               QtGui.QStandardItem(product.productName))
            self.model.setItem(num, 2,
                               QtGui.QStandardItem(product.productDescription))
            self.model.setItem(num, 3,
                               QtGui.QStandardItem(str(product.productCost)))
            num += 1
        self.ui.tableView.setModel(self.model)
        self.ui.tableView.horizontalHeader().setSectionResizeMode(
            QtWidgets.QHeaderView.Stretch)
        self.ui.tableView.setSelectionBehavior(
            QtWidgets.QAbstractItemView.SelectRows)
        self.ui.tableView.setEditTriggers(
            QtWidgets.QAbstractItemView.NoEditTriggers)

    def buttonEditClicked(self):
        selectProductNum = self.model.data(
            self.model.index(self.ui.tableView.currentIndex().row(), 0))
        selectProduct = readProduct(selectProductNum)
        self.dialogProductEditDetail = DialogProductEditDetail_Window(
            selectProduct, self)
        self.dialogProductEditDetail.show()

    def buttonAddNewClicked(self):
        self.dialogProductEditDetail = DialogProductEditDetail_Window(
            Product(), self)
        self.dialogProductEditDetail.show()
