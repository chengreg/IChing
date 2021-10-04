# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 11:59
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : main.py
# @Software: PyCharm
import sys
from PySide6.QtWidgets import QApplication
from mainWindow import MainWindow


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())