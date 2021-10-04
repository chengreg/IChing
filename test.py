# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 12:01
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : test.py
# @Software: PyCharm

import sys
from PySide6.QtWidgets import QApplication, QWidget


class Window(QWidget):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.resize(800, 600)
        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
