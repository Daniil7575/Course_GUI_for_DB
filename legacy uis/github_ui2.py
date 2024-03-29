# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\spovt\Documents\GitHub\Course_GUI_for_DB\github3.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1920, 1080)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setLayoutDirection(QtCore.Qt.LeftToRight)
        MainWindow.setStyleSheet("QWidget { background-color: rgb(13, 17, 23); } \n"
"QFrame { border: 2px solid rgb(0, 191, 255) } \n"
"QComboBox QAbstractItemView {\n"
"  border: 2px solid rgb(128, 0, 128);\n"
"  background: white;\n"
"  selection-background-color: grey;\n"
"}\n"
"QComboBox {\n"
"  border: black;\n"
"  background: grey;\n"
"  color: white;\n"
"  font-size: 20px;\n"
"}\n"
"QTextEdit {\n"
" color: #ffffff;\n"
"}")
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.repositoryList = QtWidgets.QListWidget(self.centralwidget)
        self.repositoryList.setGeometry(QtCore.QRect(10, 20, 241, 551))
        self.repositoryList.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.repositoryList.setStyleSheet("")
        self.repositoryList.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.repositoryList.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.repositoryList.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.repositoryList.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.repositoryList.setObjectName("repositoryList")
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        font.setWeight(75)
        font.setKerning(True)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        # self.repositoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        # self.repositoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setItalic(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        # self.repositoryList.addItem(item)
        item = QtWidgets.QListWidgetItem()
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        item.setFont(font)
        brush = QtGui.QBrush(QtGui.QColor(0, 0, 0))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setBackground(brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 255, 255))
        brush.setStyle(QtCore.Qt.NoBrush)
        item.setForeground(brush)
        # self.repositoryList.addItem(item)
        self.branchesComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.branchesComboBox.setGeometry(QtCore.QRect(260, 20, 191, 51))
        self.branchesComboBox.setFrame(True)
        self.branchesComboBox.setObjectName("branchesComboBox")
        # self.branchesComboBox.addItem("")
        # self.branchesComboBox.addItem("")
        # self.branchesComboBox.addItem("")
        self.commitsComboBox = QtWidgets.QComboBox(self.centralwidget)
        self.commitsComboBox.setGeometry(QtCore.QRect(460, 20, 401, 51))
        self.commitsComboBox.setFrame(True)
        self.commitsComboBox.setObjectName("commitsComboBox")
        # self.commitsComboBox.addItem("")
        # self.commitsComboBox.addItem("")
        # self.commitsComboBox.addItem("")
        self.currentBranch = QtWidgets.QTextEdit(self.centralwidget)
        self.currentBranch.setGeometry(QtCore.QRect(260, 80, 371, 31))
        self.currentBranch.setStyleSheet("QTextEdit { border: none }")
        self.currentBranch.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentBranch.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.currentBranch.setReadOnly(True)
        self.currentBranch.setObjectName("currentBranch")
        self.horizontalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(260, 220, 811, 351))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.codeText = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.codeText.setObjectName("codeText")
        self.horizontalLayout.addWidget(self.codeText)
        self.modelText = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.modelText.setObjectName("modelText")
        self.horizontalLayout.addWidget(self.modelText)
        self.datasetText = QtWidgets.QTextEdit(self.horizontalLayoutWidget)
        self.datasetText.setObjectName("datasetText")
        self.horizontalLayout.addWidget(self.datasetText)
        self.currentCommit = QtWidgets.QTextEdit(self.centralwidget)
        self.currentCommit.setGeometry(QtCore.QRect(260, 100, 371, 31))
        self.currentCommit.setStyleSheet("QTextEdit { border: none }")
        self.currentCommit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.currentCommit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.currentCommit.setReadOnly(True)
        self.currentCommit.setObjectName("currentCommit")
        self.lastCommitOwner = QtWidgets.QTextEdit(self.centralwidget)
        self.lastCommitOwner.setGeometry(QtCore.QRect(870, 10, 171, 31))
        self.lastCommitOwner.setStyleSheet("QTextEdit { border: none }")
        self.lastCommitOwner.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lastCommitOwner.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lastCommitOwner.setReadOnly(True)
        self.lastCommitOwner.setObjectName("lastCommitOwner")
        self.lastCommitDate = QtWidgets.QTextEdit(self.centralwidget)
        self.lastCommitDate.setGeometry(QtCore.QRect(870, 40, 211, 31))
        self.lastCommitDate.setStyleSheet("QTextEdit { border: none }")
        self.lastCommitDate.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.lastCommitDate.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.lastCommitDate.setReadOnly(True)
        self.lastCommitDate.setObjectName("lastCommitDate")
        self.summary = QtWidgets.QTextEdit(self.centralwidget)
        self.summary.setGeometry(QtCore.QRect(640, 80, 431, 51))
        self.summary.setStyleSheet("")
        self.summary.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.summary.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.summary.setReadOnly(True)
        self.summary.setObjectName("summary")
        self.description = QtWidgets.QTextEdit(self.centralwidget)
        self.description.setGeometry(QtCore.QRect(260, 140, 811, 71))
        self.description.setStyleSheet("")
        self.description.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.description.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.description.setReadOnly(True)
        self.description.setObjectName("description")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1080, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        # self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        __sortingEnabled = self.repositoryList.isSortingEnabled()
        self.repositoryList.setSortingEnabled(False)
        item = self.repositoryList.item(0)
        item.setText(_translate("MainWindow", "im2latex"))
        item = self.repositoryList.item(1)
        item.setText(_translate("MainWindow", "a very very very very long deeec"))
        item = self.repositoryList.item(2)
        item.setText(_translate("MainWindow", "latexOCRserver"))
        item = self.repositoryList.item(3)
        item.setText(_translate("MainWindow", "TensorSnake"))
        self.repositoryList.setSortingEnabled(__sortingEnabled)
        self.branchesComboBox.setItemText(0, _translate("MainWindow", "master"))
        self.branchesComboBox.setItemText(1, _translate("MainWindow", "bebra1"))
        self.branchesComboBox.setItemText(2, _translate("MainWindow", "bebra2"))
        self.commitsComboBox.setItemText(0, _translate("MainWindow", "\"summary_bebra\" by user1 on 0001-01-1 "))
        self.commitsComboBox.setItemText(1, _translate("MainWindow", "\"summary_xui\" by user2 on 0002-01-1"))
        self.commitsComboBox.setItemText(2, _translate("MainWindow", "\"summary_deeec\" by user3 on 0003-01-1"))
        self.currentBranch.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:7pt; color:#ffffff;\">current branch uuid: c2d29867-3d0b-d497-bbbb-18a9d8ee7830</span></p></body></html>"))
        self.currentCommit.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:7pt; color:#ffffff;\">current commit uuid: c2d29867-3d0b-d497-cccc-18a9d8ee7830</span></p></body></html>"))
        self.lastCommitOwner.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#ffffff;\">last commit by </span><span style=\" font-family:\'Arial\'; font-size:10pt; text-decoration: underline; color:#ffffff;\">pavviaz</span></p></body></html>"))
        self.lastCommitDate.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#ffffff;\">commited on 0001-01-1</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:10pt; color:#ffffff;\"><br /></p></body></html>"))
        self.summary.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#ffffff;\">Summary: Init commit. Added some shit</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'Arial\'; font-size:10pt; color:#ffffff;\"><br /></p></body></html>"))
        self.description.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'Arial\'; font-size:10pt; color:#ffffff;\">Description: I dont know what I should write here. Okay, I added a bunch of new fucking code. Thats All?</span></p></body></html>"))
