# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'biyesheji.ui'
#
# Created: Wed Apr 05 13:00:08 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

import main

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s
global file_name
file_name = ''
try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1342, 890)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_2 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))

        self.regText = QtGui.QTextBrowser(self.centralwidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.MinimumExpanding, QtGui.QSizePolicy.MinimumExpanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.regText.sizePolicy().hasHeightForWidth())

        self.regText.setSizePolicy(sizePolicy)
        self.regText.setMinimumSize(QtCore.QSize(601, 51))
        self.regText.setBaseSize(QtCore.QSize(601, 51))
        self.regText.setObjectName(_fromUtf8("regText"))
        self.gridLayout_2.addWidget(self.regText, 1, 1, 1, 1)

        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 631, 821))
        #
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.setTabsClosable(True)

        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(QtCore.QRect(0, 0, 651, 821)))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textEdit.setText("I want to play a game")
        self.textEdit.setReadOnly(False)
        self.gridLayoutWidget = QtGui.QWidget(self.tab)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(-10, -30, 1541, 871))
        self.gridLayoutWidget.setObjectName(_fromUtf8("gridLayoutWidget"))
        self.gridLayout = QtGui.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.tabWidget.addTab(self.tab, _fromUtf8("no_title"))

        self.gridLayout_2.addWidget(self.tabWidget, 0, 0, 9, 1)
        self.label_result = QtGui.QLabel(self.centralwidget)
        self.label_result.setObjectName(_fromUtf8("label_result"))
        self.gridLayout_2.addWidget(self.label_result, 7, 1, 1, 1)

        self.label_reg = QtGui.QLabel(self.centralwidget)
        self.label_reg.setObjectName(_fromUtf8("label_reg"))
        self.gridLayout_2.addWidget(self.label_reg, 0, 1, 1, 1)

        self.resultText = QtGui.QTextBrowser(self.centralwidget)
        self.resultText.setObjectName(_fromUtf8("resultText"))
        self.gridLayout_2.addWidget(self.resultText, 8, 1, 1, 1)

        self.memText = QtGui.QTextBrowser(self.centralwidget)
        self.memText.setObjectName(_fromUtf8("memText"))
        self.gridLayout_2.addWidget(self.memText, 5, 1, 1, 1)

        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.gridLayout_2.addWidget(self.commandLinkButton, 6, 1, 1, 1)

        self.label_mem = QtGui.QLabel(self.centralwidget)
        self.label_mem.setMargin(10)
        self.label_mem.setObjectName(_fromUtf8("label_mem"))
        self.gridLayout_2.addWidget(self.label_mem, 3, 1, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1342, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_2 = QtGui.QMenu(self.menubar)
        self.menu_2.setObjectName(_fromUtf8("menu_2"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.action_new = QtGui.QAction(MainWindow)
        self.action_new.setObjectName(_fromUtf8("action"))
        self.action_new.setShortcut('Ctrl+N')

        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_open.setShortcut('Ctrl+O')

        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_save.setShortcut('Ctrl+S')

        self.action_save_as = QtGui.QAction(MainWindow)
        self.action_save_as.setObjectName(_fromUtf8("action_save_as"))
        self.action_save_as.setShortcut('Ctrl+Shift+A')

        self.action_run = QtGui.QAction(MainWindow)
        self.action_run.setObjectName(_fromUtf8("action_run"))
        self.action_run.setShortcut('F5')

        self.action_debug = QtGui.QAction(MainWindow)
        self.action_debug.setObjectName(_fromUtf8("action_debug"))
        self.action_debug.setShortcut('F7')

        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_save_as)
        self.menu_2.addAction(self.action_run)
        self.menu_2.addAction(self.action_debug)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        QtGui.QCommandLinkButton.connect(self.commandLinkButton, QtCore.SIGNAL('clicked()'), self.next_step)
        self.action_open.connect(self.action_open, QtCore.SIGNAL('triggered()'), self.open_file)
        self.action_new.connect(self.action_new, QtCore.SIGNAL('triggered()'), self.new_file)
        self.action_save.connect(self.action_save, QtCore.SIGNAL('triggered()'), self.save_file)
        self.action_save_as.connect(self.action_save_as, QtCore.SIGNAL('triggered()'), self.save_file_as)
        self.action_run.connect(self.action_run, QtCore.SIGNAL('triggered()'), self.run_file)
        self.action_debug.connect(self.action_debug, QtCore.SIGNAL('triggered()'), self.debug_file)
        self.tabWidget.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested(int)"), self.close_tab)

    def debug_file(self):
        print("debug mode")

    def run_file(self):
        main.main()
        self.regText.setText(main.show_reg())
        self.memText.setText(main.show_mem())

    def close_tab(self):
        # 关闭标签
        i = self.tabWidget.currentIndex()  # 获取当前处于激活状态的标签
        self.tabWidget.removeTab(i)

    def new_file(self):
        self.tab = QtGui.QWidget()
        # self.tab.setObjectName(_fromUtf8("new_tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8("new_tab"))
        self.tabWidget.setTabsClosable(True)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(QtCore.QRect(0, 0, 651, 821)))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "new_tab", None))

    def open_file(self):
        try:
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file', './')
            self.tab = QtGui.QWidget()
            tab_name = str(self.filename.split('/')[-1])
            # self.tab.setObjectName(_fromUtf8(tab_name))
            self.tabWidget.addTab(self.tab, _fromUtf8(tab_name))
            self.tabWidget.setTabsClosable(True)
            self.textEdit = QtGui.QTextEdit(self.tab)
            self.textEdit.setGeometry(QtCore.QRect(0, 0, 651, 821))
            self.textEdit.setObjectName(_fromUtf8("textEdit"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", tab_name, None))
            fp = open(self.filename, encoding="utf-8")
            data = fp.read()
            self.textEdit.setText(data)
            global file_name
            file_name = self.filename

        except UnicodeDecodeError:
            QtGui.QMessageBox.question(None, 'Warning', "Error: Please use utf-8 encoding to input file!")

    def save_file(self):
        if file_name == '':
            self.save_file_as()
        else:
            fp = open(file_name, 'w+')
            data = str(self.textEdit.toPlainText())
            fp.write(data)
            fp.close()

    def save_file_as(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(None, 'save_file_as', './')
        data = str(self.textEdit.toPlainText())
        fp = open(self.filename, 'w')
        fp.write(data)
        fp.close()

    def next_step(self):
        print("linked to next step")


    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "filename", None))
        self.label_result.setText(_translate("MainWindow", "结果", None))
        self.label_reg.setText(_translate("MainWindow", "寄存器", None))
        self.commandLinkButton.setText(_translate("MainWindow", "next", None))
        self.label_mem.setText(_translate("MainWindow", "存储器", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_2.setTitle(_translate("MainWindow", "运行模式", None))
        self.action_new.setText(_translate("MainWindow", "新建", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))
        self.action_save.setText(_translate("MainWindow", "保存", None))
        self.action_save_as.setText(_translate("MainWindow", "另存为", None))
        self.action_run.setText(_translate("MainWindow", "运行", None))
        self.action_debug.setText(_translate("MainWindow", "单步调试", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

