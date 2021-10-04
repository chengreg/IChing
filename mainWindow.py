# -*- coding: utf-8 -*-
# @Time    : 2021/10/1 16:27
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : mainWindow.py
# @Software: PyCharm

from PySide6.QtWidgets import QMainWindow, QMdiArea
from UiRes.ui_main import Ui_MainWindow
from numberDialog import NumberDialog
from numberTo64 import NumberTo64


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.number_dialog = NumberDialog()
        self.number_dialog.sendDataSignal.connect(self.acceptDivDialogSignal)

        self.setupUi(self)
        self.initGui()

    def acceptDivDialogSignal(self, dataDict):
        print("从占卦界面获得的数据：",dict)


        from contentAera import ContentAearWindow
        cAera = ContentAearWindow()

        cAera.setWindowTitle(dataDict["name"])
        cAera.textBrowser.append(f"姓名：{dataDict['name']} \n")
        cAera.textBrowser.insertPlainText(f"性别：{dataDict['sex']} \n")
        cAera.textBrowser.insertPlainText(f"出生日期：{dataDict['birthday']} \n")
        cAera.textBrowser.insertPlainText(f"占事：{dataDict['what']} \n")

        result = NumberTo64(dataDict["num1"], dataDict["num2"], dataDict["num3"]).result()
        print(result)
        cAera.textBrowser.insertPlainText(f"第{str(result['卦序'])}卦  {result['卦名']} \n")

        self.mdiArea.addSubWindow(cAera)

        cAera.show()

    def initGui(self):
        # 窗口设置
        self.resize(1600, 1200)
        # 菜单信号

        # 菜单：占卦
        self.actionNum.triggered.connect(self.on_actionNum_triggered)
        self.actionMoney.triggered.connect(self.on_actionMoney_triggered)

        # 菜单：窗口
        self.actionTile.triggered.connect(self.on_actionTile_triggered)
        self.actionCascade.triggered.connect(self.on_actionCascade_triggered)
        self.actionTab.triggered.connect(self.on_actionTab_triggered)
        self.actioncloseAllSubWindows.triggered.connect(lambda: self.mdiArea.closeAllSubWindows())

    def on_actionMoney_triggered(self):
        pass

    def on_actionNum_triggered(self):
        self.number_dialog.exec()

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


