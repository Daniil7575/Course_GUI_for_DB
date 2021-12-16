# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Xiaomi\Documents\GitHub\Course_GUI_for_DB\user_info_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(251, 403)
        Dialog.setStyleSheet("QWidget { background-color: rgb(13, 17, 23); } \n"
"/* QFrame { border: 2px solid rgb(0, 191, 255) } */\n"
"QTextEdit {\n"
"    background-color: rgb(13, 17, 23);\n"
"    color: rgb(255,255,255);\n"
"    font: bold 22px\n"
"}\n"
"\n"
"QLineEdit {\n"
"    background-color: rgb(13, 17, 23);\n"
"    color: rgb(255,255,255);\n"
"    font: 14px\n"
"}\n"
"QTextEdit#loginTextEdit{\n"
"    background-color: rgb(13, 17, 23);\n"
"    color: grey;\n"
"    font-size: 22px\n"
"}\n"
"QPushButton {\n"
"    border-radius: 7px;\n"
"    border: 2px solid rgb(35, 134, 54);\n"
"    background-color: rgb(35, 134, 54);\n"
"    color: white;\n"
"    font: bold 16px\n"
"}\n"
"QPushButton#exitButton {\n"
"    border-radius: 7px;\n"
"    border: 2px solid rgb(180, 0, 0);\n"
"    background-color: rgb(180, 0, 0);\n"
"    color: white;\n"
"    font: bold 16px\n"
"}\n"
"")
        self.infoTextEdit = QtWidgets.QTextEdit(Dialog)
        self.infoTextEdit.setGeometry(QtCore.QRect(20, 30, 101, 31))
        self.infoTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.infoTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.infoTextEdit.setReadOnly(True)
        self.infoTextEdit.setObjectName("infoTextEdit")
        self.nameTextEdit = QtWidgets.QTextEdit(Dialog)
        self.nameTextEdit.setGeometry(QtCore.QRect(20, 70, 211, 31))
        self.nameTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nameTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nameTextEdit.setReadOnly(True)
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.loginTextEdit = QtWidgets.QTextEdit(Dialog)
        self.loginTextEdit.setGeometry(QtCore.QRect(20, 100, 211, 31))
        self.loginTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.loginTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loginTextEdit.setReadOnly(True)
        self.loginTextEdit.setObjectName("loginTextEdit")
        self.descTextEdit = QtWidgets.QTextEdit(Dialog)
        self.descTextEdit.setGeometry(QtCore.QRect(20, 150, 211, 101))
        self.descTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.descTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descTextEdit.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.descTextEdit.setReadOnly(True)
        self.descTextEdit.setObjectName("descTextEdit")
        self.geoTextEdit = QtWidgets.QTextEdit(Dialog)
        self.geoTextEdit.setGeometry(QtCore.QRect(20, 270, 211, 31))
        self.geoTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.geoTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.geoTextEdit.setReadOnly(True)
        self.geoTextEdit.setObjectName("geoTextEdit")
        self.statsButton = QtWidgets.QPushButton(Dialog)
        self.statsButton.setGeometry(QtCore.QRect(10, 320, 231, 31))
        self.statsButton.setObjectName("statsButton")
        self.exitButton = QtWidgets.QPushButton(Dialog)
        self.exitButton.setGeometry(QtCore.QRect(10, 360, 231, 31))
        self.exitButton.setObjectName("exitButton")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.infoTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px;\">User info:</span></p></body></html>"))
        self.nameTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">Name</span></p></body></html>"))
        self.loginTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:400;\">login</span></p></body></html>"))
        self.descTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">Desc</span></p></body></html>"))
        self.geoTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:22px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:12pt; font-weight:400;\">Geo</span></p></body></html>"))
        self.statsButton.setText(_translate("Dialog", "Dump statistics"))
        self.exitButton.setText(_translate("Dialog", "Cancel"))
