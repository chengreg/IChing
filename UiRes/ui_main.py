# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore

import res_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1026, 680)
        self.actionNew = QAction(MainWindow)
        self.actionNew.setObjectName(u"actionNew")
        icon = QIcon()
        icon.addFile(u":/icon/images/new.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNew.setIcon(icon)
        self.actionOpen = QAction(MainWindow)
        self.actionOpen.setObjectName(u"actionOpen")
        icon1 = QIcon()
        icon1.addFile(u":/icon/images/open.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionOpen.setIcon(icon1)
        self.actionLucy_ui = QAction(MainWindow)
        self.actionLucy_ui.setObjectName(u"actionLucy_ui")
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon2 = QIcon()
        icon2.addFile(u":/icon/images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon2)
        self.actionSave_as = QAction(MainWindow)
        self.actionSave_as.setObjectName(u"actionSave_as")
        self.actionSave_All = QAction(MainWindow)
        self.actionSave_All.setObjectName(u"actionSave_All")
        self.actionPrint = QAction(MainWindow)
        self.actionPrint.setObjectName(u"actionPrint")
        icon3 = QIcon()
        icon3.addFile(u":/icon/images/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionPrint.setIcon(icon3)
        self.actionClose = QAction(MainWindow)
        self.actionClose.setObjectName(u"actionClose")
        self.actionQuit = QAction(MainWindow)
        self.actionQuit.setObjectName(u"actionQuit")
        self.actiond = QAction(MainWindow)
        self.actiond.setObjectName(u"actiond")
        icon4 = QIcon()
        icon4.addFile(u":/icon/images/cx.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiond.setIcon(icon4)
        self.actiond_2 = QAction(MainWindow)
        self.actiond_2.setObjectName(u"actiond_2")
        icon5 = QIcon()
        icon5.addFile(u":/icon/images/cz.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiond_2.setIcon(icon5)
        self.actionCopy = QAction(MainWindow)
        self.actionCopy.setObjectName(u"actionCopy")
        icon6 = QIcon()
        icon6.addFile(u":/icon/images/cut.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCopy.setIcon(icon6)
        self.actiond_3 = QAction(MainWindow)
        self.actiond_3.setObjectName(u"actiond_3")
        icon7 = QIcon()
        icon7.addFile(u":/icon/images/copy.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiond_3.setIcon(icon7)
        self.actiond_4 = QAction(MainWindow)
        self.actiond_4.setObjectName(u"actiond_4")
        icon8 = QIcon()
        icon8.addFile(u":/icon/images/pasle.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiond_4.setIcon(icon8)
        self.actiond_5 = QAction(MainWindow)
        self.actiond_5.setObjectName(u"actiond_5")
        icon9 = QIcon()
        icon9.addFile(u":/icon/images/del.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiond_5.setIcon(icon9)
        self.actiond_6 = QAction(MainWindow)
        self.actiond_6.setObjectName(u"actiond_6")
        self.actionsjr = QAction(MainWindow)
        self.actionsjr.setObjectName(u"actionsjr")
        self.actiontih = QAction(MainWindow)
        self.actiontih.setObjectName(u"actiontih")
        self.actiononline = QAction(MainWindow)
        self.actiononline.setObjectName(u"actiononline")
        icon10 = QIcon()
        icon10.addFile(u":/icon/images/help.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actiononline.setIcon(icon10)
        self.actionabout = QAction(MainWindow)
        self.actionabout.setObjectName(u"actionabout")
        self.actionmysql = QAction(MainWindow)
        self.actionmysql.setObjectName(u"actionmysql")
        self.actionll = QAction(MainWindow)
        self.actionll.setObjectName(u"actionll")
        self.actionTile = QAction(MainWindow)
        self.actionTile.setObjectName(u"actionTile")
        self.actionTile.setCheckable(True)
        self.actioncloseAllSubWindows = QAction(MainWindow)
        self.actioncloseAllSubWindows.setObjectName(u"actioncloseAllSubWindows")
        self.actionTab = QAction(MainWindow)
        self.actionTab.setObjectName(u"actionTab")
        self.actionTab.setCheckable(True)
        self.actionCascade = QAction(MainWindow)
        self.actionCascade.setObjectName(u"actionCascade")
        self.actionCascade.setCheckable(True)
        self.actionNum = QAction(MainWindow)
        self.actionNum.setObjectName(u"actionNum")
        icon11 = QIcon()
        icon11.addFile(u":/icon/images/number.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionNum.setIcon(icon11)
        self.actionMoney = QAction(MainWindow)
        self.actionMoney.setObjectName(u"actionMoney")
        icon12 = QIcon()
        icon12.addFile(u":/icon/images/money.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionMoney.setIcon(icon12)
        self.actionTime = QAction(MainWindow)
        self.actionTime.setObjectName(u"actionTime")
        icon13 = QIcon()
        icon13.addFile(u":/icon/images/time.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionTime.setIcon(icon13)
        self.actionCostom = QAction(MainWindow)
        self.actionCostom.setObjectName(u"actionCostom")
        icon14 = QIcon()
        icon14.addFile(u":/icon/images/costom.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCostom.setIcon(icon14)
        self.actionCompter = QAction(MainWindow)
        self.actionCompter.setObjectName(u"actionCompter")
        icon15 = QIcon()
        icon15.addFile(u":/icon/images/computer.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCompter.setIcon(icon15)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widget_2 = QWidget(self.centralwidget)
        self.widget_2.setObjectName(u"widget_2")
        self.widget_2.setStyleSheet(u"background-color: rgb(85, 170, 127);")
        self.verticalLayout_4 = QVBoxLayout(self.widget_2)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.mdiArea = QMdiArea(self.widget_2)
        self.mdiArea.setObjectName(u"mdiArea")

        self.verticalLayout_4.addWidget(self.mdiArea)


        self.horizontalLayout.addWidget(self.widget_2)

        self.horizontalLayout.setStretch(0, 9)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1026, 22))
        self.menuFile = QMenu(self.menubar)
        self.menuFile.setObjectName(u"menuFile")
        self.menuRecent = QMenu(self.menuFile)
        self.menuRecent.setObjectName(u"menuRecent")
        self.menuEdit = QMenu(self.menubar)
        self.menuEdit.setObjectName(u"menuEdit")
        self.menuwi = QMenu(self.menubar)
        self.menuwi.setObjectName(u"menuwi")
        self.menuhelp = QMenu(self.menubar)
        self.menuhelp.setObjectName(u"menuhelp")
        self.menu_V = QMenu(self.menubar)
        self.menu_V.setObjectName(u"menu_V")
        self.menusetting = QMenu(self.menubar)
        self.menusetting.setObjectName(u"menusetting")
        self.menuzhangua = QMenu(self.menubar)
        self.menuzhangua.setObjectName(u"menuzhangua")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        self.toolBar.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)
        self.toolBar_zhangua = QToolBar(MainWindow)
        self.toolBar_zhangua.setObjectName(u"toolBar_zhangua")
        self.toolBar_zhangua.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar_zhangua)
        self.dockWidget = QDockWidget(MainWindow)
        self.dockWidget.setObjectName(u"dockWidget")
        self.dockWidget.setFloating(False)
        self.dockWidget.setFeatures(QDockWidget.DockWidgetClosable|QDockWidget.DockWidgetFloatable|QDockWidget.DockWidgetMovable)
        self.dockWidget.setAllowedAreas(Qt.LeftDockWidgetArea|Qt.RightDockWidgetArea)
        self.dockWidgetContents_8 = QWidget()
        self.dockWidgetContents_8.setObjectName(u"dockWidgetContents_8")
        self.verticalLayout_2 = QVBoxLayout(self.dockWidgetContents_8)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.widget = QWidget(self.dockWidgetContents_8)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"")
        self.verticalLayout_3 = QVBoxLayout(self.widget)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.listView = QListView(self.widget)
        self.listView.setObjectName(u"listView")

        self.verticalLayout_3.addWidget(self.listView)


        self.verticalLayout_2.addWidget(self.widget)

        self.dockWidget.setWidget(self.dockWidgetContents_8)
        MainWindow.addDockWidget(Qt.LeftDockWidgetArea, self.dockWidget)

        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuzhangua.menuAction())
        self.menubar.addAction(self.menuEdit.menuAction())
        self.menubar.addAction(self.menuwi.menuAction())
        self.menubar.addAction(self.menu_V.menuAction())
        self.menubar.addAction(self.menusetting.menuAction())
        self.menubar.addAction(self.menuhelp.menuAction())
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addAction(self.menuRecent.menuAction())
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSave_as)
        self.menuFile.addAction(self.actionSave_All)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionPrint)
        self.menuFile.addAction(self.actionClose)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionQuit)
        self.menuRecent.addAction(self.actionLucy_ui)
        self.menuEdit.addAction(self.actiond)
        self.menuEdit.addAction(self.actiond_2)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionCopy)
        self.menuEdit.addAction(self.actiond_3)
        self.menuEdit.addAction(self.actiond_4)
        self.menuEdit.addAction(self.actiond_5)
        self.menuEdit.addAction(self.actiond_6)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionsjr)
        self.menuEdit.addAction(self.actiontih)
        self.menuwi.addAction(self.actionTile)
        self.menuwi.addAction(self.actionCascade)
        self.menuwi.addAction(self.actionTab)
        self.menuwi.addSeparator()
        self.menuwi.addAction(self.actioncloseAllSubWindows)
        self.menuhelp.addAction(self.actiononline)
        self.menuhelp.addAction(self.actionabout)
        self.menu_V.addAction(self.actionll)
        self.menusetting.addAction(self.actionmysql)
        self.menuzhangua.addAction(self.actionNum)
        self.menuzhangua.addAction(self.actionMoney)
        self.menuzhangua.addAction(self.actionTime)
        self.menuzhangua.addAction(self.actionCostom)
        self.menuzhangua.addAction(self.actionCompter)
        self.toolBar.addAction(self.actionNew)
        self.toolBar.addAction(self.actionOpen)
        self.toolBar.addAction(self.actiond)
        self.toolBar.addAction(self.actionSave)
        self.toolBar.addAction(self.actionCopy)
        self.toolBar.addAction(self.actiond_3)
        self.toolBar.addAction(self.actiond_5)
        self.toolBar.addAction(self.actiononline)
        self.toolBar.addAction(self.actiond_2)
        self.toolBar.addSeparator()
        self.toolBar_zhangua.addAction(self.actionNum)
        self.toolBar_zhangua.addAction(self.actionMoney)
        self.toolBar_zhangua.addAction(self.actionTime)
        self.toolBar_zhangua.addAction(self.actionCostom)
        self.toolBar_zhangua.addAction(self.actionCompter)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.actionNew.setText(QCoreApplication.translate("MainWindow", u"\u65b0\u5efa...", None))
#if QT_CONFIG(shortcut)
        self.actionNew.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+N", None))
#endif // QT_CONFIG(shortcut)
        self.actionOpen.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00...", None))
#if QT_CONFIG(shortcut)
        self.actionOpen.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+O", None))
#endif // QT_CONFIG(shortcut)
        self.actionLucy_ui.setText(QCoreApplication.translate("MainWindow", u"Lucy.ui", None))
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58(&S)", None))
#if QT_CONFIG(shortcut)
        self.actionSave.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+S", None))
#endif // QT_CONFIG(shortcut)
        self.actionSave_as.setText(QCoreApplication.translate("MainWindow", u"\u53e6\u5b58\u4e3a...", None))
        self.actionSave_All.setText(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u4fdd\u5b58(&S)", None))
#if QT_CONFIG(tooltip)
        self.actionSave_All.setToolTip(QCoreApplication.translate("MainWindow", u"\u5168\u90e8\u4fdd\u5b58(L)", None))
#endif // QT_CONFIG(tooltip)
        self.actionPrint.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5370...", None))
#if QT_CONFIG(tooltip)
        self.actionPrint.setToolTip(QCoreApplication.translate("MainWindow", u"\u6253\u5370(&P)", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(shortcut)
        self.actionPrint.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+P", None))
#endif // QT_CONFIG(shortcut)
        self.actionClose.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed", None))
        self.actionQuit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actiond.setText(QCoreApplication.translate("MainWindow", u"\u64a4\u9500(&Z)", None))
#if QT_CONFIG(shortcut)
        self.actiond.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Z", None))
#endif // QT_CONFIG(shortcut)
        self.actiond_2.setText(QCoreApplication.translate("MainWindow", u"\u91cd\u505a(&Y)", None))
#if QT_CONFIG(shortcut)
        self.actiond_2.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+Y", None))
#endif // QT_CONFIG(shortcut)
        self.actionCopy.setText(QCoreApplication.translate("MainWindow", u"\u526a\u5207(&T)", None))
#if QT_CONFIG(shortcut)
        self.actionCopy.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+X", None))
#endif // QT_CONFIG(shortcut)
        self.actiond_3.setText(QCoreApplication.translate("MainWindow", u"\u590d\u5236(&C)", None))
#if QT_CONFIG(shortcut)
        self.actiond_3.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+C", None))
#endif // QT_CONFIG(shortcut)
        self.actiond_4.setText(QCoreApplication.translate("MainWindow", u"\u7c98\u8d34(&P)", None))
        self.actiond_5.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664(&D)", None))
        self.actiond_6.setText(QCoreApplication.translate("MainWindow", u"\u5168\u9009(&A)", None))
#if QT_CONFIG(shortcut)
        self.actiond_6.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+A", None))
#endif // QT_CONFIG(shortcut)
        self.actionsjr.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u627e(&S)", None))
#if QT_CONFIG(shortcut)
        self.actionsjr.setShortcut(QCoreApplication.translate("MainWindow", u"Ctrl+F", None))
#endif // QT_CONFIG(shortcut)
        self.actiontih.setText(QCoreApplication.translate("MainWindow", u"\u66ff\u6362", None))
        self.actiononline.setText(QCoreApplication.translate("MainWindow", u"\u5728\u7ebf\u6587\u6863", None))
        self.actionabout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.actionmysql.setText(QCoreApplication.translate("MainWindow", u"\u6570\u636e\u5e93\u914d\u7f6e", None))
        self.actionll.setText(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6253\u5f00", None))
        self.actionTile.setText(QCoreApplication.translate("MainWindow", u"\u5e73\u94fa\u6a21\u5f0f(&T)", None))
        self.actioncloseAllSubWindows.setText(QCoreApplication.translate("MainWindow", u"\u5173\u95ed\u5168\u90e8\u7a97\u53e3(&A)", None))
        self.actionTab.setText(QCoreApplication.translate("MainWindow", u"\u6807\u7b7e\u6a21\u5f0f", None))
        self.actionCascade.setText(QCoreApplication.translate("MainWindow", u"\u7ea7\u8054\u6a21\u5f0f", None))
        self.actionNum.setText(QCoreApplication.translate("MainWindow", u"\u6570\u5b57\u5366(&N)", None))
        self.actionMoney.setText(QCoreApplication.translate("MainWindow", u"\u94dc\u94b1\u5366(&M)", None))
        self.actionTime.setText(QCoreApplication.translate("MainWindow", u"\u65f6\u95f4\u5366(&T)", None))
        self.actionCostom.setText(QCoreApplication.translate("MainWindow", u"\u624b\u5de5\u8d77\u5366(&C)", None))
        self.actionCompter.setText(QCoreApplication.translate("MainWindow", u"\u7535\u8111\u81ea\u52a8(&A)", None))
        self.menuFile.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6(&F)", None))
        self.menuRecent.setTitle(QCoreApplication.translate("MainWindow", u"\u6700\u8fd1\u6253\u5f00", None))
        self.menuEdit.setTitle(QCoreApplication.translate("MainWindow", u"\u7f16\u8f91(&E)", None))
        self.menuwi.setTitle(QCoreApplication.translate("MainWindow", u"\u7a97\u53e3(&W)", None))
        self.menuhelp.setTitle(QCoreApplication.translate("MainWindow", u"\u5e2e\u52a9(&H)", None))
        self.menu_V.setTitle(QCoreApplication.translate("MainWindow", u"\u89c6\u56fe(&V)", None))
        self.menusetting.setTitle(QCoreApplication.translate("MainWindow", u"\u8bbe\u7f6e(&S)", None))
        self.menuzhangua.setTitle(QCoreApplication.translate("MainWindow", u"\u5360\u5366(&G)", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
        self.toolBar_zhangua.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar_2", None))
        self.dockWidget.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5360\u5366\u8bb0\u5f55", None))
    # retranslateUi

