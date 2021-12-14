from typing import get_origin
import github_ui3
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


class GithubApp(QMainWindow, github_ui3.Ui_MainWindow):
    current_rep = None
    reps = {}

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

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.__paint_reps()  # без этого репы не красятся
        login = self.establish_db_connection()
        # self.showFullScreen()
        self.showMaximized()
        self.set_repositories()
        self.repositoryList.currentItemChanged.connect(self.change_branch_view)
        # self.branchesComboBox.currentTextChanged.connect(self.change_commit_view)
    
    def __paint_reps(self):  # TODO: move this function to the end of setupUi()
        for rep in range(self.repositoryList.count()):
            self.repositoryList.item(rep).setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
        self.setFixedSize(self.size())

    # @_dialog_decorator(dialog_object=LoginDialog)
    def establish_db_connection(self):
        dialog = LoginDialog()

        while True:
            dialog.exec()
            login_data = dialog.getInputs()
            login_data = ['bebroid', '123']
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
        self.cur.execute("select id, name FROM repository")
        for elem in self.cur.fetchall():
            self.reps[elem[0]] = elem[1]
        
        self.cur.execute("select usr_login, rep_id from usr_rep_connection where status = '0'")
        for elem in self.cur.fetchall():
            self.reps[elem[0] + "/" + self.reps[elem[1]]] = elem[1]

        # [print(name, id_) for name, id_ in self.reps.items()]
        self.reps =  dict(list(self.reps.items())[len(self.reps) // 2:])

        # print(self.reps)
        for rep, rep_name in self.reps.items():
            item = QtWidgets.QListWidgetItem()
            item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
            font = QtGui.QFont()
            font.setFamily("Arial")
            font.setPointSize(14)
            font.setBold(True)
            font.setWeight(75)
            item.setFont(font)
            item.setText(rep)
            self.repositoryList.addItem(item)

        # for eli in self.cur.fetchall():
        #     for inner_el in eli:
        #         item = QtWidgets.QListWidgetItem()
        #         item.setTextAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignVCenter)
        #         font = QtGui.QFont()
        #         font.setFamily("Arial")
        #         font.setPointSize(14)
        #         font.setBold(True)
        #         font.setWeight(75)
        #         item.setFont(font)
        #         item.setText(inner_el[1])
        #         self.repositoryList.addItem(item)
        #         self.reps[inner_el[0]] = inner_el[1]
        self.__paint_reps()

    def change_branch_view(self, curr_obj, prev_obj):
        try:
            self.branchesComboBox.currentTextChanged.disconnect(self.change_commit_view)
        except:
            ...
        self.branches_name_id = {}
        self.branchesComboBox.clear()
        self.current_rep = curr_obj.text()
        # print(self.current_rep)
        # print(self.reps)
        # print(self.reps[self.current_rep])
        self.cur.execute(f"select id, name from branch where rep_id = '{self.reps[self.current_rep]}'")
        for record in self.cur.fetchall():
            self.branches_name_id[record[1]] = record[0]
            print(self.branches_name_id)
            self.branchesComboBox.addItem(record[1])
        self.branchesComboBox.currentTextChanged.connect(self.change_commit_view)
             
    def change_commit_view(self, curr_obj):
        self.commitsComboBox.clear()
        self.current_branch = curr_obj
        # print(self.current_rep)
        # print(self.reps)
        # print(self.reps[self.current_rep])
        self.cur.execute(f"select branch_id, usr_login, uuid from commits where branch_id = '{self.branches_name_id[self.current_branch]}'")
        for record in self.cur.fetchall():
            self.commitsComboBox.addItem(record[2])

    # def set_branches(self):

git = QtWidgets.QApplication(sys.argv)
window = GithubApp()

window.show()
git.exec_()