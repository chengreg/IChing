# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 14:44
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : contentAera.py
# @Software: PyCharm

import sys
from PySide6.QtWidgets import QWidget, QApplication
from UiRes.ui_content import Ui_Form


class ContentAearWindow(QWidget, Ui_Form):
    def __init__(self, *args, **kwargs):
        super(ContentAearWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)

        self.setup_ui()

    def setup_ui(self):
        pass


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ContentAearWindow()
    window.show()
    sys.exit(app.exec())
