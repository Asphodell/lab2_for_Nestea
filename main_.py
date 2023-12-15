import sqlite3
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import os

import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter import ttk

import database_manager

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(806, 601)
        
        self.connection = None
        self.cursor = None
        
        self.name = "First"
        self.db = ""
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QtWidgets.QTableWidget(self.centralwidget)
        self.tableView.setGeometry(QtCore.QRect(10, 50, 781, 281))
        self.tableView.setObjectName("tableView")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 10, 81, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(10, 10, 81, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(690, 10, 91, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 460, 231, 83))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButton_3 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 0, 1, 1)
        self.pushButton_5 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_5.setObjectName("pushButton_5")
        self.gridLayout.addWidget(self.pushButton_5, 2, 0, 1, 1)
        self.pushButton_6 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_6.setObjectName("pushButton_6")
        self.gridLayout.addWidget(self.pushButton_6, 0, 1, 1, 1)
        self.pushButton_7 = QtWidgets.QPushButton(self.gridLayoutWidget)
        self.pushButton_7.setObjectName("pushButton_7")
        self.gridLayout.addWidget(self.pushButton_7, 2, 1, 1, 1)
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(670, 390, 121, 31))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(670, 430, 121, 31))
        self.pushButton_9.setObjectName("pushButton_9")
        self.verticalLayoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(40, 340, 191, 100))
        self.verticalLayoutWidget.setObjectName("verticalLayoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lineEdit = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout.addWidget(self.lineEdit)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.verticalLayout.addWidget(self.lineEdit_2)
        self.lineEdit_3 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout.addWidget(self.lineEdit_3)
        self.lineEdit_4 = QtWidgets.QLineEdit(self.verticalLayoutWidget)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout.addWidget(self.lineEdit_4)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 340, 16, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 370, 16, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(0, 390, 31, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(0, 420, 31, 16))
        self.label_4.setObjectName("label_4")
        self.pushButton_10 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_10.setGeometry(QtCore.QRect(720, 530, 75, 23))
        self.pushButton_10.setObjectName("pushButton_10")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 806, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        
        self.pushButton.clicked.connect(self.open_btn_command)
        self.pushButton_2.clicked.connect(self.create_btn_command)
        self.pushButton_4.clicked.connect(self.display_data)
        self.pushButton_3.clicked.connect(self.add)
        self.pushButton_5.clicked.connect(self.clear_fields)
        #self.pushButton_6.clicked.connect(self.edit_data)
        self.pushButton_7.clicked.connect(self.find)
        self.pushButton_8.clicked.connect(self.backup)
        self.pushButton_9.clicked.connect(self.open_btn_command)
        self.pushButton_10.clicked.connect(self.csv)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DataBase"))
        self.pushButton.setText(_translate("MainWindow", "Открыть БД"))
        self.pushButton_2.setText(_translate("MainWindow", "Создать БД"))
        self.pushButton_4.setText(_translate("MainWindow", "Сохранить"))
        self.pushButton_3.setText(_translate("MainWindow", "Добавить"))
        self.pushButton_5.setText(_translate("MainWindow", "Очистить"))
        self.pushButton_6.setText(_translate("MainWindow", "Удалить"))
        self.pushButton_7.setText(_translate("MainWindow", "Поиск"))
        self.pushButton_8.setText(_translate("MainWindow", "Создать back-up "))
        self.pushButton_9.setText(_translate("MainWindow", "Загрузить из back-up"))
        self.label.setText(_translate("MainWindow", "id"))
        self.label_2.setText(_translate("MainWindow", "name"))
        self.label_3.setText(_translate("MainWindow", "age"))
        self.label_4.setText(_translate("MainWindow", "email"))
        self.pushButton_10.setText(_translate("MainWindow", "Импорт БД"))

    def create_btn_command(self):
        db_file = filedialog.asksaveasfilename(defaultextension=".db", filetypes=[("SQLite Database Files", "*.db")])
        self.connection = sqlite3.connect(db_file)
        self.cursor = self.connection.cursor()

        fields = ["id INTEGER PRIMARY KEY", "name TEXT", "age INTEGER", "email TEXT"]

        fields_str = ", ".join(fields)
        
        if db_file:
            create_table = f"CREATE TABLE IF NOT EXISTS First ({fields_str})"
            self.cursor.execute(create_table)
            self.connection.commit()
            messagebox.showinfo("Success", "Database created successfully.")
        else:
            messagebox.showerror("Error", "Error")

    def open_btn_command(self):
        db_file = filedialog.askopenfilename(filetypes=[("SQLite Database Files", "*.db")])
        
        self.db = os.path.basename(db_file)
        print(self.db)
        if db_file:
            self.connection = sqlite3.connect(db_file)
            self.cursor = self.connection.cursor()
            messagebox.showinfo("Success", "Database opened successfully.")
            self.display_data()
        else:
            messagebox.showerror("Unluck :(", "Database not opened.")

    def display_data(self):
        self.cursor.execute("SELECT * FROM First")
        data = self.cursor.fetchall()

        self.tableView.setRowCount(len(data))
        self.tableView.setColumnCount(len(data[0]))

        for i, row in enumerate(data):
            for j, value in enumerate(row):
                item = QtWidgets.QTableWidgetItem(str(value))
                self.tableView.setItem(i, j, item)

    def add(self):
        id = self.lineEdit.text()
        car = self.lineEdit_2.text()
        year = self.lineEdit_3.text()
        price = self.lineEdit_4.text()

        db_mng = database_manager.DatabaseManager(self.connection, self.cursor, self.name, self.db)

        db_mng.add(id, car, year, price)

        self.display_data()
    
    def backup(self):
        db_mng = database_manager.DatabaseManager(self.connection, self.cursor, self.name, self.db)
        
        db_mng.create_backup()
        
    def csv(self):
        db_mng = database_manager.DatabaseManager(self.connection, self.cursor, self.name, self.db)
        
        db_mng.import_to_csv()
    
    def clear_fields(self):
        self.lineEdit.clear()
        self.lineEdit_2.clear()
        self.lineEdit_3.clear()
        self.lineEdit_4.clear()
        
    def find(self):
        rt = tk.Tk()
        rt.title("Result of finding")
        rt.geometry("900x600")
        self.cursor.execute("SELECT * FROM First WHERE id = ? OR car = ? OR year = ? OR price = ?", (self.lineEdit.text(), self.lineEdit_2.text(), self.lineEdit_3.text(), self.lineEdit_4.text(),))
        data = (row for row in self.cursor.fetchall())
    
        table = Table(rt, headings=('ID', 'Car', 'Year', 'Price'), rows=data)
        table.grid(column=2, row = 7)
        rt.mainloop()
    
        
class Table(tk.Frame):
    def __init__(self, parent=None, headings=tuple(), rows=tuple()):
        super().__init__(parent)

        table = ttk.Treeview(self, show="headings", selectmode="browse")
        table["columns"]=headings
        table["displaycolumns"]=headings

        for head in headings:
            table.heading(head, text=head, anchor=tk.CENTER)
            table.column(head, anchor=tk.CENTER)

        for row in rows:
            table.insert('', tk.END, values=tuple(row))

        scrolltable = tk.Scrollbar(self, command=table.yview)
        table.configure(yscrollcommand=scrolltable.set)
        scrolltable.pack(side=tk.RIGHT, fill=tk.Y)
        table.pack(expand=tk.YES, fill=tk.BOTH)

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
