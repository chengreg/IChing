# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_divDialog.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import rc_rc

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(685, 681)
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.groupBox = QGroupBox(Dialog)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setMinimumSize(QSize(0, 140))
        self.groupBox.setMaximumSize(QSize(16777215, 140))
        self.verticalLayout = QVBoxLayout(self.groupBox)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(6)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.groupBox)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.lineEditName = QLineEdit(self.groupBox)
        self.lineEditName.setObjectName(u"lineEditName")

        self.horizontalLayout.addWidget(self.lineEditName)

        self.label_2 = QLabel(self.groupBox)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout.addWidget(self.label_2)

        self.radioButtonMan = QRadioButton(self.groupBox)
        self.radioButtonMan.setObjectName(u"radioButtonMan")

        self.horizontalLayout.addWidget(self.radioButtonMan)

        self.radioButtonWoman = QRadioButton(self.groupBox)
        self.radioButtonWoman.setObjectName(u"radioButtonWoman")

        self.horizontalLayout.addWidget(self.radioButtonWoman)

        self.label_3 = QLabel(self.groupBox)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout.addWidget(self.label_3)

        self.dateEditBirthday = QDateEdit(self.groupBox)
        self.dateEditBirthday.setObjectName(u"dateEditBirthday")

        self.horizontalLayout.addWidget(self.dateEditBirthday)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.label_4 = QLabel(self.groupBox)
        self.label_4.setObjectName(u"label_4")

        self.gridLayout.addWidget(self.label_4, 0, 0, 1, 1)

        self.plainTextEditWhat = QPlainTextEdit(self.groupBox)
        self.plainTextEditWhat.setObjectName(u"plainTextEditWhat")

        self.gridLayout.addWidget(self.plainTextEditWhat, 0, 1, 2, 1)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer, 1, 0, 1, 1)


        self.verticalLayout.addLayout(self.gridLayout)


        self.verticalLayout_2.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(Dialog)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setMinimumSize(QSize(0, 170))
        self.groupBox_2.setMaximumSize(QSize(16777215, 170))
        self.verticalLayout_3 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.tabWidget = QTabWidget(self.groupBox_2)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabNumber = QWidget()
        self.tabNumber.setObjectName(u"tabNumber")
        self.verticalLayout_4 = QVBoxLayout(self.tabNumber)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.gridLayout_2 = QGridLayout()
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.label_5 = QLabel(self.tabNumber)
        self.label_5.setObjectName(u"label_5")

        self.gridLayout_2.addWidget(self.label_5, 0, 0, 1, 1)

        self.label_7 = QLabel(self.tabNumber)
        self.label_7.setObjectName(u"label_7")

        self.gridLayout_2.addWidget(self.label_7, 2, 0, 1, 1)

        self.label_6 = QLabel(self.tabNumber)
        self.label_6.setObjectName(u"label_6")

        self.gridLayout_2.addWidget(self.label_6, 1, 0, 1, 1)

        self.lineEdit_num2 = QLineEdit(self.tabNumber)
        self.lineEdit_num2.setObjectName(u"lineEdit_num2")

        self.gridLayout_2.addWidget(self.lineEdit_num2, 1, 1, 1, 1)

        self.lineEdit_num3 = QLineEdit(self.tabNumber)
        self.lineEdit_num3.setObjectName(u"lineEdit_num3")

        self.gridLayout_2.addWidget(self.lineEdit_num3, 2, 1, 1, 1)

        self.lineEdit_num1 = QLineEdit(self.tabNumber)
        self.lineEdit_num1.setObjectName(u"lineEdit_num1")

        self.gridLayout_2.addWidget(self.lineEdit_num1, 0, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 2, 1, 1)


        self.verticalLayout_4.addLayout(self.gridLayout_2)

        self.tabWidget.addTab(self.tabNumber, "")
        self.tabMoney = QWidget()
        self.tabMoney.setObjectName(u"tabMoney")
        self.widget = QWidget(self.tabMoney)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(0, 0, 637, 107))
        self.widget.setStyleSheet(u"")
        self.gridLayout_3 = QGridLayout(self.widget)
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.labelMoney1 = QLabel(self.widget)
        self.labelMoney1.setObjectName(u"labelMoney1")
        self.labelMoney1.setPixmap(QPixmap(u":/images/images/qltb.gif"))

        self.gridLayout_3.addWidget(self.labelMoney1, 0, 0, 2, 1)

        self.labelMoney2 = QLabel(self.widget)
        self.labelMoney2.setObjectName(u"labelMoney2")
        self.labelMoney2.setPixmap(QPixmap(u":/images/images/qltb.gif"))

        self.gridLayout_3.addWidget(self.labelMoney2, 0, 1, 2, 1)

        self.labelMoney3 = QLabel(self.widget)
        self.labelMoney3.setObjectName(u"labelMoney3")
        self.labelMoney3.setPixmap(QPixmap(u":/images/images/qltb.gif"))

        self.gridLayout_3.addWidget(self.labelMoney3, 0, 2, 2, 1)

        self.plainTextEdit = QPlainTextEdit(self.widget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setReadOnly(True)

        self.gridLayout_3.addWidget(self.plainTextEdit, 0, 3, 2, 1)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 40))
        self.pushButton.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.pushButton, 0, 4, 1, 1)

        self.pushButton_2 = QPushButton(self.widget)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setMinimumSize(QSize(0, 40))
        self.pushButton_2.setMaximumSize(QSize(16777215, 40))

        self.gridLayout_3.addWidget(self.pushButton_2, 1, 4, 1, 1)

        self.tabWidget.addTab(self.tabMoney, "")
        self.tabTime = QWidget()
        self.tabTime.setObjectName(u"tabTime")
        self.widget_3 = QWidget(self.tabTime)
        self.widget_3.setObjectName(u"widget_3")
        self.widget_3.setGeometry(QRect(0, 0, 641, 81))
        self.gridLayout_4 = QGridLayout(self.widget_3)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.label_9 = QLabel(self.widget_3)
        self.label_9.setObjectName(u"label_9")

        self.gridLayout_4.addWidget(self.label_9, 0, 0, 1, 2)

        self.label_13 = QLabel(self.widget_3)
        self.label_13.setObjectName(u"label_13")

        self.gridLayout_4.addWidget(self.label_13, 1, 0, 1, 1)

        self.label_10 = QLabel(self.widget_3)
        self.label_10.setObjectName(u"label_10")
        font = QFont()
        font.setPointSize(21)
        font.setBold(True)
        self.label_10.setFont(font)

        self.gridLayout_4.addWidget(self.label_10, 2, 0, 2, 1)

        self.label_11 = QLabel(self.widget_3)
        self.label_11.setObjectName(u"label_11")

        self.gridLayout_4.addWidget(self.label_11, 2, 1, 1, 1)

        self.label_12 = QLabel(self.widget_3)
        self.label_12.setObjectName(u"label_12")

        self.gridLayout_4.addWidget(self.label_12, 3, 1, 1, 1)

        self.tabWidget.addTab(self.tabTime, "")
        self.tabCustom = QWidget()
        self.tabCustom.setObjectName(u"tabCustom")
        self.widget_4 = QWidget(self.tabCustom)
        self.widget_4.setObjectName(u"widget_4")
        self.widget_4.setGeometry(QRect(0, 0, 421, 102))
        self.verticalLayout_5 = QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_8 = QLabel(self.widget_4)
        self.label_8.setObjectName(u"label_8")

        self.horizontalLayout_3.addWidget(self.label_8)

        self.comboBox_yao6 = QComboBox(self.widget_4)
        self.comboBox_yao6.addItem("")
        self.comboBox_yao6.addItem("")
        self.comboBox_yao6.addItem("")
        self.comboBox_yao6.addItem("")
        self.comboBox_yao6.setObjectName(u"comboBox_yao6")
        self.comboBox_yao6.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_yao6)

        self.label_16 = QLabel(self.widget_4)
        self.label_16.setObjectName(u"label_16")

        self.horizontalLayout_3.addWidget(self.label_16)

        self.comboBox_yao3 = QComboBox(self.widget_4)
        self.comboBox_yao3.addItem("")
        self.comboBox_yao3.addItem("")
        self.comboBox_yao3.addItem("")
        self.comboBox_yao3.addItem("")
        self.comboBox_yao3.setObjectName(u"comboBox_yao3")
        self.comboBox_yao3.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_3.addWidget(self.comboBox_yao3)


        self.verticalLayout_5.addLayout(self.horizontalLayout_3)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_14 = QLabel(self.widget_4)
        self.label_14.setObjectName(u"label_14")

        self.horizontalLayout_4.addWidget(self.label_14)

        self.comboBox_yao5 = QComboBox(self.widget_4)
        self.comboBox_yao5.addItem("")
        self.comboBox_yao5.addItem("")
        self.comboBox_yao5.addItem("")
        self.comboBox_yao5.addItem("")
        self.comboBox_yao5.setObjectName(u"comboBox_yao5")
        self.comboBox_yao5.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_yao5)

        self.label_17 = QLabel(self.widget_4)
        self.label_17.setObjectName(u"label_17")

        self.horizontalLayout_4.addWidget(self.label_17)

        self.comboBox_yao2 = QComboBox(self.widget_4)
        self.comboBox_yao2.addItem("")
        self.comboBox_yao2.addItem("")
        self.comboBox_yao2.addItem("")
        self.comboBox_yao2.addItem("")
        self.comboBox_yao2.setObjectName(u"comboBox_yao2")
        self.comboBox_yao2.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.comboBox_yao2)


        self.verticalLayout_5.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.label_15 = QLabel(self.widget_4)
        self.label_15.setObjectName(u"label_15")

        self.horizontalLayout_5.addWidget(self.label_15)

        self.comboBox_yao4 = QComboBox(self.widget_4)
        self.comboBox_yao4.addItem("")
        self.comboBox_yao4.addItem("")
        self.comboBox_yao4.addItem("")
        self.comboBox_yao4.addItem("")
        self.comboBox_yao4.setObjectName(u"comboBox_yao4")
        self.comboBox_yao4.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.comboBox_yao4)

        self.label_18 = QLabel(self.widget_4)
        self.label_18.setObjectName(u"label_18")

        self.horizontalLayout_5.addWidget(self.label_18)

        self.comboBox_yao1 = QComboBox(self.widget_4)
        self.comboBox_yao1.addItem("")
        self.comboBox_yao1.addItem("")
        self.comboBox_yao1.addItem("")
        self.comboBox_yao1.addItem("")
        self.comboBox_yao1.setObjectName(u"comboBox_yao1")
        self.comboBox_yao1.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_5.addWidget(self.comboBox_yao1)


        self.verticalLayout_5.addLayout(self.horizontalLayout_5)

        self.tabWidget.addTab(self.tabCustom, "")
        self.tabComputer = QWidget()
        self.tabComputer.setObjectName(u"tabComputer")
        self.tabWidget.addTab(self.tabComputer, "")

        self.verticalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_2.addWidget(self.groupBox_2)

        self.textEditTips = QTextEdit(Dialog)
        self.textEditTips.setObjectName(u"textEditTips")
        self.textEditTips.setReadOnly(True)

        self.verticalLayout_2.addWidget(self.textEditTips)

        self.widget_2 = QWidget(Dialog)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setMinimumSize(QSize(0, 40))
        self.widget_2.setMaximumSize(QSize(16777215, 40))
        self.horizontalLayout_2 = QHBoxLayout(self.widget_2)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(460, 19, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.pushButtonOK = QPushButton(self.widget_2)
        self.pushButtonOK.setObjectName(u"pushButtonOK")

        self.horizontalLayout_2.addWidget(self.pushButtonOK)

        self.pushButtonCancel = QPushButton(self.widget_2)
        self.pushButtonCancel.setObjectName(u"pushButtonCancel")

        self.horizontalLayout_2.addWidget(self.pushButtonCancel)


        self.verticalLayout_2.addWidget(self.widget_2)

        self.verticalLayout_2.setStretch(0, 2)
        self.verticalLayout_2.setStretch(1, 3)
        self.verticalLayout_2.setStretch(2, 5)
        self.verticalLayout_2.setStretch(3, 1)
        QWidget.setTabOrder(self.lineEditName, self.radioButtonMan)
        QWidget.setTabOrder(self.radioButtonMan, self.radioButtonWoman)
        QWidget.setTabOrder(self.radioButtonWoman, self.dateEditBirthday)
        QWidget.setTabOrder(self.dateEditBirthday, self.plainTextEditWhat)
        QWidget.setTabOrder(self.plainTextEditWhat, self.tabWidget)
        QWidget.setTabOrder(self.tabWidget, self.lineEdit_num1)
        QWidget.setTabOrder(self.lineEdit_num1, self.lineEdit_num2)
        QWidget.setTabOrder(self.lineEdit_num2, self.lineEdit_num3)
        QWidget.setTabOrder(self.lineEdit_num3, self.pushButtonOK)
        QWidget.setTabOrder(self.pushButtonOK, self.pushButtonCancel)

        self.retranslateUi(Dialog)

        self.tabWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.groupBox.setTitle(QCoreApplication.translate("Dialog", u"\u7528\u6237\u4fe1\u606f", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u59d3\u540d\uff1a", None))
        self.lineEditName.setPlaceholderText(QCoreApplication.translate("Dialog", u"\u8bf7\u8f93\u5165\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"\u6027\u522b\uff1a", None))
        self.radioButtonMan.setText(QCoreApplication.translate("Dialog", u"\u7537", None))
        self.radioButtonWoman.setText(QCoreApplication.translate("Dialog", u"\u5973", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"\u51fa\u751f\u65e5\u671f\uff1a", None))
        self.dateEditBirthday.setDisplayFormat(QCoreApplication.translate("Dialog", u"yyyy/MM/dd", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5360\u4e8b\uff1a", None))
        self.plainTextEditWhat.setPlainText("")
        self.plainTextEditWhat.setPlaceholderText("")
        self.groupBox_2.setTitle(QCoreApplication.translate("Dialog", u"\u8d77\u5366\u65b9\u5f0f", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e00\u4e2a\u6570\u5b57\uff1a", None))
        self.label_7.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e09\u4e2a\u6570\u5b57\uff1a", None))
        self.label_6.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e8c\u4e2a\u6570\u5b57\uff1a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabNumber), QCoreApplication.translate("Dialog", u"\u6570\u5b57\u5366", None))
        self.labelMoney1.setText("")
        self.labelMoney2.setText("")
        self.labelMoney3.setText("")
        self.plainTextEdit.setPlainText(QCoreApplication.translate("Dialog", u"\u8bf7\u70b9\u51fb\u65c1\u8fb9\u201c\u7b2c\u4e00\u6b21\u201d\u6309\u94ae\uff0c\u4e00\u5171\u9700\u89816\u6b21", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u7b2c0/6\u6b21", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u91cd\u65b0\u5f00\u59cb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabMoney), QCoreApplication.translate("Dialog", u"\u94dc\u94b1\u5366", None))
        self.label_9.setText(QCoreApplication.translate("Dialog", u"2021\u5e7410\u670831\u65e5 13\uff1a24", None))
        self.label_13.setText(QCoreApplication.translate("Dialog", u" \u516b\u6708\u5eff\u516d", None))
        self.label_10.setText(QCoreApplication.translate("Dialog", u"\u8f9b\u4e11\u5e74 \u8fb0\u65f6", None))
        self.label_11.setText(QCoreApplication.translate("Dialog", u"\u5b9c\uff1a\u642c\u5bb6 \u7ed3\u5a5a \u9886\u8bc1 \u5b89\u5e8a \u8ba2\u5a5a \u4e0a\u6881 \u5165\u5b66 \u6c42\u55e3 \u4fee\u575f \u8d74\u4efb \u7948\u798f \u6c42\u533b \u7eb3\u91c7 \u7acb\u5238", None))
        self.label_12.setText(QCoreApplication.translate("Dialog", u"\u5fcc\uff1a\u88c5\u4fee \u5f00\u4e1a \u5f00\u5de5 \u52a8\u571f \u51fa\u884c \u5b89\u846c \u5f00\u5f20 \u65c5\u6e38 \u7834\u571f \u653e\u6c34 \u6c42\u8d22 \u4fee\u9020 \u7f6e\u4ea7 \u7eb3\u755c", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabTime), QCoreApplication.translate("Dialog", u"\u65f6\u95f4\u5366", None))
        self.label_8.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u516d\u723b", None))
        self.comboBox_yao6.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao6.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao6.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao6.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.label_16.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e09\u723b", None))
        self.comboBox_yao3.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao3.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao3.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao3.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.label_14.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e94\u723b", None))
        self.comboBox_yao5.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao5.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao5.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao5.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.label_17.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e8c\u723b", None))
        self.comboBox_yao2.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao2.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao2.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao2.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.label_15.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u56db\u723b", None))
        self.comboBox_yao4.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao4.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao4.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao4.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.label_18.setText(QCoreApplication.translate("Dialog", u"\u7b2c\u4e00\u723b", None))
        self.comboBox_yao1.setItemText(0, QCoreApplication.translate("Dialog", u"\u5c11\u9634 - -", None))
        self.comboBox_yao1.setItemText(1, QCoreApplication.translate("Dialog", u"\u5c11\u9633 \u2014", None))
        self.comboBox_yao1.setItemText(2, QCoreApplication.translate("Dialog", u"\u8001\u9633 \u2014 O", None))
        self.comboBox_yao1.setItemText(3, QCoreApplication.translate("Dialog", u"\u8001\u9634 - - X", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabCustom), QCoreApplication.translate("Dialog", u"\u624b\u5de5\u8d77\u5366", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tabComputer), QCoreApplication.translate("Dialog", u"\u7535\u8111\u81ea\u52a8", None))
        self.textEditTips.setHtml(QCoreApplication.translate("Dialog", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'Microsoft YaHei UI'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<h3 style=\" margin-top:5px; margin-bottom:5px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:28px; background-color:#f8eacf;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:large; font-weight:700; color:#804627; background-color:#f8eacf;\">\u5468\u6613\u5360\u535c\u7b80\u4ecb\uff1a</span></h3>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:12px; margin-right:0px; -qt-block-indent:0; text-indent:0px; line-height:28px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29"
                        "\u7d8b'; font-size:medium; color:#000000; background-color:#fefaef;\">\u300a\u6613\u7ecf\u300b\u662f\u4e00\u672c\u6700\u53e4\u8001\u7684\u4e66\uff0c\u88ab\u79f0\u4e3a\u201c\u7fa4\u7ecf\u4e4b\u9996\u201d\u3001\u201c\u6587\u5316\u4e4b\u6e90\u201d\u3002\u4e0d\u8fc7\uff0c\u73b0\u4ee3\u4eba\u542c\u5230\u300a\u6613\u7ecf\u300b\u6240\u60f3\u5230\u7684\u53ef\u80fd\u662f\uff1a\u5b83\u53ef\u4ee5\u7528\u6765\u7b97\u547d\u5417\uff1f\u6ca1\u9519\uff0c\u300a\u6613\u7ecf\u300b\u786e\u5b9e\u654e\u4eba\u5982\u4f55\u5360\u5366\uff0c\u4f46\u662f\u5360\u5366\u4e0d\u7b49\u4e8e\u7b97\u547d\uff1b\u5e76\u4e14\uff0c\u9664\u4e86\u5360\u5366\u4e4b\u5916\uff0c\u300a\u6613\u7ecf\u300b\u8fd8\u8c08\u505a\u4eba\u5904\u4e16\u7684\u9053\u7406\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:12px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:medium; color:#000000; back"
                        "ground-color:#fefaef;\">\u300a\u6613\u7ecf\u300b\u5360\u5366\u987b\u77e5</span><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:medium; color:#000000;\"><br />1.\u4eba\u751f\u6709\u65e0\u6570\u7684\u6289\u62e9\uff0c\u9020\u6210\u5409\u51f6\u6094\u541d\u3002\u5982\u4f55\u6289\u62e9\u53ef\u4fdd\u5e73\u5b89\uff1f\u53ef\u4ee5\u8d8b\u5409\u907f\u51f6\uff1f\u300a\u6613\u7ecf\u300b\u63d0\u9192\u4eba\u8981\u6ce8\u610f\uff1a\u5fb7\u884c\uff08\u56e0\u4e3a\u6b32\u671b\u4f1a\u9020\u6210\u76f2\u70b9\u4e0e\u6267\u8457\uff09\uff1b\u80fd\u529b\uff08\u6709\u80fd\u529b\u5c31\u6709\u81ea\u4fe1\uff09\uff1b\u4ee5\u53ca\u667a\u6167\uff08\u5145\u5206\u8fd0\u7528\u7406\u6027\u7684\u529b\u91cf\uff0c\u52a0\u4e0a\u751f\u6d3b\u7ecf\u9a8c\u7684\u914d\u5408\uff09\u3002<br />2.\u5728\u201c\u667a\u6167\u201d\u65b9\u9762\uff0c\u5360\u5366\u53ef\u4ee5\u63d0\u4f9b\u534f\u52a9\u3002\u6240\u8c13\u7684\u201c\u65e0\u6709\u5e08\u4fdd\uff0c\u5982\u4e34\u7236\u6bcd\u201d\uff0c\u4ee5\u53ca\u201c"
                        "\u4eba\u8c0b\u9b3c\u8c0b\uff0c\u767e\u59d3\u4e0e\u80fd\u201d\uff08\u7cfb\u8f9e\u4e0b\uff09\u3002<br />3.\u5728\u7406\u6027\u53ca\u7ecf\u9a8c\u7686\u65e0\u6cd5\u660e\u786e\u8bba\u65ad\u65f6\uff0c\u53ef\u4ee5\u8fdb\u884c\u5360\u5366\u3002\u9996\u5148\uff0c\u8981\u9075\u5b88\u201c\u4e09\u4e0d\u5360\u201d\u539f\u5219\uff1a<br />\u2460\u4e0d\u8bda\u4e0d\u5360\uff1a\u6b64\u4e43\u6c42\u6559\u4e8e\u795e\u660e\uff0c\u9996\u91cd\u771f\u8bda\u3002<br />\u2461\u4e0d\u4e49\u4e0d\u5360\uff1a\u4e0d\u5408\u4e4e\u6b63\u5f53\u6027\u53ca\u5408\u7406\u6027\u7684\u95ee\u9898\uff0c\u4e0d\u5fc5\u5360\u95ee\u3002<br />\u2462\u4e0d\u7591\u4e0d\u5360\uff1a\u5fc5\u987b\u662f\u7406\u6027\u96be\u4ee5\u6d4b\u5ea6\u4e4b\u4e8b\u3002<br />4.\u63d0\u95ee\u65b9\u6cd5\uff1a<br />\u2460\u6bcf\u6b21\u4e00\u4e2a\u95ee\u9898\uff0c\u95ee\u9898\u662f\uff1a\u73b0\u5728\u6709\u4e00\u9009\u62e9\uff0c\u4e00\u65e6\u51b3\u5b9a\u5219\u540e\u679c\u5982\u4f55\uff1f\u8b6c\u5982\u5c0f\u5b69\u53ef\u9009\u4e24\u4e2a\u5b66\u6821\uff0c\u5219\u987b\u5206\u5360\u4e8c\u6b21"
                        "\uff0c\u770b\u5176\u7ed3\u679c\u4f55\u8005\u4e3a\u5b9c\u3002\u6216\u8005\uff0c\u6b32\u8d2d\u67d0\u5c4b\uff0c\u5360\u5176\u662f\u5426\u53ef\u884c\uff1f\u5f53\u7136\uff0c\u4ea6\u53ef\u5360\u4e2a\u4eba\u4e4b\u65f6\u8fd0\u3001\u7ecf\u5546\u3001\u5a5a\u59fb\u3001\u4e8b\u4e1a\u3001\u5065\u5eb7\u3001\u5b50\u55e3\u7b49\u3002<br />\u2461\u540c\u4e00\u95ee\u9898\uff0c\u53ef\u4ee5\u6362\u4e0d\u540c\u65b9\u5f0f\u6765\u5360\u3002\u4e00\u65e6\u6709\u4e86\u7ed3\u679c\uff0c\u5219\u987b\u8fc7\u4e09\u4e2a\u6708\uff08\u4e00\u5b63\uff09\u518d\u5360\u3002<br />5.\u5360\u5366\u6700\u597d\u5728\u6e05\u6668\uff0c\u5fc3\u601d\u6e05\u51c0\uff0c\u610f\u5ff5\u96c6\u4e2d\u3002\u5148\u62df\u597d\u95ee\u9898\uff0c\u51c6\u5907\u7eb8\u7b14\u3002\u62ff\u51fa\u7b79\u7b56\uff0c\u63e1\u4e8e\u624b\u4e2d\uff0c\u5fc3\u4e2d\u9ed8\u5ff5\uff1a\u201c\u5047\u5c14\u6cf0\u7b6e\u6709\u5e38\uff0c\u67d0\uff08\u81ea\u5df1\u540d\u5b57\uff09\u4eca\u4ee5\u67d0\u4e8b\uff0c\u672a\u77e5\u53ef\u5426\u3002\u7230\u8d28\u6240\u7591\u4e8e\u795e\u4e4b\u7075\uff0c\u5409\u51f6"
                        "\u3001\u5f97\u5931\u3001\u6094\u541d\u3001\u5fe7\u865e\uff0c\u552f\u5c14\u6709\u795e\uff0c\u5c1a\u660e\u544a\u4e4b\u3002\u201d<br />6.\u7136\u540e\u4f9d\u5360\u5366\u6b65\u9aa4\uff0c\u4ed4\u7ec6\u8fdb\u884c\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:medium; color:#000000; background-color:#fefaef;\">\u00a0</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:medium; font-weight:700; color:#000000;\">\u5468\u6613\u9884\u6d4b\u6447\u5366\u65b9\u6cd5</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; te"
                        "xt-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000;\"><br />\u6309\u7167\u53e4\u7c4d\u300a\u6613\u7ecf\u300b\u7684\u94dc\u5e01\u8d77\u5366\u65b9\u6cd5\u5982\u4e0b\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000; background-color:#fefaef;\">\u4e00\u3001\u53cc\u624b\u5408\u5341\uff0c\u5c06\u4e09\u679a\u94dc\u94b1\uff08\u6216\u94dc\u5e01\uff09\u5408\u4e8e\u638c\u5fc3\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; co"
                        "lor:#000000; background-color:#fefaef;\">\u4e8c\u3001\u96c6\u4e2d\u610f\u5ff5\uff0c\u5fc3\u91cc\u60f3\u7740\u9700\u8981\u9884\u6d4b\u7684\u4e8b\uff0c\u5fc3\u5ff5\u8981\u4e13\u4e00\uff0c\u4e00\u822c\u4e00\u4ef6\u4e8b\u8d77\u4e00\u5366\uff0c\u4e0d\u8981\u540c\u65f6\u60f3\u7740\u51e0\u4ef6\u4e8b\uff0c\u8fd9\u6837\u5c31\u8d77\u5366\u4e0d\u51c6\u4e86\u3002\u96c6\u4e2d\u610f\u5ff5\uff0c\u4f7f\u624b\u5fc3\u94dc\u94b1\u7684\u78c1\u573a\u4e0e\u4eba\u4f53\u78c1\u573a\u76f8\u901a\uff0c\u53cc\u624b\u5408\u5341\u65f6\u95f4\u7ea6\u4e00\u5206\u949f\u3002\uff08\u6ce8\uff1a\u53e4\u4ee3\u8d77\u5366\u793c\u8282\u9887\u591a\uff0c\u8fd8\u9700\u6c90\u6d74\u66f4\u8863\uff0c\u711a\u9999\uff0c\u9759\u5fc3\u7b49\uff0c\u8fd9\u4e9b\u5728\u4e00\u822c\u8d77\u5366\u65f6\u5c31\u7b80\u7565\u4e86\uff0c\u53ea\u662f\u5728\u9884\u6d4b\u91cd\u5927\u4e8b\u9879\u65f6\uff0c\u4f9d\u53e4\u65b9\u8d77\u5366\uff0c\u51c6\u786e\u5ea6\u66f4\u9ad8\uff09</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-"
                        "indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000; background-color:#fefaef;\">\u4e09\u3001\u53cc\u624b\u5408\u5341\uff0c\u638c\u5fc3\u7565\u7559\u7a7a\u95f4\uff0c\u4f7f\u5f97\u94dc\u94b1\u80fd\u591f\u5728\u53cc\u624b\u638c\u5fc3\u8f6c\u52a8\u4e3a\u4f73\uff0c\u53cc\u624b\u6447\u52a8\u51e0\u6b21\u540e\uff0c\u677e\u5f00\uff0c\u8ba9\u94dc\u94b1\u843d\u5728\u684c\u9762\uff0c\u770b\u4e09\u4e2a\u94dc\u94b1\u4e2d\uff0c\u5171\u6709\u51e0\u4e2a\u662f\u201c\u80cc\u9762\u201d\uff1a\u4e00\u4e2a\u80cc\u9762\u8bb0\u4f5c\u201c\u3001\u201d\uff0c\u4e24\u4e2a\u80cc\u9762\u8bb0\u4f5c\u201c\u3001\u3001\u201d\uff0c\u4e09\u4e2a\u80cc\u9762\u8bb0\u4f5c\uff1a\u201co\u201d,\u5982\u679c\u4e09\u4e2a\u90fd\u662f\u6b63\u9762\uff0c\u5219\u8bb0\u4f5c\u201cx\u201d,\u8fd9\u6837\uff0c\u4e00\u5366\u7684\u4e00\u723b\u4fbf\u5f62\u6210\u4e86\u3002</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin"
                        "-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000;\"><br />\u56db\u3001\u7167\u4e0a\u9762\u65b9\u6cd5\u5171\u6447\u516d\u6b21\uff0c\u4ece\u4e0b\u5411\u4e0a\u5206\u522b\u8bb0\u5f55\u6bcf\u4e00\u6b21\uff08\u4e5f\u5c31\u662f\u6bcf\u4e00\u723b\uff09\u7684\u7ed3\u679c\uff0c\u4e00\u4e2a\u5b8c\u6574\u7684\u5366\uff08\u5171\u516d\u723b\uff09\u5c31\u5f62\u6210\u4e86\uff0c\u53ef\u4ee5\u7528\u4e8e\u9884\u6d4b\u4e86\u3002\u4f8b\u5982\u6447\u4e86\u516d\u6b21\uff0c\u8bb0\u5f55\u5982\u4e0b\uff1a</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000; background-color:#fefaef;\">\u7b2c\u516d\u6b21\uff08\u4e00\u4e2a\u80cc\u9762"
                        "\uff09 \u7ed3\u679c\u201c\u3001\u201d</span><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000;\"><br />\u7b2c\u4e94\u6b21\uff08\u4e00\u4e2a\u80cc\u9762\uff09 \u7ed3\u679c\u201c\u3001\u201d<br />\u7b2c\u56db\u6b21\uff08\u4e24\u4e2a\u80cc\u9762\uff09 \u7ed3\u679c\u201c\u3001\u3001\u201d<br />\u7b2c\u4e09\u6b21\uff08\u4e09\u4e2a\u80cc\u9762\uff09 \u7ed3\u679c\u201co\u201d<br />\u7b2c\u4e8c\u6b21\uff08\u4e09\u4e2a\u6b63\u9762\uff09 \u7ed3\u679c\u201cx\u201d<br />\u7b2c\u4e00\u6b21\uff08\u4e00\u4e2a\u80cc\u9762\uff09 \u7ed3\u679c\u201c\u3001\u201d</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#fefaef;\"><span style=\" font-family:'Microsoft Yahei','Arial','Helvetica','sans-serif','\u7039\u5b29\u7d8b'; font-size:14px; color:#000000;\"><br />\u8fd9\u5c31\u662f\u5b8c\u6574\u7684\u4e00\u5366\uff0c\u65b9\u6cd5\u5e76\u4e0d\u96be\uff0c\u96be"
                        "\u5c31\u96be\u5728\u5fc3\u5ff5\u4e13\u4e00\u3001\u4e00\u4e8b\u4e00\u5366\uff0c\u5f53\u7136\u8fd8\u6709\u89e3\u5366\u7684\u51c6\u786e\u6027\u4e86\u3002</span></p></body></html>", None))
        self.pushButtonOK.setText(QCoreApplication.translate("Dialog", u"\u67e5\u770b\u7ed3\u679c", None))
        self.pushButtonCancel.setText(QCoreApplication.translate("Dialog", u"\u53d6\u6d88", None))
    # retranslateUi

