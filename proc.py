# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'employee.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_proc_window(object):
    def setupUi(self, proc_window):
        proc_window.setObjectName("proc_window")
        proc_window.resize(909, 401)
        self.table_proc = QtWidgets.QTableWidget(proc_window)
        self.table_proc.setGeometry(QtCore.QRect(10, 10, 601, 381))
        self.table_proc.setObjectName("table_proc")
        self.table_proc.setColumnCount(6)
        self.table_proc.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_proc.setHorizontalHeaderItem(5, item)
        self.horizontalLayoutWidget = QtWidgets.QWidget(proc_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(620, 10, 281, 41))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.search_entry = QtWidgets.QLineEdit(self.horizontalLayoutWidget)
        self.search_entry.setObjectName("search_entry")
        self.horizontalLayout.addWidget(self.search_entry)
        self.search_button = QtWidgets.QPushButton(self.horizontalLayoutWidget)
        self.search_button.setObjectName("search_button")
        self.horizontalLayout.addWidget(self.search_button)
        self.line = QtWidgets.QFrame(proc_window)
        self.line.setGeometry(QtCore.QRect(620, 50, 281, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.formLayoutWidget = QtWidgets.QWidget(proc_window)
        self.formLayoutWidget.setGeometry(QtCore.QRect(620, 90, 271, 183))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.label_6 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.label_7 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_7.setText("")
        self.label_7.setObjectName("label_7")
        self.formLayout.setWidget(6, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.label_8 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_8.setText("")
        self.label_8.setObjectName("label_8")
        self.formLayout.setWidget(7, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.name = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.name.setObjectName("name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.name)
        self.room = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room.setObjectName("room")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.room)
        self.time = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.time.setObjectName("time")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.time)
        self.rest = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.rest.setObjectName("rest")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.rest)
        self.more = QtWidgets.QComboBox(self.formLayoutWidget)
        self.more.setObjectName("more")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.more)
        self.label_9 = QtWidgets.QLabel(proc_window)
        self.label_9.setGeometry(QtCore.QRect(680, 70, 161, 16))
        self.label_9.setObjectName("label_9")
        self.add_button = QtWidgets.QPushButton(proc_window)
        self.add_button.setGeometry(QtCore.QRect(620, 290, 271, 31))
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(proc_window)
        self.remove_button.setGeometry(QtCore.QRect(620, 320, 131, 31))
        self.remove_button.setObjectName("remove_button")
        self.back_button = QtWidgets.QPushButton(proc_window)
        self.back_button.setGeometry(QtCore.QRect(760, 320, 131, 31))
        self.back_button.setObjectName("back_button")

        self.retranslateUi(proc_window)
        QtCore.QMetaObject.connectSlotsByName(proc_window)

    def retranslateUi(self, proc_window):
        _translate = QtCore.QCoreApplication.translate
        proc_window.setWindowTitle(_translate("proc_window", "Процедуры"))
        item = self.table_proc.horizontalHeaderItem(0)
        item.setText(_translate("proc_window", "Названвие"))
        item = self.table_proc.horizontalHeaderItem(1)
        item.setText(_translate("proc_window", "Кабинет"))
        item = self.table_proc.horizontalHeaderItem(2)
        item.setText(_translate("proc_window", "График"))
        item = self.table_proc.horizontalHeaderItem(3)
        item.setText(_translate("proc_window", "Перерыв"))
        item = self.table_proc.horizontalHeaderItem(4)
        item.setText(_translate("proc_window", "Отвественный"))
        item = self.table_proc.horizontalHeaderItem(5)
        item.setText(_translate("proc_window", "ID"))
        self.search_button.setText(_translate("proc_window", "Поиск"))
        self.label.setText(_translate("proc_window", "Название:"))
        self.label_2.setText(_translate("proc_window", "Кабинет:"))
        self.label_3.setText(_translate("proc_window", "График:"))
        self.label_4.setText(_translate("proc_window", "Перерыв:"))
        self.label_5.setText(_translate("proc_window", "Отвественный:"))
        self.label_9.setText(_translate("proc_window", "Добавить новую процедуру"))
        self.add_button.setText(_translate("proc_window", "Добавить"))
        self.remove_button.setText(_translate("proc_window", "Удалить"))
        self.back_button.setText(_translate("proc_window", "Назад"))



import sys
app = QtWidgets.QApplication(sys.argv)
proc_window = QtWidgets.QWidget()
ui = Ui_proc_window()
ui.setupUi(proc_window)
# proc_window.show()
# sys.exit(app.exec_())
