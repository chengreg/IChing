# -*- coding: utf-8 -*-
# @Time    : 2021/10/2 2:22
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : divDialog.py
# @Software: PyCharm

from PySide6.QtWidgets import QDialog, QButtonGroup, QMessageBox, QCheckBox, QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QIntValidator
from UiRes.ui_divDialog import Ui_Dialog


class NumberVlidator(QIntValidator):
    pass

class DivDialog(QDialog, Ui_Dialog):
    # 发送对话框内数据在信号，数据格式为字典dict
    sendDataSignal = Signal(dict)

    def __init__(self, *args, **kwargs):
        super(DivDialog, self).__init__(*args, **kwargs)


        self.setupUi(self)

        # 设置UI
        self.initGui()

    def initGui(self):
        self.setWindowTitle("占卦")

        # 性别的按钮组
        self.sexGroup = QButtonGroup(self)
        self.sexGroup.addButton(self.radioButtonMan, 1)
        self.sexGroup.addButton(self.radioButtonWoman, 2)

        # 设置数字卦的三个lineEdit
        self.lineEdit_num1.setValidator(QIntValidator(100,999))
        self.lineEdit_num2.setValidator(QIntValidator(100, 999))
        self.lineEdit_num3.setValidator(QIntValidator(100,999))

        # 查看结果的信号
        self.pushButtonOK.clicked.connect(self.on_pushButtonOK_clicked)

    def on_pushButtonOK_clicked(self):
        if self.sexGroup.checkedId() == -1:
            print("没有任何选中")
            self.messageBoxTips()

            return
        # 获取窗口数据并添加到字典中
        name = self.lineEditName.text()
        sex = self.sexGroup.checkedButton().text()
        dataDict = {"name": name, "sex": sex}

        # 发送信号
        self.sendDataSignal.emit(dataDict)

        # 关闭窗口
        self.close()




    def messageBoxTips(self):
        mb = QMessageBox(self)
        mb.setIconPixmap(QPixmap("images/div_messagebox_pic.png").scaled(200, 200))
        mb.setWindowTitle("未设置性别")
        mb.setText("<h2>您忘记设置占卦对象的性别了哦</h2>")
        mb.setInformativeText("设置性别更有利于区分不同的用户，未来还会推出更多根据不同性别的不同设置")
        mb.setCheckBox(QCheckBox("下次不再提示！", mb))
        mb.setDetailedText("必须设置性别才可以使用")

        btn1 = QPushButton("设置为男", mb)
        btn2 = QPushButton("设置为女", mb)
        mb.addButton(btn1, QMessageBox.YesRole)
        mb.addButton(btn2, QMessageBox.YesRole)

        mb.setDefaultButton(btn1)
        mb.setEscapeButton(btn1)

        # 自定义按钮的信号，判断按钮类型，设置男女的RadioButton选中状态
        mb.buttonClicked.connect(
            lambda btn: self.radioButtonMan.setChecked(True) if btn == btn1 else self.radioButtonWoman.setChecked(True))

        mb.show()

