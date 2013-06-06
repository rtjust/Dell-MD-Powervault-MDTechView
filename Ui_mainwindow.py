# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'D:\Dropbox\Projects\MDTechView\MDTechView\MDTechView\mainwindow.ui'
#
# Created: Tue Apr 30 10:21:23 2013
#      by: PyQt4 UI code generator 4.10.1
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

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName(_fromUtf8("MainWindow"))
        MainWindow.resize(1032, 855)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.tabWidget = QtGui.QTabWidget(self.centralwidget)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 1021, 721))
        self.tabWidget.setStyleSheet(_fromUtf8(""))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.webView = QtWebKit.QWebView(self.tab_2)
        self.webView.setGeometry(QtCore.QRect(10, 10, 991, 661))
        self.webView.setUrl(QtCore.QUrl(_fromUtf8("about:blank")))
        self.webView.setObjectName(_fromUtf8("webView"))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.textSAP = Qsci.QsciScintilla(self.tab)
        self.textSAP.setGeometry(QtCore.QRect(10, 10, 991, 681))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textSAP.setFont(font)
        self.textSAP.setToolTip(_fromUtf8(""))
        self.textSAP.setWhatsThis(_fromUtf8(""))
        self.textSAP.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textSAP.setObjectName(_fromUtf8("textSAP"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_3 = QtGui.QWidget()
        self.tab_3.setObjectName(_fromUtf8("tab_3"))
        self.textMEL = Qsci.QsciScintilla(self.tab_3)
        self.textMEL.setGeometry(QtCore.QRect(10, 10, 991, 321))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textMEL.setFont(font)
        self.textMEL.setToolTip(_fromUtf8(""))
        self.textMEL.setWhatsThis(_fromUtf8(""))
        self.textMEL.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textMEL.setObjectName(_fromUtf8("textMEL"))
        self.tableWidget = QtGui.QTableWidget(self.tab_3)
        self.tableWidget.setGeometry(QtCore.QRect(10, 340, 991, 321))
        self.tableWidget.setObjectName(_fromUtf8("tableWidget"))
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.pushButton_2 = QtGui.QPushButton(self.tab_3)
        self.pushButton_2.setGeometry(QtCore.QRect(910, 660, 93, 28))
        self.pushButton_2.setObjectName(_fromUtf8("pushButton_2"))
        self.tabWidget.addTab(self.tab_3, _fromUtf8(""))
        self.tab_4 = QtGui.QWidget()
        self.tab_4.setObjectName(_fromUtf8("tab_4"))
        self.textStateCap = Qsci.QsciScintilla(self.tab_4)
        self.textStateCap.setGeometry(QtCore.QRect(10, 10, 991, 681))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textStateCap.setFont(font)
        self.textStateCap.setToolTip(_fromUtf8(""))
        self.textStateCap.setWhatsThis(_fromUtf8(""))
        self.textStateCap.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textStateCap.setObjectName(_fromUtf8("textStateCap"))
        self.tabWidget.addTab(self.tab_4, _fromUtf8(""))
        self.tab_5 = QtGui.QWidget()
        self.tab_5.setObjectName(_fromUtf8("tab_5"))
        self.textiSCSI = Qsci.QsciScintilla(self.tab_5)
        self.textiSCSI.setGeometry(QtCore.QRect(10, 10, 991, 681))
        font = QtGui.QFont()
        font.setFamily(_fromUtf8("Consolas"))
        font.setPointSize(8)
        font.setBold(False)
        font.setItalic(False)
        font.setUnderline(False)
        font.setWeight(50)
        font.setStrikeOut(False)
        self.textiSCSI.setFont(font)
        self.textiSCSI.setToolTip(_fromUtf8(""))
        self.textiSCSI.setWhatsThis(_fromUtf8(""))
        self.textiSCSI.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOn)
        self.textiSCSI.setObjectName(_fromUtf8("textiSCSI"))
        self.tabWidget.addTab(self.tab_5, _fromUtf8(""))
        self.pushButton = QtGui.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(920, 790, 93, 28))
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.labelPath = QtGui.QLabel(self.centralwidget)
        self.labelPath.setGeometry(QtCore.QRect(160, 790, 751, 20))
        self.labelPath.setTextFormat(QtCore.Qt.PlainText)
        self.labelPath.setObjectName(_fromUtf8("labelPath"))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1032, 26))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(_translate("MainWindow", "MD TechView Concept - NOT FINAL SOFTWARE", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Recovery Guru", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Array Profile", None))
        self.pushButton_2.setText(_translate("MainWindow", "Parse into list", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "MEL", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), _translate("MainWindow", "State Capture", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), _translate("MainWindow", "iSCSI Sessions", None))
        self.pushButton.setText(_translate("MainWindow", "Open Bundle", None))
        self.labelPath.setText(_translate("MainWindow", "Current Bundle Path:  ", None))

from PyQt4 import Qsci
from PyQt4 import QtWebKit

if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

