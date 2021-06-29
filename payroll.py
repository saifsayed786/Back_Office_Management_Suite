# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'editEmployee.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

import sys
from PyQt5.QtSql import QSqlDatabase, QSqlQuery, QSqlTableModel
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QTableView,QVBoxLayout,QPushButton,QHBoxLayout,QApplication,QWidget


class Ui_Payroll(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(705, 572)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableView(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 671, 491))
        self.tableView.setObjectName("tableView")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("ems.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.initializedModel()
        
        self.tableView.setModel(self.model)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
    def initializedModel(self):
        self.model.setTable("payroll")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()

    def closeEvent(self, event):
        self.db.close()


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_Payroll()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())