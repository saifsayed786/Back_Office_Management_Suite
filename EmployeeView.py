# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'EmployeeLoginView.ui'
#
# Created by: PyQt5 UI code generator 5.15.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialog
import datetime

import db2
from EmployeePayroll import E_Payroll


class Ui_other_login(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Employee Screen")
        Dialog.resize(420, 470)
        # MainWindow.setObjectName("MainWindow")
        # MainWindow.resize(370, 408)
        # self.centralwidget = QtWidgets.QWidget(MainWindow)
        # self.centralwidget.setObjectName("centralwidget")
        self.clockin_button = QtWidgets.QPushButton(Dialog)
        self.clockin_button.setGeometry(QtCore.QRect(110, 100, 121, 71))
        self.clockin_button.setObjectName("clockin_button")
        self.schedule_button = QtWidgets.QPushButton(Dialog)
        self.schedule_button.setGeometry(QtCore.QRect(110, 180, 121, 71))
        self.schedule_button.setObjectName("schedule_button")
        self.schedule_button.clicked.connect(self.schedulemsg)
        self.displayName = QtWidgets.QLabel(Dialog)
        self.displayName.setGeometry(QtCore.QRect(10, 30, 131, 16))
        self.displayName.setObjectName("displayName")
        self.current_time = QtWidgets.QLabel(Dialog)
        self.current_time.setGeometry(QtCore.QRect(270, 10, 71, 23))
        self.current_time.setObjectName("current_time")
        self.clockin_button.clicked.connect(self.clockinout)
        self.clockout_button = QtWidgets.QPushButton(Dialog)
        self.clockout_button.setGeometry(QtCore.QRect(110, 340, 121, 71))
        self.clockout_button.setObjectName("clockin_button")
        self.clockout_button.clicked.connect(self.ClockOut)
        self.payroll_button = QtWidgets.QPushButton(Dialog)
        self.payroll_button.setGeometry(QtCore.QRect(110, 260, 121, 71))
        self.payroll_button.setObjectName("payroll_button")
        cur = db2.conn.cursor()
        sql = ("SELECT schedulestartdate,scheduleenddate from schedule where employeeid = ?")
        data = db2.emp_list[0]
        cur.execute(sql,[data])
        res = cur.fetchall()
        if len(res) !=0:
            self.payroll_button.clicked.connect(self.openpayroll)
        
        # MainWindow.setCentralWidget(Dialog)
        # self.statusbar = QtWidgets.QStatusBar(MainWindow)
        # self.statusbar.setObjectName("statusbar")
        # MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)


    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Employee Screen"))
        self.clockin_button.setText(_translate("Dialog", "Clock In"))
        self.clockout_button.setText(_translate("Dialog", "Clock Out"))
        self.schedule_button.setText(_translate("Dialog", "Schedules"))
        self.payroll_button.setText(_translate("Dialog", "Payroll"))
        self.current_time.setText(datetime.datetime.now().strftime("%H:%M:%S"))
        
        cur = db2.conn.cursor()
        sql = ("SELECT firstname from employees where employeeid = ?")
        data = db2.emp_list[0]
        cur.execute(sql,[data])
        res = cur.fetchall()
        for i in res:
            self.displayName.setText(_translate("Dialog", "Hello"+" "+i[0]))
    
    def clockinout(self):
        time1 = datetime.datetime.now()
        db2.time1_list.append(time1)
        # print(db2.time1_list)
        
    def ClockOut(self):
        time2 = datetime.datetime.now()+datetime.timedelta(hours=9)
        db2.time2_list.append(time2)
        # print(db2.time2_list)
    
    def openpayroll(self):        
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = E_Payroll()
        self.ui.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def schedulemsg(self):  
        cur = db2.conn.cursor()
        sql = ("SELECT schedulestartdate,scheduleenddate,employeeId from schedule where employeeid = ?")
        data = db2.emp_list[0]
        cur.execute(sql,[data])
        res = cur.fetchone()
        if len(res) !=0:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("Your Todays Schedule is from"+" "+res[0]+" "+"to"+" "+res[1])
            msg.exec_()
            diff = db2.time2_list[0]-db2.time1_list[0]
            days, seconds = diff.days, diff.seconds
            hours = days * 24 + seconds // 3600
            rate = ("SELECT currentrate from employees where employeeid =?")
            cur.execute(rate,[res[2]])
            output = cur.fetchone()
            netpay = hours*output[0]
            insert_sql = ("INSERT INTO payroll (employeeid,netpay) values (?,?)")
            data = ([res[2],netpay])
            cur.execute(insert_sql,data)
            db2.conn.commit()    
        else:
            msg = QtWidgets.QMessageBox()
            msg.setWindowTitle("Info")
            msg.setText("You Have No Schedule Today")
            msg.exec_()
            
        
if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_other_login()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())
