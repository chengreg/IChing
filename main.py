# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:27
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : main.py
# @Software: PyCharm
import sys
from PySide6.QtWidgets import *
from UiRes.ui_main import Ui_MainWindow
from content import Content
from divDialog import DivDialog


class Window(QMainWindow, Ui_MainWindow):
    def __init__(self, *args, **kwargs):
        super(Window, self).__init__(*args, **kwargs)

        self.div_dialog = DivDialog()

        self.setupUi(self)
        self.initGui()

    def initGui(self):
        # 窗口设置
        self.resize(800, 600)
        # 菜单信号
        self.actionNew.triggered.connect(self.on_actionNew_triggered) # 测试
        self.actionOpen.triggered.connect(self.on_actionOpen_triggered) # 测试
        self.actionTile.triggered.connect(self.on_actionTile_triggered)
        self.actionCascade.triggered.connect(self.on_actionCascade_triggered)
        self.actionTab.triggered.connect(self.on_actionTab_triggered)
        self.actioncloseAllSubWindows.triggered.connect(lambda: self.mdiArea.closeAllSubWindows())

    def on_actionNew_triggered(self):
        content_pane = Content(self)
        self.mdiArea.addSubWindow()
        content_pane.show()

    def on_actionOpen_triggered(self):
        self.div_dialog.exec()

    def on_actionTile_triggered(self, checked: bool):
        self.actionTile.setChecked(True)
        self.actionCascade.setChecked(False)
        if checked:
            self.mdiArea.tileSubWindows()

    def on_actionCascade_triggered(self, checked: bool):
        self.actionCascade.setChecked(True)
        self.actionTile.setChecked(False)
        if checked:
            self.mdiArea.cascadeSubWindows()

    def on_actionTab_triggered(self, checked: bool):
        if checked:
            self.mdiArea.setViewMode(QMdiArea.TabbedView)
        else:
            self.mdiArea.setViewMode(QMdiArea.SubWindowView)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Window()
    window.show()
    sys.exit(app.exec())
