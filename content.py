# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 23:10
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : content.py
# @Software: PyCharm

import sys
from PySide6.QtWidgets import *
from UiRes.ui_content import Ui_Form


class Content(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(Content, self).__init__(*args, **kwargs)

        self.resize(800, 600)
        self.setup_ui()
        self.setupUi(self)

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Content()
    window.show()
    sys.exit(app.exec())
