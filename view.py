import github_ui8
import login_dialog
import user_creation_dialog
import create_rep_dialog
import create_branch_dialog
import user_info_dialog
import commit_dialog

from os import error
import sys
import json
import re

import psycopg2 as pg
import nanoid as nd

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
POSTGRES_LOGIN = "postgres"
POSTGRES_PASS = "246509"


def odin_protection(query: str):
        black_list = ("--", ";", "\\", "/", "||", "chr(")

        if any(el in query.replace("\\n", "").replace("\n", "") for el in black_list):
            return ""
        return query


def pars2(string):
    return [f"{hex(ord(el))}" for el in string]


def depars2(bytes):
    bytes = bytes + " "
    if bytes == " ":
        return

    res = ""
    buffer = ""
    for el in bytes:
        if el != " ":
            buffer += el
            continue

        res += chr(int(buffer, base=16))

        buffer = ""
    return res


class UserInfoDialog(QDialog, user_info_dialog.Ui_Dialog):
    def __init__(self, cur, login):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        # self.rejected.connect(self.exit)
        self.statsButton.clicked.connect(lambda: self.stats(cur, login))
        self.exitButton.clicked.connect(self.exit)
    
    def stats(self, cur, login):
        try:
            cur.execute(f"call developer_info('{login}')")
            QMessageBox.information(  
                        None,
                        "USER STATS INFO",
                        f"stats for user '{login}' have been successfully dumped on C:\\321.csv!")
        except:
            QMessageBox.critical(  
                        None,
                        "USER STATS ERROR",
                        f"dumping stats have failed!")
        # self.accept()
    
    def exit(self):
        self.reject()


class UserCreationDialog(QDialog, user_creation_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        # self.rejected.connect(self.exit)
        self.createUserButton.clicked.connect(self.getInputs)
        self.cancelButton.clicked.connect(self.exit)
    
    def getInputs(self):
        self.accept()
        return (self.newUserLogin.text(), self.newUserName.text(), self.newUserAbout.text(), self.newUserGeo.text(), self.newUserPass.text())
    
    def exit(self):
        self.is_cancel = True
        self.reject()


class LoginDialog(QDialog, login_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.regButton.clicked.connect(self.register)
        self.signButton.clicked.connect(self.getInputs)
        self.exitButton.clicked.connect(self.exit)

    def register(self):
        dialog = UserCreationDialog()

        while True:
            dialog.exec()
            user_data = dialog.getInputs()
            executed = False

            try:
                q_variables = [("'" + el + "'") if el != "" else 'null' for el in user_data]
                conn = pg.connect(host="localhost",
                                    database="CourseDB",
                                    user=POSTGRES_LOGIN,
                                    password=POSTGRES_PASS)
                # print(f"insert into developer values({', '.join(q_variables)})")
                conn.cursor().execute(odin_protection(f"insert into developer values({', '.join(q_variables)})"))
                conn.cursor().execute(odin_protection(f"create user {user_data[0]} with encrypted password '{user_data[-1]}' in group \"Developer\", \"pg_write_server_files\" "))
                executed = True
            except:
                if hasattr(dialog, "is_cancel") and dialog.is_cancel:
                    break
                # TODO: customize error window
                QMessageBox.critical(  
                        None,
                        "USER CREATION ERROR",
                        "Something wrong with new user data! Try again")
            finally:
                conn.commit()
                if executed:
                    # TODO: customize error window
                    QMessageBox.information(  
                        None,
                        "USER CREATION INFO",
                        f"user '{user_data[0]}' has been created!")
                    break
            
            del(conn)
    

    def getInputs(self):
        self.accept()
        return (self.loginEdit.text(), self.passEdit.text())
    
    def exit(self):
        sys.exit(0)


class CreateRepDialog(QDialog, create_rep_dialog.Ui_Dialog):
    def __init__(self, login):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.isdone = False
        self.is_cancel = False
        self.currentUser.setText(login)
        # self.rejected.connect(self.exit)

        self.createRepButton.clicked.connect(self.getIputs)
        self.cancelButton.clicked.connect(self.exit)
        # self.signButton.clicked.connect(self.getInputs)
        # self.exitButton.clicked.connect(self.exit)
    
    def getIputs(self):
        self.accept()
        return (self.newRepName.text(), self.langs.text(), self.description.text(), self.tags.text())
    
    def exit(self):
        self.is_cancel = True
        self.reject()


class CreateBranchDialog(QDialog, create_branch_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.isdone = False
        self.is_cancel = False

        self.createRepButton.clicked.connect(self.getIputs)
        self.cancelButton.clicked.connect(self.exit)

    def getIputs(self):
        self.accept()
        return (self.description.text())
    
    def exit(self):
        self.is_cancel = True
        self.reject()


class CommitDialog(QDialog, commit_dialog.Ui_Dialog):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setFixedSize(self.size())

        self.isdone = False
        self.is_cancel = False

        self.commitButton.clicked.connect(self.getInputs)
        self.cancelButton.clicked.connect(self.exit)

    def getInputs(self):
        self.accept()
        return (self.codeCheckBox.isChecked(), self.modelCheckBox.isChecked(), self.datasetCheckBox.isChecked(), self.summary.text(), self.description.text())
        
    def exit(self):
        self.is_cancel = True
        self.reject()
    

class GithubApp(QMainWindow, github_ui8.Ui_MainWindow):
    current_rep = None
    reps = {}
    TYPES = {
        "rep": "0000",
        "br": "bbbb",
        "c": "cccc"
        }

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
        
        self.login = self.establish_db_connection()
        self.showMaximized()
        
        self.set_repositories()
        self.menuprofile.aboutToShow.connect(self.show_profile)
        self.newRepButton.clicked.connect(self.create_rep)
        self.newBranchButton.clicked.connect(self.create_branch)
        self.commitButton.clicked.connect(self.commit)
        self.deleteRepButton.clicked.connect(self.delete_rep)
        # self.branchesComboBox.currentTextChanged.connect(self.change_commit_view)
    
    def gen_uuid(self, alp="abcdef1234567890", type='rep'):
        oct = nd.generate(alphabet=alp, size=8)

        quads = nd.generate(alphabet=alp, size=4) + \
                "-" + \
                nd.generate(alphabet=alp, size=4) + \
                "-" + \
                self.TYPES[type]
        
        twlv = nd.generate(alphabet=alp, size=12)

        return oct + "-" + quads + "-" + twlv

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
        try:
            self.repositoryList.currentItemChanged.disconnect(self.change_branch_view)
        except:
            ...
        self.reps = {}
        self.repositoryList.clear()

        self.cur.execute("select id, name FROM repository")
        for elem in self.cur.fetchall():
            self.reps[elem[0]] = elem[1]
        
        self.cur.execute("select usr_login, rep_id from usr_rep_connection where status = '0'")
        for elem in self.cur.fetchall():
            self.reps[elem[0] + "/" + self.reps[elem[1]]] = elem[1]

        # [print(name, id_) for name, id_ in self.reps.items()]
        self.reps = dict(list(self.reps.items())[len(self.reps) // 2:])

        self.repositoryList.currentItemChanged.connect(self.change_branch_view)
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
        self.current_rep = curr_obj if isinstance(curr_obj, str) else curr_obj.text()
        # print(self.reps[self.current_rep])
        
        # print(self.current_rep)
        # print(self.reps)
        # print(self.reps[self.current_rep])
        self.cur.execute(f"select id, name from branch where rep_id = '{self.reps[self.current_rep]}'")

        self.currentBranch.clear()
        self.currentBranch.font = 8
        self.currentBranch.insertPlainText(f"current rep uuid: {self.reps[self.current_rep]}")
        
        self.branchesComboBox.clear()
        self.branchesComboBox.currentTextChanged.connect(self.change_commit_view)

        for record in self.cur.fetchall():
            self.branches_name_id[record[1]] = record[0]
            # print(self.branches_name_id)
            self.branchesComboBox.addItem(record[1])
        
        # self.change_commit_view()

        # self.branchesComboBox.currentTextChanged.disconnect(self)
    
    def change_commit_view(self, curr_obj):
        try:
            self.commitsComboBox.currentTextChanged.disconnect(self.change_sum_desc_tmps)
        except:
            ...
        
        # try:
        #     self.commitsComboBox.currentTextChanged.disconnect(lambda: self.change_code_model_dataset(curr_obj))
        # except:
        #     ...
        self.current_branch = curr_obj
        self.commitsComboBox.clear()

        self.currentCommit.clear()
        self.currentCommit.insertPlainText(f"current branch uuid: {self.branches_name_id[self.current_branch]}")
        self.commitsComboBox.currentTextChanged.connect(self.change_sum_desc_tmps) 
    
        # self.commitsComboBox.currentTextChanged.connect(lambda: self.change_code_model_dataset(curr_obj)) 
        self.cur.execute(f"select branch_id, usr_login, uuid from commits where branch_id = '{self.branches_name_id[self.current_branch]}'")
        for record in self.cur.fetchall():
            self.commitsComboBox.addItem(record[2])
        
        self.change_code_model_dataset(self.current_branch)
    
    def change_sum_desc_tmps(self, curr_obj):
        self.current_code_model_dataset = ["", "", ""]
        self.current_commit = curr_obj

        #---------------------------------------------------------------------------code model dataset----------------------------------------------------------------------
        self.codeText.clear()
        self.cur.execute(f"select tmp_model from commits where uuid = '{curr_obj}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[0] = code
                    self.codeText.insertPlainText(code)

        self.modelText.clear()
        self.cur.execute(f"select tmp_code from commits where uuid = '{curr_obj}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[1] = code
                    self.modelText.insertPlainText(code)
        
        self.datasetText.clear()
        self.cur.execute(f"select tmp_dataset from commits where uuid = '{curr_obj}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[2] = code
                    self.datasetText.insertPlainText(code)

        #---------------------------------------------------------------------------summary description---------------------------------------------------------------------------------------
        # print(self.current_commit)
        self.cur.execute(f"select summary, description from commits where uuid = '{self.current_commit}'")
        for record in self.cur.fetchall():
            self.summary.setText(f"Summary: {record[0]}")
            self.description.setText(f"Description: {record[1]}")

    #TODO: Сделать выделение UUID последнего коммита
    def change_code_model_dataset(self, curr_obj):
        self.current_code_model_dataset = ["", "", ""]
        #TODO: сделать элегантнее
        self.codeText.clear()
        self.cur.execute(f"select model from rep_storage where id = '{self.branches_name_id[curr_obj]}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[0] = code
                    self.codeText.insertPlainText(code)

        self.modelText.clear()
        self.cur.execute(f"select code from rep_storage where id = '{self.branches_name_id[curr_obj]}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[1] = code
                    self.modelText.insertPlainText(code)
        
        self.datasetText.clear()
        self.cur.execute(f"select dataset from rep_storage where id = '{self.branches_name_id[curr_obj]}'")
        for record in self.cur.fetchall():
            if not record[0] == None:
                for key, code in dict(record[0]).items():
                    code = depars2(code)
                    self.current_code_model_dataset[2] = code
                    self.datasetText.insertPlainText(code)
        
        # self.lastCommitDate.clear()
        print(self.branches_name_id[curr_obj])
        self.cur.execute(f"select usr_login from commits where uuid = (select last_commit_uuid from rep_storage where id = '{self.branches_name_id[curr_obj]}')")
        self.lastCommitOwner.setText(f"there are no commits")
        a = self.cur.fetchall()
        for i in a:
            self.lastCommitOwner.setText(f"last commit by {i[0]}") 

    def create_rep(self):
        rep_dialog = CreateRepDialog(self.login)

        while True:
            rep_dialog.exec()
            error = False
            rep_dialog.isdone = False

            inputs = list(rep_dialog.getIputs())
            inputs.insert(0, self.gen_uuid())

            try:
                inputs[2] = "{" + ', '.join(re.findall(r'\w+', inputs[2])) + "}"
            except:
                ...
            
            try:
                inputs[4] = "{" + ', '.join(re.findall(r'\w+', inputs[4])) + "}"
            except:
                ...

            sql_data = [f"'{data}'" for data in inputs if inputs != "None"]
            
            conditions = ", ".join(sql_data)

            conditions = conditions.replace("''", "null").replace("'null'", "null").replace("'{}'", "null")

            try:
                if not rep_dialog.is_cancel:
                    self.cur.execute(f"insert into repository values({conditions})")
                    rep_dialog.isdone = True

            except:
                # TODO: customize error window
                error = True
                QMessageBox.critical(  
                        None,
                        "REPOSITORY CREATION ERROR",
                        "The entered data is incorrect! Try again")
                        
            finally:
                self.conn.commit()
                if (rep_dialog.isdone and not error) or rep_dialog.is_cancel:
                    break
            
        self.set_repositories()

    def show_profile(self):
        dialog = UserInfoDialog(self.cur, self.login)
        data = []
        self.cur.execute(odin_protection(f"select * from developer where login = '{self.login}'"))
        for el in self.cur.fetchall():
            for eli in el:
                data.append(eli)
        for record, el in zip(data, [dialog.nameTextEdit, dialog.loginTextEdit, dialog.descTextEdit, dialog.geoTextEdit]):
            el.setText(record) if record is not None else el.setText("N/A")
        
        dialog.exec()
        # dialog.nameTextEdit.setText(str(self.login))
        # dialog.

    def create_branch(self):
        branch_dialog = CreateBranchDialog()

        while True:
            branch_dialog.exec()
            err = False
            branch_dialog.isdone = False
            
            inputs = [self.gen_uuid(type="br"), self.reps[self.current_rep],branch_dialog.getIputs()]
            
            sql_query = ", ".join(["'" + elem + "'" if elem is not None else "null" for elem in inputs])
            try:
                if not branch_dialog.is_cancel:
                    self.cur.execute(odin_protection(f"insert into branch values({sql_query})"))
                    branch_dialog.isdone = True
            except(error):
                err = True
                print(error)
                QMessageBox.critical(  
                        None,
                        "BRANCH CREATION ERROR",
                        "The entered data is incorrect! Try again")
            finally:
                self.conn.commit()
                if (branch_dialog.isdone and not err) or branch_dialog.is_cancel:
                    break
        
        # self.set_repositories()
        self.change_branch_view(self.current_rep, None)

    def commit(self):
        commit_dialog = CommitDialog()
        c_m_ds = ["code", "model", "dataset"]

        while True:
            snippet = [self.modelText.toPlainText(), self.codeText.toPlainText(), self.datasetText.toPlainText()]
            commit_dialog.exec()
            commit_dialog.isdone = False
            err = False
            inputs = list(commit_dialog.getInputs())

            flags, inputs = inputs[:3], inputs[3:]
            [inputs.insert(elem[1], elem[0]) for elem in [(self.gen_uuid(type="c"), 0), (self.login, 0), (self.branches_name_id[self.current_branch], 0), ("NOW()", len(inputs) + 100)]]

            for indx in range(len(flags)):
                if flags[indx]:
                    snip = pars2(snippet[indx])
                    if self.current_code_model_dataset[indx] != snip:
                        inputs.insert(len(inputs) + indx + 1, '{"' + c_m_ds[indx] + '": "' + " ".join(snip) + '"}')
                        continue
                else:
                    inputs.insert(len(inputs) + indx + 1, None)    

            try:
                if not commit_dialog.is_cancel:
                    print("insert into commits values(" + odin_protection(", ".join([f"'{elem}'" if elem is not None else "null" for elem in inputs]).replace("'NOW()'", "NOW()")) + ")")
                    self.cur.execute("insert into commits values(" + odin_protection(", ".join([f"'{elem}'" if elem is not None else "null" for elem in inputs]).replace("'NOW()'", "NOW()")) + ")")
                    commit_dialog.isdone = True

            except(error):
                err = True
                print(error)
                QMessageBox.critical(  
                        None,
                        "COMMIT ERROR",
                        "The entered data is incorrect! Try again")
            finally:
                self.conn.commit()
                if (commit_dialog.isdone and not err) or commit_dialog.is_cancel:
                    break
        
        self.change_commit_view(self.current_branch)

    def delete_rep(self):
        try:
            self.cur.execute(f"delete from repository where id = '{self.reps[self.current_rep]}'")
        except:
             QMessageBox.critical(  
                        None,
                        "DELETE ERROR",
                        "Something goes wrong!")
        finally:
            self.conn.commit()
            self.set_repositories()

   


git = QtWidgets.QApplication(sys.argv)
window = GithubApp()

window.show()
git.exec_()