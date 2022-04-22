# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rooms.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_proc_window(object):
    def setupUi(self, proc_window):
        proc_window.setObjectName("proc_window")
        proc_window.resize(810, 362)
        self.table_proc = QtWidgets.QTableWidget(proc_window)
        self.table_proc.setGeometry(QtCore.QRect(10, 10, 501, 341))
        self.table_proc.setObjectName("table_proc")
        self.table_proc.setColumnCount(5)
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
        self.horizontalLayoutWidget = QtWidgets.QWidget(proc_window)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(520, 10, 281, 41))
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
        self.add_button = QtWidgets.QPushButton(proc_window)
        self.add_button.setGeometry(QtCore.QRect(520, 290, 271, 31))
        self.add_button.setObjectName("add_button")
        self.remove_button = QtWidgets.QPushButton(proc_window)
        self.remove_button.setGeometry(QtCore.QRect(520, 320, 131, 31))
        self.remove_button.setObjectName("remove_button")
        self.back_button = QtWidgets.QPushButton(proc_window)
        self.back_button.setGeometry(QtCore.QRect(660, 320, 131, 31))
        self.back_button.setObjectName("back_button")
        self.formLayoutWidget = QtWidgets.QWidget(proc_window)
        self.formLayoutWidget.setGeometry(QtCore.QRect(520, 120, 271, 81))
        self.formLayoutWidget.setObjectName("formLayoutWidget")
        self.formLayout = QtWidgets.QFormLayout(self.formLayoutWidget)
        self.formLayout.setContentsMargins(0, 0, 0, 0)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.formLayoutWidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.room = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.room.setObjectName("room")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.room)
        self.label_2 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.flour = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.flour.setObjectName("flour")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.flour)
        self.label_3 = QtWidgets.QLabel(self.formLayoutWidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.place = QtWidgets.QLineEdit(self.formLayoutWidget)
        self.place.setObjectName("place")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.place)
        self.label_4 = QtWidgets.QLabel(proc_window)
        self.label_4.setGeometry(QtCore.QRect(610, 90, 91, 16))
        self.label_4.setObjectName("label_4")
        self.line = QtWidgets.QFrame(proc_window)
        self.line.setGeometry(QtCore.QRect(527, 60, 271, 20))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(proc_window)
        self.line_2.setGeometry(QtCore.QRect(520, 250, 271, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.report_button = QtWidgets.QPushButton(proc_window)
        self.report_button.setGeometry(QtCore.QRect(520, 260, 271, 31))
        self.report_button.setObjectName("report_button")

        self.retranslateUi(proc_window)
        QtCore.QMetaObject.connectSlotsByName(proc_window)

    def retranslateUi(self, proc_window):
        _translate = QtCore.QCoreApplication.translate
        proc_window.setWindowTitle(_translate("proc_window", "Номера"))
        item = self.table_proc.horizontalHeaderItem(0)
        item.setText(_translate("proc_window", "Номер"))
        item = self.table_proc.horizontalHeaderItem(1)
        item.setText(_translate("proc_window", "Этаж"))
        item = self.table_proc.horizontalHeaderItem(2)
        item.setText(_translate("proc_window", "Мест"))
        item = self.table_proc.horizontalHeaderItem(3)
        item.setText(_translate("proc_window", "Статус"))
        item = self.table_proc.horizontalHeaderItem(4)
        item.setText(_translate("proc_window", "ID"))
        self.search_button.setText(_translate("proc_window", "Поиск"))
        self.add_button.setText(_translate("proc_window", "Добавить"))
        self.remove_button.setText(_translate("proc_window", "Удалить"))
        self.back_button.setText(_translate("proc_window", "Назад"))
        self.label.setText(_translate("proc_window", "Номер:"))
        self.label_2.setText(_translate("proc_window", "Этаж:"))
        self.label_3.setText(_translate("proc_window", "Мест:"))
        self.label_4.setText(_translate("proc_window", "Добавить номер"))
        self.report_button.setText(_translate("proc_window", "Отчет о номерах"))



import sys
app = QtWidgets.QApplication(sys.argv)
proc_window = QtWidgets.QWidget()
ui = Ui_proc_window()
ui.setupUi(proc_window)

