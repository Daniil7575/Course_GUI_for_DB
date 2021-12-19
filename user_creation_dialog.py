# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\Xiaomi\Documents\GitHub\Course_GUI_for_DB\user_creation_dialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(441, 444)
        Dialog.setStyleSheet("QWidget { background-color: rgb(13, 17, 23); } \n"
"\n"
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
"}")
        self.loginTextEdit = QtWidgets.QTextEdit(Dialog)
        self.loginTextEdit.setGeometry(QtCore.QRect(20, 20, 181, 31))
        self.loginTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.loginTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.loginTextEdit.setReadOnly(True)
        self.loginTextEdit.setObjectName("loginTextEdit")
        self.newUserLogin = QtWidgets.QLineEdit(Dialog)
        self.newUserLogin.setGeometry(QtCore.QRect(20, 60, 191, 31))
        self.newUserLogin.setText("")
        self.newUserLogin.setObjectName("newUserLogin")
        self.nameTextEdit = QtWidgets.QTextEdit(Dialog)
        self.nameTextEdit.setGeometry(QtCore.QRect(20, 100, 181, 31))
        self.nameTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.nameTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.nameTextEdit.setReadOnly(True)
        self.nameTextEdit.setObjectName("nameTextEdit")
        self.newUserName = QtWidgets.QLineEdit(Dialog)
        self.newUserName.setGeometry(QtCore.QRect(20, 140, 401, 31))
        self.newUserName.setText("")
        self.newUserName.setObjectName("newUserName")
        self.newUserAbout = QtWidgets.QLineEdit(Dialog)
        self.newUserAbout.setGeometry(QtCore.QRect(20, 220, 401, 81))
        self.newUserAbout.setText("")
        self.newUserAbout.setObjectName("newUserAbout")
        self.aboutTextEdit = QtWidgets.QTextEdit(Dialog)
        self.aboutTextEdit.setGeometry(QtCore.QRect(20, 180, 181, 31))
        self.aboutTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.aboutTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.aboutTextEdit.setReadOnly(True)
        self.aboutTextEdit.setObjectName("aboutTextEdit")
        self.geoTextEdit = QtWidgets.QTextEdit(Dialog)
        self.geoTextEdit.setGeometry(QtCore.QRect(20, 310, 181, 31))
        self.geoTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.geoTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.geoTextEdit.setReadOnly(True)
        self.geoTextEdit.setObjectName("geoTextEdit")
        self.newUserGeo = QtWidgets.QLineEdit(Dialog)
        self.newUserGeo.setGeometry(QtCore.QRect(20, 350, 401, 31))
        self.newUserGeo.setText("")
        self.newUserGeo.setObjectName("newUserGeo")
        self.createUserButton = QtWidgets.QPushButton(Dialog)
        self.createUserButton.setGeometry(QtCore.QRect(20, 400, 191, 31))
        self.createUserButton.setObjectName("createUserButton")
        self.cancelButton = QtWidgets.QPushButton(Dialog)
        self.cancelButton.setGeometry(QtCore.QRect(230, 400, 191, 31))
        self.cancelButton.setObjectName("cancelButton")
        self.newUserPass = QtWidgets.QLineEdit(Dialog)
        self.newUserPass.setGeometry(QtCore.QRect(230, 60, 191, 31))
        self.newUserPass.setText("")
        self.newUserPass.setObjectName("newUserPass")
        self.passTextEdit = QtWidgets.QTextEdit(Dialog)
        self.passTextEdit.setGeometry(QtCore.QRect(230, 20, 181, 31))
        self.passTextEdit.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.passTextEdit.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.passTextEdit.setReadOnly(True)
        self.passTextEdit.setObjectName("passTextEdit")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.loginTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">Login </span><span style=\" font-size:18px; font-weight:400; color:#f14d46;\">*</span></p></body></html>"))
        self.nameTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">Name </span><span style=\" font-size:9pt; font-weight:400; color:#6d6d6d;\">(optional)</span></p></body></html>"))
        self.aboutTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">About myself </span><span style=\" font-size:9pt; font-weight:400; color:#6d6d6d;\">(optional)</span></p></body></html>"))
        self.geoTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">Geolocation </span><span style=\" font-size:9pt; font-weight:400; color:#6d6d6d;\">(optional)</span></p></body></html>"))
        self.createUserButton.setText(_translate("Dialog", "Register"))
        self.cancelButton.setText(_translate("Dialog", "Cancel"))
        self.passTextEdit.setHtml(_translate("Dialog", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:18px; font-weight:600; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18px; font-weight:400;\">Password </span><span style=\" font-size:18px; font-weight:400; color:#f14d46;\">*</span></p></body></html>"))
