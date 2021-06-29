# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from Employees import Ui_EmployeeWidget
from InventoryMenu import Ui_InventoryMenu
from schedule import Ui_ScheduleWidget
from payroll import Ui_Payroll

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(474, 648)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.employee_button = QtWidgets.QPushButton(self.centralwidget)
        self.employee_button.setGeometry(QtCore.QRect(170, 70, 113, 61))
        self.employee_button.setObjectName("employee_button")
        self.inventory_button = QtWidgets.QPushButton(self.centralwidget)
        self.inventory_button.setGeometry(QtCore.QRect(170, 150, 113, 61))
        self.inventory_button.setObjectName("inventory_button")
        self.payroll_button = QtWidgets.QPushButton(self.centralwidget)
        self.payroll_button.setGeometry(QtCore.QRect(170, 230, 113, 61))
        self.payroll_button.setObjectName("payroll_button")
        self.payroll_button.clicked.connect(self.openpayroll)
        self.schedules_button = QtWidgets.QPushButton(self.centralwidget)
        self.schedules_button.setGeometry(QtCore.QRect(170, 310, 113, 61))
        self.schedules_button.setObjectName("schedules_button")
        self.config_button = QtWidgets.QPushButton(self.centralwidget)
        self.config_button.setGeometry(QtCore.QRect(170, 390, 113, 61))
        self.config_button.setObjectName("config_button")
        self.report_button = QtWidgets.QPushButton(self.centralwidget)
        self.report_button.setGeometry(QtCore.QRect(170, 470, 113, 61))
        self.report_button.setObjectName("report_button")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.employee_button.clicked.connect(lambda:self.openemployee())

        self.inventory_button.clicked.connect(lambda: self.openinventory())
        
        self.schedules_button.clicked.connect(lambda:self.openschedule())


    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.employee_button.setText(_translate("MainWindow", "Employees"))
        self.inventory_button.setText(_translate("MainWindow", "Inventory"))
        self.payroll_button.setText(_translate("MainWindow", "Payroll"))
        self.schedules_button.setText(_translate("MainWindow", "Schedules"))
        self.config_button.setText(_translate("MainWindow", "Configuration"))
        self.report_button.setText(_translate("MainWindow", "Reports"))

    def openemployee(self):
        self.window=QtWidgets.QStackedWidget()
        self.ui=Ui_EmployeeWidget()
        self.ui.setupUi(self.window)
        self.window.show()

    def openinventory(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_InventoryMenu()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openschedule(self):
        self.window=QtWidgets.QDialog()
        self.ui=Ui_ScheduleWidget()
        self.ui.setupUi(self.window)
        self.window.show()
        
    def openpayroll(self):
        self.MainWindow = QtWidgets.QDialog()
        self.ui = Ui_Payroll()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())