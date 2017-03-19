# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bishe.ui'
#
# Created: Sat Mar 18 14:07:11 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8

    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)
file_name = ""

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1226, 890)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(1040, 160, 141, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 30, 561, 821))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.textBrowser = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(590, 30, 601, 51))
        self.textBrowser.setObjectName(_fromUtf8("textBrowser"))
        self.textBrowser.setReadOnly(True)
        self.textBrowser_2 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(590, 110, 601, 51))
        self.textBrowser_2.setObjectName(_fromUtf8("textBrowser_2"))
        self.textBrowser_2.setReadOnly(True)
        self.textBrowser_3 = QtGui.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(590, 200, 601, 631))
        self.textBrowser_3.setObjectName(_fromUtf8("textBrowser_3"))
        self.textBrowser_3.setReadOnly(True)
        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(590, 10, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(590, 90, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalSlider = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider.setGeometry(QtCore.QRect(150, 820, 160, 22))
        self.horizontalSlider.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider.setObjectName(_fromUtf8("horizontalSlider"))
        self.horizontalSlider_2 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_2.setGeometry(QtCore.QRect(830, 70, 160, 22))
        self.horizontalSlider_2.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_2.setObjectName(_fromUtf8("horizontalSlider_2"))
        self.horizontalSlider_3 = QtGui.QSlider(self.centralwidget)
        self.horizontalSlider_3.setGeometry(QtCore.QRect(830, 150, 160, 22))
        self.horizontalSlider_3.setOrientation(QtCore.Qt.Horizontal)
        self.horizontalSlider_3.setObjectName(_fromUtf8("horizontalSlider_3"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))
        self.menu_run = QtGui.QMenu(self.menubar)
        self.menu_run.setObjectName(_fromUtf8("menu_run"))
        self.menu_debug = QtGui.QMenu(self.menubar)
        self.menu_debug.setObjectName(_fromUtf8("menu_debug"))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)
        self.action_new = QtGui.QAction(MainWindow)
        self.action_new.setObjectName(_fromUtf8("action_new"))
        self.action_open = QtGui.QAction(MainWindow)
        self.action_open.setObjectName(_fromUtf8("action_open"))
        self.action_open.setShortcut('Ctrl+O')
        self.action_save = QtGui.QAction(MainWindow)
        self.action_save.setObjectName(_fromUtf8("action_save"))
        self.action_save.setShortcut('Ctrl+S')
        self.action_save_as = QtGui.QAction(MainWindow)
        self.action_save_as.setObjectName(_fromUtf8("action_save_as"))
        self.action_save_as.setShortcut('Ctrl+Shift+A')
        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_save_as)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_run.menuAction())
        self.menubar.addAction(self.menu_debug.menuAction())

        self.retranslateUi(MainWindow)
        QtGui.QCommandLinkButton.connect(self.commandLinkButton, QtCore.SIGNAL('clicked()'), self.next_step)
        self.action_open.connect(self.action_open, QtCore.SIGNAL('triggered()'), self.open_file)

        self.action_save_as.connect(self.action_save_as, QtCore.SIGNAL('triggered()'), self.save_file_as)

    def open_file(self):
        try:
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file', '/home')
            fname = open(self.filename, encoding="utf-8")
            data = fname.read()
            self.textEdit.setText(data)
        except UnicodeDecodeError:
            QtGui.QMessageBox.question(None, 'Warning', "Error: Please use utf-8 encoding to input file!")
        file_name = self.filename

    def save_file(self):
        fp = open(file_name, 'w+')
        data = str(self.textEdit.toPlainText())
        fp.write(data)
        fp.close()

    def save_file_as(self):
        self.filename = QtGui.QFileDialog.getSaveFileName(None, 'save_file', './')
        data = str(self.textEdit.toPlainText())
        fp = open(self.filename, 'w')
        fp.write(data)
        fp.close()
    def next_step(self):
        print("linked to next step")

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "next", None))
        self.textEdit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'SimSun\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.label.setText(_translate("MainWindow", "寄存器", None))
        self.label_2.setText(_translate("MainWindow", "存储器", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.menu_run.setTitle(_translate("MainWindow", "运行", None))
        self.menu_debug.setTitle(_translate("MainWindow", "调试", None))
        self.action_new.setText(_translate("MainWindow", "新建", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))
        self.action_save.setText(_translate("MainWindow", "保存", None))
        self.action_save_as.setText(_translate("MainWindow", "另存为", None))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

