# -*- coding: utf-8 -*-
# @Time    : 2021/10/4 20:17
# @Author  : Chen GangQiang
# @Email   : uoaoo@163.com
# @File    : numberDialog.py
# @Software: PyCharm
from PySide6.QtWidgets import QDialog, QButtonGroup, QMessageBox, QCheckBox, QPushButton
from PySide6.QtCore import Signal
from PySide6.QtGui import QPixmap, QIntValidator
from UiRes.ui_NumberDialog import Ui_Dialog


class NumberDialog(QDialog, Ui_Dialog):
    # 发送对话框内数据在信号，数据格式为字典dict
    sendDataSignal = Signal(dict)

    def __init__(self, *args, **kwargs):
        super(NumberDialog, self).__init__(*args, **kwargs)

        # 空字典，用于存储界面上获取的数据
        self.dictData = {"name": "未知", "sex": "未知", "what":"", "birthday":"", "num1":0, "num2":0, "num3":0}
        # 性别的按钮组
        self.sexGroup = QButtonGroup(self)

        # 设置UI
        self.setupUi(self)
        self.initGui()

    def initGui(self):
        self.setWindowTitle("占卦")

        # 性别的按钮组
        self.sexGroup.addButton(self.radioButtonMan, 1)
        self.sexGroup.addButton(self.radioButtonWoman, 2)

        # 设置数字卦的三个lineEdit
        self.lineEdit_num1.setValidator(QIntValidator(100, 999))
        self.lineEdit_num2.setValidator(QIntValidator(100, 999))
        self.lineEdit_num3.setValidator(QIntValidator(100, 999))


        # 查看结果的信号
        self.pushButtonOK.clicked.connect(self.on_pushButtonOK_clicked)

    def on_pushButtonOK_clicked(self):
        """查看结果按钮的槽函数"""
        # 判断界面上的控件内容
        if self.lineEditName.text() == "":
            result = QMessageBox.warning(self, "姓名不能为空", "请输入姓名", QMessageBox.Ok)
            self.lineEditName.setFocus()
            if result == QMessageBox.Ok:
                return
        if self.sexGroup.checkedId() == -1:
            self.messageBoxTips()
            return

        # 发送信号
        self.sendDataSignal.emit(self.getUIDataToDict())

        # 清空控件中的数据
        self.lineEditName.clear()
        self.plainTextEditWhat.clear()
        self.lineEdit_num1.clear()
        self.lineEdit_num2.clear()
        self.lineEdit_num3.clear()

        # 关闭窗口
        self.close()


    def messageBoxTips(self):
        """如果没有选择性别，则弹出该对话框（学习对话框专用）"""
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

    def getUIDataToDict(self):
        """
        从UI上获取数据，并保存到字典中
        :return: 字典
        """
        self.dictData["name"] = self.lineEditName.text()
        self.dictData["sex"] = self.sexGroup.checkedButton().text()
        self.dictData["what"] = self.plainTextEditWhat.toPlainText()
        self.dictData["birthday"] = self.dateEditBirthday.date().toString("yyyy-MM-dd")
        if self.lineEdit_num1.text() == "":
            self.lineEdit_num1.setText("0")
        if self.lineEdit_num2.text() == "":
            self.lineEdit_num2.setText("0")
        if self.lineEdit_num3.text() == "":
            self.lineEdit_num3.setText("0")
        self.dictData["num1"] = int(self.lineEdit_num1.text())
        self.dictData["num2"] = int(self.lineEdit_num2.text())
        self.dictData["num3"] = int(self.lineEdit_num3.text())

        return self.dictData
