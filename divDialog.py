# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 2:22
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : divDialog.py
# @Software: PyCharm
import sys
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtCore import *
from UiRes.ui_divDialog import Ui_Dialog


class DivDialog(QDialog, Ui_Dialog):
    def __init__(self, *args, **kwargs):
        super(DivDialog, self).__init__(*args, **kwargs)

        self.setupUi(self)
        self.initGui()

    def initGui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = DivDialog()
    window.show()
    sys.exit(app.exec())
