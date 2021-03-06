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
from PyQt5.QtWidgets import QTableView,QVBoxLayout,QPushButton,QHBoxLayout,QApplication,QWidget,QMessageBox

import db2


class Ui_InventoryCreate(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(705, 572)
        self.tableView = QtWidgets.QTableView(Dialog)
        self.tableView.setGeometry(QtCore.QRect(20, 10, 671, 491))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(20, 510, 311, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(360, 510, 311, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        
        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)
        self.db = QSqlDatabase.addDatabase("QSQLITE")
        self.db.setDatabaseName("ems.db")
        self.db.open()
        self.model = QSqlTableModel()
        self.initializedModel()
        
        self.tableView.setModel(self.model)
        self.tableView.hideColumn(7)
        self.tableView.hideColumn(8)    
        self.tableView.hideColumn(10)
        self.tableView.hideColumn(9)
                    
        
        self.pushButton.clicked.connect(self.onAddRow)
        self.pushButton.clicked.connect(self.insdata)
        self.pushButton_2.clicked.connect(self.onDeleteRow)

        

    def initializedModel(self):
        self.model.setTable("inventory")
        self.model.setEditStrategy(QSqlTableModel.OnFieldChange)
        self.model.select()


    def onAddRow(self):
        self.model.insertRows(self.model.rowCount(), 1)  
        self.model.submit()
        

    def insdata(self):
        cur=db2.conn.cursor()
        sql2 = ("SELECT inventoryId,unitofmeasure FROM inventory")
        cur.execute(sql2)
        res = cur.fetchall()
        for i in res:     
            cur2 = db2.conn.cursor()
            sql = ("INSERT INTO inventoryConsume (inventoryid,unitofmeasure) values (?,?)" )
            cur2.execute(sql,(i))
            db2.conn.commit()       
        


    def onDeleteRow(self):
        self.model.removeRow(self.tableView.currentIndex().row())
        self.model.submit()
        self.model.select()
    
    def closeEvent(self, event):
        self.db.close()


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "Add Inventory"))
        self.pushButton_2.setText(_translate("Dialog", "Delete Inventory"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_InventoryCreate()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
