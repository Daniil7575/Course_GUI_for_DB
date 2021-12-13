import github_ui
import sys
from PyQt5 import QtGui, QtWidgets
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


class GithubApp(QMainWindow, github_ui.Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self._paint_reps()  # без этого репы не красятся
    
    def _paint_reps(self):
        for rep in range(self.repositoryList.count()):
            self.repositoryList.item(rep).setForeground(QtGui.QBrush(QtGui.QColor(255, 255, 255)))
            

git = QtWidgets.QApplication(sys.argv)
window = GithubApp()
window.show()
git.exec_()