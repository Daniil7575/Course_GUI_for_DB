from typing import get_origin
# import github_ui
import nanoid as nd
import login_dialog
import sys
import json
import psycopg2 as pg
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import (
    QMainWindow,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QDialog,
    QLineEdit,
    QDialogButtonBox,
    QFormLayout,
)

# DB_PARAMS_PATH = "db_connection.json"


class LoginDialog(QDialog, login_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.signButton.clicked.connect(self.getInputs)
        self.exitButton.clicked.connect(self.exit)
    
    def getInputs(self):
        self.accept()
        return (self.loginEdit.text(), self.passEdit.text())
    
    def exit(self):
        sys.exit(0)


class GithubApp(QMainWindow, github_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__paint_reps()  # без этого репы не красятся
        login = self.establish_db_connection()
        self.set_repositories()
        
        
    def __paint_reps(self):  # TODO: move this function to the end of setupUi()
        for rep in range(self.repositoryList.count()):
            self.repositoryList.item(rep).setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        self.setFixedSize(self.size())

    # def _dialog_decorator(dialog_object):
    #     def decorator(func):
    #         dialog = dialog_object()
    #         def wrapper(*args, **kwargs):
    #             ex_flag = False
    #             while not ex_flag:
    #                 ex_flag, ret_list = func(dialog, ex_flag, *args, **kwargs)
    #             return list(ret_list)
    #         return wrapper
    #     return decorator

    # @_dialog_decorator(dialog_object=LoginDialog)
    def establish_db_connection(self):
        dialog = LoginDialog()

        while True:
            dialog.exec()
            login_data = dialog.getInputs()
            try:
                self.conn = pg.connect(host="localhost",
                                    database="CourseDB",
                                    user=login_data[0],
                                    password=login_data[1])
            except:
                # TODO: customize error window
                QMessageBox.critical(  
                        None,
                        "LOGIN ERROR",
                        "Login or password is incorrect! Try again")
            finally:
                if hasattr(self, "conn"):
                    break
        
        self.cur = self.conn.cursor()
        return login_data[0]

        # l = LoginDialog()
        # l.exec()
        # print(l.getInputs())
        # conn = pg.connect(
        #     host="localhost",
        #     database="MyCompany2",
        #     user="247468",
        #     password="regjiekjgek")

    def set_repositories(self):
        self.cur.execute("select name FROM repository")
        for eli in self.cur.fetchall():
            for inner_el in eli:
                item = QtWidgets.QListWidgetItem()
                item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
                font = QtGui.QFont()
                font.setFamily("Arial")
                font.setPointSize(14)
                font.setBold(True)
                font.setWeight(75)
                item.setFont(font)
                item.setText(inner_el)
                self.repositoryList.addItem(item)
        self.__paint_reps()

# git = QtWidgets.QApplication(sys.argv)
# window = GithubApp()

# window.show()
# git.exec()
# print(f"{nd.generate(alphabet='abcdef1234567890', size=8)}-{nd.generate(alphabet='abcdef1234567890', size=4)}")

# a = [1, 2, 3, 4]
# # a.insert(len(a), 5)
# print(type(None))



print(1024 % (25))