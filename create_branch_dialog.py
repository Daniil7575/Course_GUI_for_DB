# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\spovt\Documents\GitHub\Course_GUI_for_DB\create_branch_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(500, 260)
        Dialog.setStyleSheet("QWidget { background-color: rgb(13, 17, 23); } \n"
"/* QFrame { border: 2px solid rgb(0, 191, 255) } */\n"
"QTextEdit {\n"
"    background-color: rgb(13, 17, 23);\n"
"    color: rgb(255,255,255);\n"
"    font: bold 18px\n"
"}\n"
"QLineEdit {\n"
"    border: 2px solid rgb(0, 191, 255);\n"
"    border-radius: 7px;\n"
"    background-color: rgb(13, 17, 23);\n"
"    color: rgb(255,255,255);\n"
"    font: 14px\n"
"}\n"
"QPushButton {\n"
"    border-radius: 7px;\n"
"    border: 2px solid rgb(35, 134, 54);\n"
"    background-color: rgb(35, 134, 54);\n"
"    color: white;\n"
"    font: bold 16px\n"
"}\n"
"QPushButton#cancelButton {\n"
"    border-radius: 7px;\n"
"    border: 2px solid rgb(180, 0, 0);\n"
"    background-color: rgb(180, 0, 0);\n"
"    color: white;\n"
"    font: bold 16px\n"
"}\n"
"")
        self.createRepButton = QtWidgets.QPushButton(Dialog)
        self.createRepButton.setGeometry(QtCore.QRect(10, 220, 231, 31))
        self.createRepButton.setObjectName("createRepButton")
        self.passTextEdit = QtWidgets.QTextEdit(Dialog)
        self.passTextEdit.setGeometry(QtCore.QRect(10, 70, 181, 31))
        self.passTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.passTextEdit.setReadOnly(True)
        self.passTextEdit.setObjectName("passTextEdit")
        self.description = QtWidgets.QLineEdit(Dialog)
        self.description.setGeometry(QtCore.QRect(10, 110, 481, 41))
        self.description.setText("")
        self.description.setObjectName("description")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(260, 220, 231, 31))
        self.cancelButton.setObjectName("cancelButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.createRepButton.setText(_translate("Dialog", "Create repository"))
        self.passTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">Name</span></p></body></html>"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
