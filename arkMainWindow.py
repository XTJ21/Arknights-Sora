# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\arkMainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_arkMainWindow(object):
    def setupUi(self, arkMainWindow):
        arkMainWindow.setObjectName("arkMainWindow")
        arkMainWindow.resize(387, 176)
        self.centralwidget = QtWidgets.QWidget(arkMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.formLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.formLayoutWidget.setGeometry(QtCore.QRect(10, 0, 371, 121))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.LAYOUT_MAINWINDOW = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.LAYOUT_MAINWINDOW.setContentsMargins(0, 0, 0, 0)
        self.LAYOUT_MAINWINDOW.setObjectName("LAYOUT_MAINWINDOW")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.LAYOUT_INFO_BATTLECOUNT = QtWidgets.QHBoxLayout()
        self.LAYOUT_INFO_BATTLECOUNT.setObjectName("LAYOUT_INFO_BATTLECOUNT")
        self.CB_BATTLECOUNT = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.CB_BATTLECOUNT.setCheckable(True)
        self.CB_BATTLECOUNT.setChecked(False)
        self.CB_BATTLECOUNT.setTristate(False)
        self.CB_BATTLECOUNT.setObjectName("CB_BATTLECOUNT")
        self.LAYOUT_INFO_BATTLECOUNT.addWidget(self.CB_BATTLECOUNT)
        self.TXT_BATTLECOUNT = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.TXT_BATTLECOUNT.setEnabled(True)
        self.TXT_BATTLECOUNT.setProperty("value", 0)
        self.TXT_BATTLECOUNT.setObjectName("TXT_BATTLECOUNT")
        self.LAYOUT_INFO_BATTLECOUNT.addWidget(self.TXT_BATTLECOUNT)
        self.verticalLayout.addLayout(self.LAYOUT_INFO_BATTLECOUNT)
        self.LAYOUT_INFO_SANITYCOUNT = QtWidgets.QHBoxLayout()
        self.LAYOUT_INFO_SANITYCOUNT.setObjectName("LAYOUT_INFO_SANITYCOUNT")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.LAYOUT_INFO_SANITYCOUNT.addWidget(self.label)
        self.TXT_SANITYCOUNT = QtWidgets.QSpinBox(self.formLayoutWidget)
        self.TXT_SANITYCOUNT.setObjectName("TXT_SANITYCOUNT")
        self.LAYOUT_INFO_SANITYCOUNT.addWidget(self.TXT_SANITYCOUNT)
        self.verticalLayout.addLayout(self.LAYOUT_INFO_SANITYCOUNT)
        self.CB_MUSIC = QtWidgets.QCheckBox(self.formLayoutWidget)
        self.CB_MUSIC.setEnabled(True)
        self.CB_MUSIC.setMouseTracking(True)
        self.CB_MUSIC.setAcceptDrops(False)
        self.CB_MUSIC.setObjectName("CB_MUSIC")
        self.verticalLayout.addWidget(self.CB_MUSIC)
        self.LAYOUT_MAINWINDOW.setLayout(0, QtWidgets.QFormLayout.LabelRole, self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.BIN_START = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BIN_START.setObjectName("BIN_START")
        self.verticalLayout_2.addWidget(self.BIN_START)
        self.BIN_STOP = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BIN_STOP.setEnabled(False)
        self.BIN_STOP.setObjectName("BIN_STOP")
        self.verticalLayout_2.addWidget(self.BIN_STOP)
        self.BTN_GETDEVICE = QtWidgets.QPushButton(self.formLayoutWidget)
        self.BTN_GETDEVICE.setObjectName("BTN_GETDEVICE")
        self.verticalLayout_2.addWidget(self.BTN_GETDEVICE)
        self.LAYOUT_MAINWINDOW.setLayout(0, QtWidgets.QFormLayout.FieldRole, self.verticalLayout_2)
        arkMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(arkMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 387, 26))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        self.menuabout = QtWidgets.QMenu(self.menubar)
        self.menuabout.setObjectName("menuabout")
        arkMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(arkMainWindow)
        self.statusbar.setObjectName("statusbar")
        arkMainWindow.setStatusBar(self.statusbar)
        self.MENU_FILE_PWSHERE = QtWidgets.QAction(arkMainWindow)
        self.MENU_FILE_PWSHERE.setObjectName("MENU_FILE_PWSHERE")
        self.MENU_ABOUT_ABOUT = QtWidgets.QAction(arkMainWindow)
        self.MENU_ABOUT_ABOUT.setObjectName("MENU_ABOUT_ABOUT")
        self.menuFile.addAction(self.MENU_FILE_PWSHERE)
        self.menuabout.addAction(self.MENU_ABOUT_ABOUT)
        self.menubar.addAction(self.menuFile.menuAction())
        self.menubar.addAction(self.menuabout.menuAction())

        self.retranslateUi(arkMainWindow)
        self.MENU_FILE_PWSHERE.triggered.connect(arkMainWindow.pwsHere)
        self.BIN_START.clicked.connect(arkMainWindow.runMain)
        self.BIN_STOP.clicked.connect(arkMainWindow.stop)
        self.BTN_GETDEVICE.clicked.connect(arkMainWindow.getDevice)
        self.MENU_ABOUT_ABOUT.triggered.connect(arkMainWindow.about)
        QtCore.QMetaObject.connectSlotsByName(arkMainWindow)

    def retranslateUi(self, arkMainWindow):
        _translate = QtCore.QCoreApplication.translate
        arkMainWindow.setWindowTitle(_translate("arkMainWindow", "Arknights-Sora - zsppp"))
        self.CB_BATTLECOUNT.setStatusTip(_translate("arkMainWindow", "完成数次行动后终止"))
        self.CB_BATTLECOUNT.setText(_translate("arkMainWindow", "预定行动次数"))
        self.TXT_BATTLECOUNT.setStatusTip(_translate("arkMainWindow", "预定行动次数"))
        self.label.setStatusTip(_translate("arkMainWindow", "不足以行动时，补充理智"))
        self.label.setText(_translate("arkMainWindow", "理智液数量"))
        self.TXT_SANITYCOUNT.setStatusTip(_translate("arkMainWindow", "预定要喝的理智液数量"))
        self.CB_MUSIC.setStatusTip(_translate("arkMainWindow", "达成目标行动次数或理智清空完成，播放结束音乐"))
        self.CB_MUSIC.setText(_translate("arkMainWindow", "结束音乐"))
        self.BIN_START.setStatusTip(_translate("arkMainWindow", "在‘’开始行动“界面点击Start按钮"))
        self.BIN_START.setText(_translate("arkMainWindow", "Start"))
        self.BIN_STOP.setStatusTip(_translate("arkMainWindow", "停止脚本"))
        self.BIN_STOP.setText(_translate("arkMainWindow", "Stop"))
        self.BTN_GETDEVICE.setStatusTip(_translate("arkMainWindow", "更换安卓设备"))
        self.BTN_GETDEVICE.setText(_translate("arkMainWindow", "ChangeDevice"))
        self.menuFile.setTitle(_translate("arkMainWindow", "File"))
        self.menuabout.setTitle(_translate("arkMainWindow", "About"))
        self.MENU_FILE_PWSHERE.setText(_translate("arkMainWindow", "PowerShell"))
        self.MENU_ABOUT_ABOUT.setText(_translate("arkMainWindow", "about"))