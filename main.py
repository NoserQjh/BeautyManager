'''
@Author: NoserQJH
@LastEditors: NoserQJH
@Date: 2019-11-05 18:22:26
@LastEditTime: 2019-11-05 20:53:02
@Description:
'''

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from Ui.Ui_MainWindowIndex_Window import MainWindowIndex_window


def main():
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindowIndex_window()
    window.showMaximized()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
