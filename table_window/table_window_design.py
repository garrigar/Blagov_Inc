# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'table_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(1500, 733)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout_2.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setSpacing(20)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(Form)
        font = QtGui.QFont()
        font.setBold(False)
        font.setWeight(50)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.label_spends = QtWidgets.QLabel(Form)
        self.label_spends.setObjectName("label_spends")
        self.horizontalLayout.addWidget(self.label_spends)
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.btn_save_table = QtWidgets.QPushButton(Form)
        self.btn_save_table.setEnabled(True)
        self.btn_save_table.setObjectName("btn_save_table")
        self.gridLayout.addWidget(self.btn_save_table, 0, 0, 1, 1)
        self.btn_build_graphs = QtWidgets.QPushButton(Form)
        self.btn_build_graphs.setObjectName("btn_build_graphs")
        self.gridLayout.addWidget(self.btn_build_graphs, 1, 0, 1, 1)
        self.comboBox_row_col = QtWidgets.QComboBox(Form)
        self.comboBox_row_col.setObjectName("comboBox_row_col")
        self.comboBox_row_col.addItem("")
        self.comboBox_row_col.addItem("")
        self.gridLayout.addWidget(self.comboBox_row_col, 1, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.label_description = QtWidgets.QLabel(Form)
        self.label_description.setObjectName("label_description")
        self.verticalLayout.addWidget(self.label_description)
        self.tableView = QtWidgets.QTableView(Form)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableView.sizePolicy().hasHeightForWidth())
        self.tableView.setSizePolicy(sizePolicy)
        self.tableView.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.tableView.setObjectName("tableView")
        self.verticalLayout.addWidget(self.tableView)
        self.horizontalLayout_2.addLayout(self.verticalLayout)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Анализ доходов институтов Самарского университета - Результаты"))
        self.label.setText(_translate("Form", "Обозначения институтов:\n"
"ИРКТ –институт ракетно-космической техники,\n"
"ИДЭУ – институт двигателей и энергетических установок,\n"
"ИАТ – институт авиационных двигателей,\n"
"ЕНИ – естественно-научный институт,\n"
"СГИ – социально-гуманитарный институт,\n"
"ИИМЭ – институт информатики, математики и электроники,\n"
"ИЭУ – институт экономики и управления,\n"
"ЮИ – юридический институт."))
        self.label_spends.setText(_translate("Form", "Обозначения затрат:\n"
""))
        self.btn_save_table.setText(_translate("Form", "Сохранить таблицу"))
        self.btn_build_graphs.setToolTip(_translate("Form", "<html><head/><body><p>Выделите ячейки с интересующими данными</p></body></html>"))
        self.btn_build_graphs.setText(_translate("Form", "Построить графики"))
        self.comboBox_row_col.setToolTip(_translate("Form", "<html><head/><body><p>По строкам - вывод графиков конкретных затрат по институтам</p><p>По столбцам - вывод графиков распределения затрат у конкретных институтов</p></body></html>"))
        self.comboBox_row_col.setItemText(0, _translate("Form", "по строкам"))
        self.comboBox_row_col.setItemText(1, _translate("Form", "по столбцам"))
        self.label_description.setText(_translate("Form", "Выбранные параметры:"))
