from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtGui import QTextCursor
import MySQLdb as mdb
from PyQt5.QtWidgets import QLineEdit, QApplication, QMainWindow, QPushButton, QWidget
import sys

#這個code裡面有很多不同的class,每個class都是用來創建不同功能的介面
#每個class裡面有三個主要的function ---- __init__,LoadData,retranslateUi
#__init__和retranslateUi主要是做介面布置和event觸發
#LoadData是用來與資料庫做連結

#創建having的介面
class having_page(QWidget):
    def __init__(self, parent=None):
        super(having_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 351))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 100, 381, 41))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(280, 60, 381, 41))
        self.widget_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_5.setObjectName("widget_5")
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_8.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 100, 231, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_10.setGeometry(QtCore.QRect(30, 180, 231, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(280, 180, 381, 41))
        self.widget_8.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_8.setObjectName("widget_8")
        self.comboBox_10 = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_10.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 220, 231, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 260, 231, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 220, 381, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 310, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_12.setGeometry(QtCore.QRect(30, 140, 231, 41))
        self.textBrowser_12.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.widget_10 = QtWidgets.QWidget(self.widget)
        self.widget_10.setGeometry(QtCore.QRect(280, 140, 381, 41))
        self.widget_10.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_10.setObjectName("widget_10")
        self.comboBox_12 = QtWidgets.QComboBox(self.widget_10)
        self.comboBox_12.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_12.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_12.setObjectName("comboBox_12")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.comboBox_12.addItem("")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 260, 381, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 370, 691, 181))
        self.textBrowser_3.setStyleSheet("background-color: rgb(60, 78, 143);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 380, 671, 161))
        self.textBrowser_4.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
    def LoadData(self):
        self.textBrowser_4.clear()
        if self.lineEdit.text()==1:
            text="SELECT "+self.comboBox_8.currentText()+","+self.comboBox_3.currentText()+"("+self.comboBox_12.currentText()+")"+" FROM "+self.comboBox_10.currentText()+" GROUP BY "+self.comboBox_8.currentText()+" HAVING "+self.comboBox_8.currentText()+"="+self.lineEdit_2.text()
        else:
            text="SELECT "+self.comboBox_8.currentText()+","+self.comboBox_3.currentText()+"("+self.comboBox_12.currentText()+")"+" FROM "+self.comboBox_10.currentText()+" GROUP BY "+self.comboBox_8.currentText()+" HAVING "+self.comboBox_3.currentText()+"("+self.comboBox_12.currentText()+")"+"="+self.lineEdit_2.text()
        self.textBrowser_4.clear()
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        for i in range(cur.rowcount):
            result=cur.fetchall()
            for row in result:
                self.cursor=QTextCursor(self.textBrowser_4.document())
                self.cursor.insertText(str(row)+'\n')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "SUM"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "AVG"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "MAX"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "MIN"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "COUNT"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_8.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_8.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_8.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_8.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_8.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_8.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_8.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_8.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_8.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_8.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">TYPE</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">HAVING(1/2)</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">查詢關鍵字</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_12.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_12.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_12.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_12.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_12.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_12.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_12.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_12.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_12.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_12.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_12.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_12.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_12.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_12.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_12.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_12.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_12.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_12.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_12.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_12.setItemText(19, _translate("MainWindow", "*"))
        
        
#創建exist的介面
class exist_page(QWidget):
    def __init__(self, parent=None):
        super(exist_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 391))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 100, 381, 41))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 100, 231, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(280, 60, 381, 41))
        self.widget_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_5.setObjectName("widget_5")
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_8.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 180, 231, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(280, 180, 381, 41))
        self.widget_7.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_7.setObjectName("widget_7")
        self.comboBox_9 = QtWidgets.QComboBox(self.widget_7)
        self.comboBox_9.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_10.setGeometry(QtCore.QRect(30, 220, 231, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(280, 220, 381, 41))
        self.widget_8.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_8.setObjectName("widget_8")
        self.comboBox_10 = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_10.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_11.setGeometry(QtCore.QRect(30, 140, 231, 41))
        self.textBrowser_11.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(280, 140, 381, 41))
        self.widget_9.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_9.setObjectName("widget_9")
        self.comboBox_11 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox_11.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 260, 231, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(280, 260, 381, 41))
        self.widget_6.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_6.setObjectName("widget_6")
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 300, 231, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 300, 381, 41))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 350, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 410, 691, 141))
        self.textBrowser_3.setStyleSheet("background-color: rgb(60, 78, 143);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 420, 671, 121))
        self.textBrowser_4.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)

    def LoadData(self):
        self.textBrowser_4.clear()
        text="SELECT "+self.comboBox_8.currentText()+" FROM "+self.comboBox_3.currentText()+" WHERE "+self.comboBox_11.currentText()+" (SELECT "+self.comboBox_9.currentText()+" FROM "+self.comboBox_10.currentText()+" WHERE "+self.comboBox_6.currentText()+"="+self.lineEdit.text()+")"
        self.textBrowser_4.clear()
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        for i in range(cur.rowcount):
            result=cur.fetchall()
            for row in result:
                self.cursor=QTextCursor(self.textBrowser_4.document())
                self.cursor.insertText(str(row)+'\n')    
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_8.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_8.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_8.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_8.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_8.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_8.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_8.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_8.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_8.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_8.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_9.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_9.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_9.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_9.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_9.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_9.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_9.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">TYPE</span></p></body></html>"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "EXISTS"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "NOT EXISTS"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_6.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_6.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_6.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_6.setItemText(18, _translate("MainWindow", "plan_department"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">查詢關鍵字</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))

#創建in的介面
class in_page(QWidget):
    def __init__(self, parent=None):
        super(in_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 371))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 100, 381, 41))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 140, 231, 41))
        self.textBrowser_5.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 320, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 100, 231, 41))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(280, 140, 381, 41))
        self.widget_4.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_4.setObjectName("widget_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 60, 231, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(280, 60, 381, 41))
        self.widget_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_5.setObjectName("widget_5")
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_8.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 220, 231, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.widget_7 = QtWidgets.QWidget(self.widget)
        self.widget_7.setGeometry(QtCore.QRect(280, 220, 381, 41))
        self.widget_7.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_7.setObjectName("widget_7")
        self.comboBox_9 = QtWidgets.QComboBox(self.widget_7)
        self.comboBox_9.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_9.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_9.setObjectName("comboBox_9")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.comboBox_9.addItem("")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_10.setGeometry(QtCore.QRect(30, 260, 231, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(280, 260, 381, 41))
        self.widget_8.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_8.setObjectName("widget_8")
        self.comboBox_10 = QtWidgets.QComboBox(self.widget_8)
        self.comboBox_10.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_10.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_10.setObjectName("comboBox_10")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.comboBox_10.addItem("")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_11.setGeometry(QtCore.QRect(30, 180, 231, 41))
        self.textBrowser_11.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.widget_9 = QtWidgets.QWidget(self.widget)
        self.widget_9.setGeometry(QtCore.QRect(280, 180, 381, 41))
        self.widget_9.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_9.setObjectName("widget_9")
        self.comboBox_11 = QtWidgets.QComboBox(self.widget_9)
        self.comboBox_11.setGeometry(QtCore.QRect(20, 10, 331, 21))
        self.comboBox_11.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_11.setObjectName("comboBox_11")
        self.comboBox_11.addItem("")
        self.comboBox_11.addItem("")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 390, 691, 161))
        self.textBrowser_3.setStyleSheet("background-color: rgb(60, 78, 143);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 400, 671, 141))
        self.textBrowser_4.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
    def LoadData(self):
        self.textBrowser_4.clear()
        text="SELECT "+self.comboBox_8.currentText()+" FROM "+self.comboBox_3.currentText()+" WHERE "+self.comboBox_5.currentText()+" "+self.comboBox_11.currentText()+" (SELECT "+self.comboBox_9.currentText()+" FROM "+self.comboBox_10.currentText()+")"
        self.textBrowser_4.clear()
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        for i in range(cur.rowcount):
            result=cur.fetchall()
            for row in result:
                self.cursor=QTextCursor(self.textBrowser_4.document())
                self.cursor.insertText(str(row)+'\n')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "plan_department"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_8.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_8.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_8.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_8.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_8.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_8.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_8.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_8.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_8.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_8.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_9.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_9.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_9.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_9.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_9.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_9.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_9.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_9.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_9.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_9.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_9.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_9.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_9.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_9.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_9.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_9.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_9.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_9.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_9.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_9.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_10.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_10.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_10.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_10.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_10.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; font-weight:600;\">TYPE</span></p></body></html>"))
        self.comboBox_11.setItemText(0, _translate("MainWindow", "IN"))
        self.comboBox_11.setItemText(1, _translate("MainWindow", "NOT IN"))

#創建delete的介面
class delete_page(QWidget):
    def __init__(self, parent=None):
        super(delete_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 521))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 60, 381, 51))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 110, 231, 51))
        self.textBrowser_5.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 170, 381, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 170, 231, 51))
        self.textBrowser_6.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 230, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 60, 231, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(280, 110, 381, 51))
        self.widget_4.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_4.setObjectName("widget_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
    def LoadData(self):
        text="DELETE FROM "+self.comboBox_3.currentText()+" WHERE "+self.comboBox_5.currentText()+"="+"\""+self.lineEdit_2.text()+"\""
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        conn.commit()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢關鍵字</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "plan_department"))
        
        
#創建update的介面
class update_page(QWidget):
    def __init__(self, parent=None):
        super(update_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 511))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 60, 381, 51))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 110, 231, 51))
        self.textBrowser_5.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 160, 381, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 420, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 60, 231, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(280, 110, 381, 51))
        self.widget_4.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_4.setObjectName("widget_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 160, 231, 51))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 210, 231, 51))
        self.textBrowser_8.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 260, 231, 51))
        self.textBrowser_9.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 260, 381, 51))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(280, 210, 381, 51))
        self.widget_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_5.setObjectName("widget_5")
        self.comboBox_6 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_6.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_6.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_6.setObjectName("comboBox_6")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.comboBox_6.addItem("")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
    def LoadData(self):
        text="UPDATE "+self.comboBox_3.currentText()+" SET "+self.comboBox_5.currentText()+"="+"\""+self.lineEdit_2.text()+"\""+" WHERE "+self.comboBox_6.currentText()+"="+"\""+self.lineEdit_3.text()+"\""
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        conn.commit()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">SET</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "plan_department"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">SET</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.comboBox_6.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_6.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_6.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_6.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_6.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_6.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_6.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_6.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_6.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_6.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_6.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_6.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_6.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_6.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_6.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_6.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_6.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_6.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_6.setItemText(18, _translate("MainWindow", "plan_department"))
        
        
#創建insert的介面
class insert_page(QWidget):
    def __init__(self, parent=None):
        super(insert_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 521))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 60, 381, 51))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.information=["employee_id","employee_name","salary","employee_gender","for_department_id","own_department_id","dorm_area","plan_id","kid_id"]
        self.comboBox_3.currentIndexChanged.connect(self.info)
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 110, 231, 41))
        self.textBrowser_5.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 150, 381, 41))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 150, 231, 41))
        self.textBrowser_6.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 480, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 60, 231, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 18pt \"標楷體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 190, 231, 41))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 230, 231, 41))
        self.textBrowser_8.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.textBrowser_9 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_9.setGeometry(QtCore.QRect(30, 270, 231, 41))
        self.textBrowser_9.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_9.setObjectName("textBrowser_9")
        self.textBrowser_10 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_10.setGeometry(QtCore.QRect(30, 310, 231, 41))
        self.textBrowser_10.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_10.setObjectName("textBrowser_10")
        self.textBrowser_11 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_11.setGeometry(QtCore.QRect(30, 350, 231, 41))
        self.textBrowser_11.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_11.setObjectName("textBrowser_11")
        self.textBrowser_12 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_12.setGeometry(QtCore.QRect(30, 390, 231, 41))
        self.textBrowser_12.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_12.setObjectName("textBrowser_12")
        self.textBrowser_13 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_13.setGeometry(QtCore.QRect(30, 430, 231, 41))
        self.textBrowser_13.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_13.setObjectName("textBrowser_13")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_3.setGeometry(QtCore.QRect(280, 190, 381, 41))
        self.lineEdit_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_4.setGeometry(QtCore.QRect(280, 230, 381, 41))
        self.lineEdit_4.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_5.setGeometry(QtCore.QRect(280, 270, 381, 41))
        self.lineEdit_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_6.setGeometry(QtCore.QRect(280, 110, 381, 41))
        self.lineEdit_6.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_7.setGeometry(QtCore.QRect(280, 310, 381, 41))
        self.lineEdit_7.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_8 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_8.setGeometry(QtCore.QRect(280, 390, 381, 41))
        self.lineEdit_8.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.lineEdit_9 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_9.setGeometry(QtCore.QRect(280, 430, 381, 41))
        self.lineEdit_9.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_9.setObjectName("lineEdit_9")
        self.lineEdit_10 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_10.setGeometry(QtCore.QRect(280, 350, 381, 41))
        self.lineEdit_10.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_10.setObjectName("lineEdit_10")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
        
    def LoadData(self):
        if self.comboBox_3.currentIndex()==0:
            text="INSERT INTO "+self.comboBox_3.currentText()+" ("+self.information[0]+","+self.information[1]+","+self.information[2]+","+self.information[3]+","+self.information[4]+","+self.information[5]+","+self.information[6]+","+self.information[7]+","+self.information[8]+")"+" VALUES "+"("+"\""+self.lineEdit_6.text()+"\""+","+"\""+self.lineEdit_2.text()+"\""+","+"\""+self.lineEdit_3.text()+"\""+","+"\""+self.lineEdit_4.text()+"\""+","+"\""+self.lineEdit_5.text()+"\""+","+"\""+self.lineEdit_7.text()+"\""+","+"\""+self.lineEdit_10.text()+"\""+","+"\""+self.lineEdit_8.text()+"\""+","+"\""+self.lineEdit_9.text()+"\""+");"
        elif self.comboBox_3.currentIndex()==4:
            text="INSERT INTO "+self.comboBox_3.currentText()+" ("+self.information[0]+","+self.information[1]+","+self.information[2]+")"+" VALUES "+"("+"\""+self.lineEdit_6.text()+"\""+","+"\""+self.lineEdit_2.text()+"\""+","+"\""+self.lineEdit_3.text()+"\""+","+"\""+self.lineEdit_4.text()+"\""+");"
        else:
            text="INSERT INTO "+self.comboBox_3.currentText()+" ("+self.information[0]+","+self.information[1]+","+self.information[2]+")"+" VALUES "+"("+"\""+self.lineEdit_6.text()+"\""+","+"\""+self.lineEdit_2.text()+"\""+","+"\""+self.lineEdit_3.text()+"\""+");"
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        conn.commit()
    
    def info(self):
        _translate = QtCore.QCoreApplication.translate
        if self.comboBox_3.currentIndex()==0:
            self.information=["employee_id","employee_name","salary","employee_gender","for_department_id","own_department_id","dorm_area","plan_id","kid_id"]
        elif self.comboBox_3.currentIndex()==1:
            self.information=["department_id","department_name","department_num_of_employee","no","no","no","no","no","no"]
        elif self.comboBox_3.currentIndex()==2:
            self.information=["dorm_area","dorm_gender","maxnum","no","no","no","no","no","no"]
        elif self.comboBox_3.currentIndex()==3:
            self.information=["kid_id","age","kid_name","no","no","no","no","no","no"]
        elif self.comboBox_3.currentIndex()==4:
            self.information=["plan_id","plan_name","plan_num_of_employee","plan_department","no","no","no","no","no"]
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[0]+"</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[1]+"</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[2]+"</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[3]+"</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[4]+"</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[5]+"</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[6]+"</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[7]+"</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[8]+"</span></p></body></html>"))
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[0]+"</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[1]+"</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "INSERT"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'微軟正黑體\'; font-weight:600;\">類別</span></p></body></html>"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[2]+"</span></p></body></html>"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[3]+"</span></p></body></html>"))
        self.textBrowser_9.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[4]+"</span></p></body></html>"))
        self.textBrowser_10.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[5]+"</span></p></body></html>"))
        self.textBrowser_11.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[6]+"</span></p></body></html>"))
        self.textBrowser_12.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[7]+"</span></p></body></html>"))
        self.textBrowser_13.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:10pt; font-weight:600;\">"+self.information[8]+"</span></p></body></html>"))
        
#創建select的介面
class select_page(QWidget):
    def __init__(self, parent=None):
        super(select_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 371))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.widget_3 = QtWidgets.QWidget(self.widget)
        self.widget_3.setGeometry(QtCore.QRect(280, 160, 381, 51))
        self.widget_3.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_3.setObjectName("widget_3")
        self.comboBox_3 = QtWidgets.QComboBox(self.widget_3)
        self.comboBox_3.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_3.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 210, 231, 51))
        self.textBrowser_5.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget)
        self.lineEdit_2.setGeometry(QtCore.QRect(280, 270, 381, 51))
        self.lineEdit_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.textBrowser_6 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_6.setGeometry(QtCore.QRect(30, 270, 231, 51))
        self.textBrowser_6.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_6.setObjectName("textBrowser_6")
        self.pushButton = QtWidgets.QPushButton(self.widget)
        self.pushButton.setGeometry(QtCore.QRect(30, 330, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_2.setGeometry(QtCore.QRect(30, 160, 231, 51))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget_4 = QtWidgets.QWidget(self.widget)
        self.widget_4.setGeometry(QtCore.QRect(280, 210, 381, 51))
        self.widget_4.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_4.setObjectName("widget_4")
        self.comboBox_5 = QtWidgets.QComboBox(self.widget_4)
        self.comboBox_5.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_5.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_5.setObjectName("comboBox_5")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.comboBox_5.addItem("")
        self.textBrowser_7 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_7.setGeometry(QtCore.QRect(30, 110, 231, 51))
        self.textBrowser_7.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_7.setObjectName("textBrowser_7")
        self.widget_5 = QtWidgets.QWidget(self.widget)
        self.widget_5.setGeometry(QtCore.QRect(280, 110, 381, 51))
        self.widget_5.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_5.setObjectName("widget_5")
        self.comboBox_8 = QtWidgets.QComboBox(self.widget_5)
        self.comboBox_8.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_8.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.textBrowser_8 = QtWidgets.QTextBrowser(self.widget)
        self.textBrowser_8.setGeometry(QtCore.QRect(30, 60, 231, 51))
        self.textBrowser_8.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_8.setObjectName("textBrowser_8")
        self.widget_6 = QtWidgets.QWidget(self.widget)
        self.widget_6.setGeometry(QtCore.QRect(280, 60, 381, 51))
        self.widget_6.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_6.setObjectName("widget_6")
        self.comboBox_4 = QtWidgets.QComboBox(self.widget_6)
        self.comboBox_4.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox_4.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 390, 691, 161))
        self.textBrowser_3.setStyleSheet("background-color: rgb(60, 78, 143);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 400, 671, 141))
        self.textBrowser_4.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)

        self.retranslateUi(parent)
        
    def LoadData(self):
        if self.comboBox_4.currentText()=="no":
            text="SELECT "+self.comboBox_8.currentText()+" FROM "+self.comboBox_3.currentText()+" WHERE "+self.comboBox_5.currentText()+"="+"\""+self.lineEdit_2.text()+"\""
        else:
            text="SELECT "+self.comboBox_4.currentText()+"("+self.comboBox_8.currentText()+")"+" FROM "+self.comboBox_3.currentText()+" WHERE "+self.comboBox_5.currentText()+"="+"\""+self.lineEdit_2.text()+"\""
        self.textBrowser_4.clear()
        conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
        cur=conn.cursor()
        cur.execute(text)
        for i in range(cur.rowcount):
            result=cur.fetchall()
            for row in result:
                self.cursor=QTextCursor(self.textBrowser_4.document())
                self.cursor.insertText(str(row)+'\n')
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("MainWindow", "employee"))
        self.comboBox_3.setItemText(1, _translate("MainWindow", "department"))
        self.comboBox_3.setItemText(2, _translate("MainWindow", "dorm"))
        self.comboBox_3.setItemText(3, _translate("MainWindow", "kid"))
        self.comboBox_3.setItemText(4, _translate("MainWindow", "plan"))
        self.textBrowser_5.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">WHERE</span></p></body></html>"))
        self.textBrowser_6.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢關鍵字</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">FROM</span></p></body></html>"))
        self.comboBox_5.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_5.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_5.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_5.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_5.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_5.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_5.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_5.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_5.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_5.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_5.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_5.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_5.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_5.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_5.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_5.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_5.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_5.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_5.setItemText(18, _translate("MainWindow", "plan_department"))
        self.textBrowser_7.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">SELECT</span></p></body></html>"))
        self.comboBox_8.setItemText(0, _translate("MainWindow", "employee_id"))
        self.comboBox_8.setItemText(1, _translate("MainWindow", "employee_name"))
        self.comboBox_8.setItemText(2, _translate("MainWindow", "salary"))
        self.comboBox_8.setItemText(3, _translate("MainWindow", "employee_gender"))
        self.comboBox_8.setItemText(4, _translate("MainWindow", "for_department_id"))
        self.comboBox_8.setItemText(5, _translate("MainWindow", "own_department_id"))
        self.comboBox_8.setItemText(6, _translate("MainWindow", "department_id"))
        self.comboBox_8.setItemText(7, _translate("MainWindow", "department_name"))
        self.comboBox_8.setItemText(8, _translate("MainWindow", "department_num_of_employee"))
        self.comboBox_8.setItemText(9, _translate("MainWindow", "maxnum"))
        self.comboBox_8.setItemText(10, _translate("MainWindow", "kid_id"))
        self.comboBox_8.setItemText(11, _translate("MainWindow", "plan_num_of_employee"))
        self.comboBox_8.setItemText(12, _translate("MainWindow", "kid_name"))
        self.comboBox_8.setItemText(13, _translate("MainWindow", "age"))
        self.comboBox_8.setItemText(14, _translate("MainWindow", "plan_id"))
        self.comboBox_8.setItemText(15, _translate("MainWindow", "plan_name"))
        self.comboBox_8.setItemText(16, _translate("MainWindow", "dorm_area"))
        self.comboBox_8.setItemText(17, _translate("MainWindow", "dorm_gender"))
        self.comboBox_8.setItemText(18, _translate("MainWindow", "plan_department"))
        self.comboBox_8.setItemText(19, _translate("MainWindow", "*"))
        self.textBrowser_8.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:18pt; font-weight:600;\">TYPE</span></p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("MainWindow", "no"))
        self.comboBox_4.setItemText(1, _translate("MainWindow", "COUNT"))
        self.comboBox_4.setItemText(2, _translate("MainWindow", "SUM"))
        self.comboBox_4.setItemText(3, _translate("MainWindow", "AVG"))
        self.comboBox_4.setItemText(4, _translate("MainWindow", "MAX"))
        self.comboBox_4.setItemText(5, _translate("MainWindow", "MIN"))

#創建mysql的介面       
class mysql_page(QWidget):
    def __init__(self, parent=None):
        super(mysql_page, self).__init__(parent)
        parent.resize(800, 600)
        parent.setStyleSheet("background-color: rgb(225, 244, 255);")
        self.centralwidget = QtWidgets.QWidget(parent)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(80, 230, 631, 31))
        self.pushButton.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.LoadData)
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(80, 80, 231, 141))
        self.textBrowser_2.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.widget_2 = QtWidgets.QWidget(self.centralwidget)
        self.widget_2.setGeometry(QtCore.QRect(330, 20, 381, 51))
        self.widget_2.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.widget_2.setObjectName("widget_2")
        self.comboBox = QtWidgets.QComboBox(self.widget_2)
        self.comboBox.setGeometry(QtCore.QRect(20, 10, 331, 31))
        self.comboBox.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(80, 20, 231, 51))
        self.textBrowser.setStyleSheet("background-color: rgb(169, 221, 255);\n"
"font: 9pt \"微軟正黑體\";")
        self.textBrowser.setObjectName("textBrowser")
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setGeometry(QtCore.QRect(50, 10, 691, 271))
        self.widget.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.widget.setObjectName("widget")
        self.lineEdit = QtWidgets.QLineEdit(self.widget)
        self.lineEdit.setGeometry(QtCore.QRect(280, 70, 381, 141))
        self.lineEdit.setStyleSheet("background-color: rgb(255, 254, 235);")
        self.lineEdit.setObjectName("lineEdit")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(50, 300, 691, 251))
        self.textBrowser_3.setStyleSheet("background-color: rgb(60, 78, 143);")
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(60, 310, 671, 231))
        self.textBrowser_4.setStyleSheet("background-color: rgb(214, 235, 241);")
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.widget.raise_()
        self.pushButton.raise_()
        self.textBrowser_2.raise_()
        self.widget_2.raise_()
        self.textBrowser.raise_()
        self.textBrowser_3.raise_()
        self.textBrowser_4.raise_()
        parent.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 25))
        self.menubar.setObjectName("menubar")
        parent.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(parent)
        self.statusbar.setObjectName("statusbar")
        parent.setStatusBar(self.statusbar)
        self.retranslateUi(parent)

    def LoadData(self):
        self.textBrowser_4.clear()
        temp=self.lineEdit.text()
        get=temp.split(" ")
        get=get[0]
        if get=="SELECT":
            conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
            cur=conn.cursor()
            cur.execute(self.lineEdit.text())
            for i in range(cur.rowcount):
                result=cur.fetchall()
                for row in result:
                    self.cursor=QTextCursor(self.textBrowser_4.document())
                    self.cursor.insertText(str(row)+'\n')
        else:
            conn=mdb.connect(host="127.0.0.1",user="root",passwd="a201020102010",db="dbms")
            cur=conn.cursor()
            cur.execute(self.lineEdit.text())
            conn.commit()
    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton.setText(_translate("MainWindow", "Search"))
        self.textBrowser_2.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:\'標楷體\'; font-size:18pt; font-weight:600;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢關鍵字</span></p></body></html>"))
        self.comboBox.setItemText(0, _translate("MainWindow", "MYSQL"))
        self.comboBox.setItemText(1, _translate("MainWindow", "SELECT"))
        self.comboBox.setItemText(2, _translate("MainWindow", "INSERT"))
        self.comboBox.setItemText(3, _translate("MainWindow", "UPDATE"))
        self.comboBox.setItemText(4, _translate("MainWindow", "DELETE"))
        self.comboBox.setItemText(5, _translate("MainWindow", "IN"))
        self.comboBox.setItemText(6, _translate("MainWindow", "EXIST"))
        self.comboBox.setItemText(7, _translate("MainWindow", "HAVING"))
        self.textBrowser.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'微軟正黑體\'; font-size:9pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:\'標楷體\'; font-size:18pt; font-weight:600;\">查詢工具</span></p></body></html>"))
        
#mainwindow,有各個介面的function
class MainWindow(QMainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setFixedSize(800, 600)
        self.get_mysql()
    def get_mysql(self):
        self.mysql = mysql_page(self)
        self.setWindowTitle("MYSQL")
        self.mysql.comboBox.setCurrentIndex(0)
        self.mysql.comboBox.currentIndexChanged.connect(lambda index=self.mysql.comboBox.currentIndex() : self.change(index))
        self.show()
    
    def get_select(self):
        self.select = select_page(self)
        self.setWindowTitle("SELECT")
        self.select.comboBox.setCurrentIndex(1)
        self.select.comboBox.currentIndexChanged.connect(lambda index=self.select.comboBox.currentIndex() : self.change(index))
        self.show()
        
    def get_insert(self):
        self.insert = insert_page(self)
        self.setWindowTitle("INSERT")
        self.insert.comboBox.setCurrentIndex(2)
        self.insert.comboBox.currentIndexChanged.connect(lambda index=self.insert.comboBox.currentIndex() : self.change(index))
        self.show()
    
    def get_update(self):
        self.update = update_page(self)
        self.setWindowTitle("UPDATE")
        self.update.comboBox.setCurrentIndex(3)
        self.update.comboBox.currentIndexChanged.connect(lambda index=self.update.comboBox.currentIndex() : self.change(index))
        self.show()
    
    def get_delete(self):
        self.delete = delete_page(self)
        self.setWindowTitle("DELETE")
        self.delete.comboBox.setCurrentIndex(4)
        self.delete.comboBox.currentIndexChanged.connect(lambda index=self.delete.comboBox.currentIndex() : self.change(index))
        self.show()
    
    def get_selectin(self):
        self.selectin = in_page(self)
        self.setWindowTitle("IN")
        self.selectin.comboBox.setCurrentIndex(5)
        self.selectin.comboBox.currentIndexChanged.connect(lambda index=self.selectin.comboBox.currentIndex() : self.change(index))
        self.show()
        
    def get_selectexist(self):
        self.selectexist = exist_page(self)
        self.setWindowTitle("EXIST")
        self.selectexist.comboBox.setCurrentIndex(6)
        self.selectexist.comboBox.currentIndexChanged.connect(lambda index=self.selectexist.comboBox.currentIndex() : self.change(index))
        self.show()
        
    def get_selecthaving(self):
        self.selecthaving = having_page(self)
        self.setWindowTitle("HAVING")
        self.selecthaving.comboBox.setCurrentIndex(7)
        self.selecthaving.comboBox.currentIndexChanged.connect(lambda index=self.selecthaving.comboBox.currentIndex() : self.change(index))
        self.show()
        
    #根據選取的功能,轉移到不同介面
    def change(self,index):
        if index==0:
            self.get_mysql()
        elif index==1:
            self.get_select()
        elif index==2:
            self.get_insert()
        elif index==3:
            self.get_update()
        elif index==4:
            self.get_delete()
        elif index==5:
            self.get_selectin()
        elif index==6:
            self.get_selectexist()
        elif index==7:
            self.get_selecthaving()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    sys.exit(app.exec_())