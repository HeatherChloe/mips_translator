# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'bishe.ui'
#
# Created: Sat Mar 18 14:07:11 2017
#      by: PyQt4 UI code generator 4.10.3
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui
from PyQt4.QtGui import QMainWindow

import common
import cons
import if_opt_equals
import main
from cons import name_and_tab
from queue_works import debugQueue

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

# name_and_tab = {}
# debug_job = None


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.filename = ''
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1335, 890)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.commandLinkButton = QtGui.QCommandLinkButton(self.centralwidget)
        self.commandLinkButton.setGeometry(QtCore.QRect(1200, 0, 141, 41))
        self.commandLinkButton.setObjectName(_fromUtf8("commandLinkButton"))
        ########################
        #       TAB AREA       #
        ########################
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(20, 10, 631, 750))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tabWidget.setTabsClosable(True)

        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))

        MainWindow.setCentralWidget(self.centralwidget)
        ########################
        #      TEXT AREA       #
        ########################
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(0, 0, 625, 750))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        name_and_tab[0] = "already"
        # self.regText = QtGui.QTextBrowser(self.centralwidget)
        # self.regText.setGeometry(QtCore.QRect(710, 30, 601, 51))
        # self.regText.setObjectName(_fromUtf8("regText"))

        # self.regText.setReadOnly(True)

        # self.memText = QtGui.QTextBrowser(self.centralwidget)
        # self.memText.setGeometry(QtCore.QRect(710, 110, 601, 51))
        # self.memText.setObjectName(_fromUtf8("memText"))
        # self.memText.setReadOnly(True)

        self.resultText = QtGui.QTextBrowser(self.centralwidget)
        self.resultText.setGeometry(QtCore.QRect(710, 50, 601, 750))
        self.resultText.setObjectName(_fromUtf8("resultText"))
        self.resultText.setReadOnly(True)

        self.label = QtGui.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(730, 10, 72, 15))
        self.label.setObjectName(_fromUtf8("label"))
        self.label_2 = QtGui.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(730, 90, 72, 15))
        self.label_2.setObjectName(_fromUtf8("label_2"))

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1226, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))

        self.menu = QtGui.QMenu(self.menubar)
        self.menu.setObjectName(_fromUtf8("menu"))

        self.run_or_debug = QtGui.QMenu(self.menubar)
        self.run_or_debug.setObjectName(_fromUtf8("run_or_debug"))

        self.regAndMem = QtGui.QMenu(self.menubar)
        self.regAndMem.setObjectName(_fromUtf8("regAndMem"))

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        MainWindow.setStatusBar(self.statusbar)

        self.action_run = QtGui.QAction(MainWindow)
        self.action_run.setObjectName(_fromUtf8("action_run"))
        self.action_run.setShortcut('F5')

        self.action_debug = QtGui.QAction(MainWindow)
        self.action_debug.setObjectName(_fromUtf8("action_debug"))
        self.action_debug.setShortcut('F7')

        self.action_new = QtGui.QAction(MainWindow)
        self.action_new.setObjectName(_fromUtf8("action_new"))
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

        self.action_regShow = QtGui.QAction(MainWindow)
        self.action_regShow.setObjectName(_fromUtf8("action_regShow"))
        self.action_regShow.setShortcut('Ctrl+Shift+R')

        self.action_memShow = QtGui.QAction(MainWindow)
        self.action_memShow.setObjectName(_fromUtf8("action_memShow"))
        self.action_memShow.setShortcut('Ctrl+Shift+M')

        self.action_clear = QtGui.QAction(MainWindow)
        self.action_clear.setObjectName(_fromUtf8("action_clear"))
        self.action_clear.setShortcut('Ctrl+L')

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.run_or_debug.menuAction())
        self.menubar.addAction(self.regAndMem.menuAction())

        self.menu.addAction(self.action_new)
        self.menu.addAction(self.action_open)
        self.menu.addAction(self.action_save)
        self.menu.addAction(self.action_save_as)

        self.run_or_debug.addAction(self.action_run)
        self.run_or_debug.addAction(self.action_debug)

        self.regAndMem.addAction(self.action_regShow)
        self.regAndMem.addAction(self.action_memShow)
        self.regAndMem.addAction(self.action_clear)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)

        self.regwindow = RegWindow()
        self.memwindow = MemWindow()
        ########################
        #     CONNECT AREA     #
        ########################
        QtGui.QCommandLinkButton.connect(self.commandLinkButton, QtCore.SIGNAL('clicked()'), self.next_step)
        self.action_open.connect(self.action_open, QtCore.SIGNAL('triggered()'), self.open_file)
        self.action_new.connect(self.action_new, QtCore.SIGNAL('triggered()'), self.new_file)
        self.action_save.connect(self.action_save, QtCore.SIGNAL('triggered()'), self.save_file)
        self.action_save_as.connect(self.action_save_as, QtCore.SIGNAL('triggered()'), self.save_file_as)
        self.action_run.connect(self.action_run, QtCore.SIGNAL('triggered()'), self.run_file)
        self.action_debug.connect(self.action_debug, QtCore.SIGNAL('triggered()'), self.debug_file)
        self.action_clear.connect(self.action_clear, QtCore.SIGNAL('triggered()'), self.clear_all)
        self.action_regShow.connect(self.action_regShow, QtCore.SIGNAL('triggered()'), self.showRegResult)
        self.action_memShow.connect(self.action_memShow, QtCore.SIGNAL('triggered()'), self.showMemResult)
        self.tabWidget.connect(self.tabWidget, QtCore.SIGNAL("tabCloseRequested(int)"), self.close_tab)

    def clear_all(self):
        self.resultText.clear()
        self.regwindow.regText.clear()
        self.memwindow.memText.clear()

    def showRegResult(self):
        self.regwindow.show()

    def showMemResult(self):
        self.memwindow.show()

    def run_file(self):

        curr_index = self.tabWidget.currentIndex()
        file_name = name_and_tab.get(curr_index)
        opt_list_with_line_num = main.to_opt_list(file_name)
        main.main(opt_list_with_line_num)
        code_result = if_opt_equals.result_str
        self.resultText.setText(code_result)
        self.regwindow.regText.setText(common.result_reg)
        self.memwindow.memText.setText(common.result_mem)

    # def eventListener(self):
    #     try:
    #         curr_index = self.tabWidget.currentIndex()
    #         file_name = name_and_tab.get(curr_index)
    #         opt_list_with_line_num = main.to_opt_list(file_name)
    #
    #         count = 0
    #         if cons.next_flag is True:
    #             opt = opt_list_with_line_num[count]
    #             main.if_opt_eqs_func(opt, main.reg_list, main.mem_list, opt_list_with_line_num)
    #             count += 1
    #             cons.next_flag = False
    #             code_result = if_opt_equals.result_str
    #             self.resultText.setText(code_result)
    #             # self.regwindow.regText.setText(common.result_reg)
    #             # self.memwindow.memText.setText(common.result_mem)
    #     except Exception as e:
    #         print(e)
    #         print(trace)

    def debug_file(self):
        cons.count = 0
        cons.line_num = None
        cons.changed_reg = None
        cons.changed_mem = None
        cons.data = None
        if_opt_equals.result_str = ''
        main.reg_list = []
        for i in range(0, 32):
            main.reg_list.append(0)
        main.mem_list = {}
        # self.regwindow.regText.setText("123123")
        for each in main.reg_list:
            self.regwindow.regText.append(str(main.reg_list.index(each)) + ':' + str(each) + '\n')
        # self.regwindow.regText.setText(common.result_reg)
        # self.memwindow.memText.setText(common.result_mem)
        curr_index = self.tabWidget.currentIndex()
        file_name = name_and_tab.get(curr_index)
        opt_list_with_line_num = main.to_opt_list(file_name)
        cons.debug_obj = debugQueue(main.reg_list, main.mem_list, opt_list_with_line_num)
        # self.regwindow.regText.setText(common.result_reg)
        # self.memwindow.memText.setText(common.result_mem)

    def close_idx(self, curr_index):
        b = {}
        for k, v in cons.name_and_tab.items():
            if k < curr_index:
                b[k] = v
            if k > curr_index:
                b[k - 1] = v
        cons.name_and_tab = b

    def close_tab(self):
        # 关闭标签
        curr_index = self.tabWidget.currentIndex()  # 获取当前处于激活状态的标签
        self.tabWidget.removeTab(curr_index)
        name_and_tab.pop(curr_index)
        self.close_idx(curr_index)
        print(name_and_tab)

    def next_step(self):
        cons.debug_obj.q_pop(cons.count)
        cons.count += 1
        code_result = if_opt_equals.result_str
        last_step = ''.join(code_result.split('\n\n')[-2])

        before_last_step_lst = '\n\n'.join(code_result.split('\n\n')[:-2])
        self.resultText.append('\n\n')
        self.resultText.setText(before_last_step_lst)
        self.resultText.append('\n\n')
        self.resultText.append("<font color=\"#ec0053\">%s</font>" % last_step)

        ####debug show reg####
        if cons.changed_reg:
            reg_list = common.result_reg.split('\n')
            for reg_each in reg_list:
                try:
                    if reg_each:
                        c_reg = int(reg_each.split(':')[0])
                except Exception as e:
                    print(e)
                if c_reg == cons.changed_reg:
                    index_target = int(common.result_reg.index(reg_each))
                    reg_before = common.result_reg[:index_target]
                    reg_after = common.result_reg[index_target:].split('\n')[1:]
                    self.regwindow.regText.setText(str(reg_before))
                    self.regwindow.regText.append("<font color=\"#ec0053\">%s</font>" % reg_each)
                    self.regwindow.regText.append('\n'.join(reg_after))
                    break
        if cons.changed_mem:
            mem_list = common.result_mem.split('\n')[:-1]
            for each in mem_list:
                if int(each.split(':')[0]) == cons.changed_mem:
                    try:
                        index_mem = mem_list.index(each)
                        mem_before = mem_list[:index_mem]
                        mem_after = mem_list[index_mem+1:]
                        if mem_before:
                            result_m = ''
                            for each_n in mem_before:
                                result_m += each_n + '\n'
                            self.memwindow.memText.setText(result_m)
                        self.memwindow.memText.append("<font color=\"#ec0053\">%s</font>" % each)
                        if mem_after:
                            self.memwindow.memText.append('\n'.join(mem_after))
                        break
                    except Exception as e:
                        print(e)
        if cons.changed_line:
            try:
                file_list = cons.data
                file_fore = file_list[:int(cons.changed_line)-1]
                file_after = file_list[int(cons.changed_line):]
                if file_fore:
                    result_f = ""
                    for each_line_fore in file_fore:
                        result_f += each_line_fore
                    self.textEdit.setText(result_f)
                self.textEdit.append("<font color=\"#ec0053\">%s</font>" % file_list[int(cons.changed_line)-1])
                if file_after:
                    result_a = ""
                    for each_a in file_after:
                        result_a += each_a
                    self.textEdit.append(result_a)
            except Exception as e:
                print(e)

    def new_file(self):
        self.tab = QtGui.QWidget()
        self.tabWidget.addTab(self.tab, _fromUtf8("new_tab"))
        self.tabWidget.setTabsClosable(True)
        curr_index = self.tabWidget.currentIndex()
        print(curr_index)
        name_and_tab[curr_index+1] = ""
        print(name_and_tab)
        self.textEdit = QtGui.QTextEdit(self.tab)
        self.textEdit.setGeometry(QtCore.QRect(QtCore.QRect(0, 0, 625, 750)))
        self.textEdit.setObjectName(_fromUtf8("textEdit"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "new_tab", None))

    def open_file(self):
        try:
            self.tab = QtGui.QWidget()
            self.filename = QtGui.QFileDialog.getOpenFileName(None, 'Open file', './')

            tab_name = str(self.filename.split('/')[-1])
            self.tabWidget.setTabsClosable(True)
            self.textEdit = QtGui.QTextEdit(self.tab)
            self.textEdit.setGeometry(QtCore.QRect(0, 0, 571, 750))
            self.textEdit.setObjectName(_fromUtf8("textEdit"))
            self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", tab_name, None))
            self.tabWidget.addTab(self.tab, _fromUtf8(tab_name))
            curr_index = self.tabWidget.currentIndex()
            if curr_index == 0 and name_and_tab.get(curr_index) != "already":
                name_and_tab[curr_index] = self.filename
            else:
                name_and_tab[curr_index + 1] = self.filename

            fp = open(self.filename, encoding="utf-8")
            data = fp.read()
            self.textEdit.setText(data)
            self.resultText.setText('')
            self.regwindow.regText.setText('')
            self.memwindow.memText.setText('')
        except UnicodeDecodeError:
            QtGui.QMessageBox.question(None, 'Warning', "Error: Please use utf-8 encoding to input file!")

    def save_file(self):
        curr_index = self.tabWidget.currentIndex()
        file_name = name_and_tab[curr_index]
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
        curr_index = self.tabWidget.currentIndex()
        file_name = name_and_tab[curr_index]
        name_and_tab[curr_index] = file_name

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow", None))
        self.commandLinkButton.setText(_translate("MainWindow", "next", None))
        self.menu.setTitle(_translate("MainWindow", "文件", None))
        self.action_new.setText(_translate("MainWindow", "新建", None))
        self.action_open.setText(_translate("MainWindow", "打开", None))
        self.action_save.setText(_translate("MainWindow", "保存", None))
        self.action_save_as.setText(_translate("MainWindow", "另存为", None))

        self.run_or_debug.setTitle(_translate("MainWindow", "运行模式", None))
        self.action_run.setText(_translate("MainWindow", "运行", None))
        self.action_debug.setText(_translate("MainWindow", "单步调试", None))

        self.regAndMem.setTitle(_translate("MainWindow", "查看", None))
        self.action_regShow.setText(_translate("MainWindow", "寄存器", None))
        self.action_memShow.setText(_translate("MainWindow", "存储器", None))
        self.action_clear.setText(_translate("MainWindow", "清屏", None))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "file_name", None))
        self.tabWidget.setCurrentIndex(0)


class RegWindow(QMainWindow):
    def __init__(self):
        super(RegWindow, self).__init__()
        self.resize(800, 1200)
        self.regText = QtGui.QTextBrowser(self)
        self.regText.setGeometry(QtCore.QRect(0, 0, 800, 1200))
        self.regText.setObjectName(_fromUtf8("regText"))
        self.setWindowTitle("this is reg window")
        self.regText.setText("this is reg")


class MemWindow(QMainWindow):
    def __init__(self):
        super(MemWindow, self).__init__()
        self.resize(800, 1200)
        self.memText = QtGui.QTextBrowser(self)
        self.memText.setGeometry(QtCore.QRect(0, 0, 800, 1200))
        self.memText.setObjectName(_fromUtf8("memText"))
        self.setWindowTitle("this is mem window")


def ui_main():
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    ui_main()
