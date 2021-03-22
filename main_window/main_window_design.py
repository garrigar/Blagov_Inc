# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_window_design.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(655, 281)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(655, 281))
        MainWindow.setMaximumSize(QtCore.QSize(655, 281))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.l_steps = QtWidgets.QLabel(self.centralwidget)
        self.l_steps.setGeometry(QtCore.QRect(20, 140, 111, 21))
        self.l_steps.setAlignment(QtCore.Qt.AlignCenter)
        self.l_steps.setObjectName("l_steps")
        self.chb_st_bak = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_st_bak.setGeometry(QtCore.QRect(20, 160, 121, 31))
        self.chb_st_bak.setChecked(False)
        self.chb_st_bak.setTristate(False)
        self.chb_st_bak.setObjectName("chb_st_bak")
        self.chb_st_asp = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_st_asp.setGeometry(QtCore.QRect(20, 210, 111, 17))
        self.chb_st_asp.setChecked(False)
        self.chb_st_asp.setTristate(False)
        self.chb_st_asp.setObjectName("chb_st_asp")
        self.chb_st_mag = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_st_mag.setGeometry(QtCore.QRect(20, 190, 111, 17))
        self.chb_st_mag.setChecked(False)
        self.chb_st_mag.setTristate(False)
        self.chb_st_mag.setObjectName("chb_st_mag")
        self.chb_st_all = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_st_all.setGeometry(QtCore.QRect(20, 230, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setItalic(True)
        self.chb_st_all.setFont(font)
        self.chb_st_all.setChecked(False)
        self.chb_st_all.setTristate(False)
        self.chb_st_all.setObjectName("chb_st_all")
        self.chb_group_all = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_group_all.setGeometry(QtCore.QRect(150, 230, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setItalic(True)
        self.chb_group_all.setFont(font)
        self.chb_group_all.setChecked(False)
        self.chb_group_all.setTristate(False)
        self.chb_group_all.setObjectName("chb_group_all")
        self.l_groups = QtWidgets.QLabel(self.centralwidget)
        self.l_groups.setGeometry(QtCore.QRect(150, 140, 111, 21))
        self.l_groups.setAlignment(QtCore.Qt.AlignCenter)
        self.l_groups.setObjectName("l_groups")
        self.chb_group_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_group_3.setGeometry(QtCore.QRect(150, 210, 111, 17))
        self.chb_group_3.setChecked(False)
        self.chb_group_3.setTristate(False)
        self.chb_group_3.setObjectName("chb_group_3")
        self.chb_group_1 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_group_1.setGeometry(QtCore.QRect(150, 160, 111, 31))
        self.chb_group_1.setChecked(False)
        self.chb_group_1.setTristate(False)
        self.chb_group_1.setObjectName("chb_group_1")
        self.chb_group_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_group_2.setGeometry(QtCore.QRect(150, 190, 111, 17))
        self.chb_group_2.setChecked(False)
        self.chb_group_2.setTristate(False)
        self.chb_group_2.setObjectName("chb_group_2")
        self.chb_form_all = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_form_all.setGeometry(QtCore.QRect(270, 230, 111, 17))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(9)
        font.setItalic(True)
        self.chb_form_all.setFont(font)
        self.chb_form_all.setChecked(False)
        self.chb_form_all.setTristate(False)
        self.chb_form_all.setObjectName("chb_form_all")
        self.l_form = QtWidgets.QLabel(self.centralwidget)
        self.l_form.setGeometry(QtCore.QRect(270, 140, 111, 21))
        self.l_form.setAlignment(QtCore.Qt.AlignCenter)
        self.l_form.setObjectName("l_form")
        self.chb_form_pay_dist = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_form_pay_dist.setGeometry(QtCore.QRect(270, 210, 131, 17))
        self.chb_form_pay_dist.setChecked(False)
        self.chb_form_pay_dist.setTristate(False)
        self.chb_form_pay_dist.setObjectName("chb_form_pay_dist")
        self.chb_form_bud_full = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_form_bud_full.setGeometry(QtCore.QRect(270, 160, 111, 31))
        self.chb_form_bud_full.setChecked(False)
        self.chb_form_bud_full.setTristate(False)
        self.chb_form_bud_full.setObjectName("chb_form_bud_full")
        self.chb_form_pay_full = QtWidgets.QCheckBox(self.centralwidget)
        self.chb_form_pay_full.setGeometry(QtCore.QRect(270, 190, 111, 17))
        self.chb_form_pay_full.setChecked(False)
        self.chb_form_pay_full.setTristate(False)
        self.chb_form_pay_full.setObjectName("chb_form_pay_full")
        self.button_gen = QtWidgets.QPushButton(self.centralwidget)
        self.button_gen.setGeometry(QtCore.QRect(440, 195, 171, 31))
        self.button_gen.setObjectName("button_gen")
        self.ledit_numb_stud = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_numb_stud.setGeometry(QtCore.QRect(30, 50, 271, 20))
        self.ledit_numb_stud.setText("")
        self.ledit_numb_stud.setObjectName("ledit_numb_stud")
        self.ledit_price = QtWidgets.QLineEdit(self.centralwidget)
        self.ledit_price.setGeometry(QtCore.QRect(340, 50, 271, 20))
        self.ledit_price.setText("")
        self.ledit_price.setObjectName("ledit_price")
        self.l_numb_stud = QtWidgets.QLabel(self.centralwidget)
        self.l_numb_stud.setGeometry(QtCore.QRect(30, 20, 271, 21))
        self.l_numb_stud.setAlignment(QtCore.Qt.AlignCenter)
        self.l_numb_stud.setObjectName("l_numb_stud")
        self.l_price = QtWidgets.QLabel(self.centralwidget)
        self.l_price.setGeometry(QtCore.QRect(340, 20, 271, 21))
        self.l_price.setAlignment(QtCore.Qt.AlignCenter)
        self.l_price.setObjectName("l_price")
        self.button_submit_file_stud = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit_file_stud.setGeometry(QtCore.QRect(90, 90, 141, 31))
        self.button_submit_file_stud.setObjectName("button_submit_file_stud")
        self.button_submit_file_price = QtWidgets.QPushButton(self.centralwidget)
        self.button_submit_file_price.setGeometry(QtCore.QRect(400, 90, 141, 31))
        self.button_submit_file_price.setObjectName("button_submit_file_price")
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Анализ доходов институтов - Выбор параметров"))
        self.l_steps.setText(_translate("MainWindow", "Ступени"))
        self.chb_st_bak.setText(_translate("MainWindow", "Бакалавры \n"
"+ Специалисты"))
        self.chb_st_bak.setProperty("key", _translate("MainWindow", "бакалавры"))
        self.chb_st_asp.setText(_translate("MainWindow", "Аспиранты"))
        self.chb_st_asp.setProperty("key", _translate("MainWindow", "аспиранты"))
        self.chb_st_mag.setText(_translate("MainWindow", "Магистры"))
        self.chb_st_mag.setProperty("key", _translate("MainWindow", "магистры"))
        self.chb_st_all.setText(_translate("MainWindow", "Выбрать все"))
        self.chb_group_all.setText(_translate("MainWindow", "Выбрать все"))
        self.l_groups.setText(_translate("MainWindow", "Группы"))
        self.chb_group_3.setText(_translate("MainWindow", "3"))
        self.chb_group_3.setProperty("key", _translate("MainWindow", "3 группа"))
        self.chb_group_1.setText(_translate("MainWindow", "1"))
        self.chb_group_1.setProperty("key", _translate("MainWindow", "1 группа"))
        self.chb_group_2.setText(_translate("MainWindow", "2"))
        self.chb_group_2.setProperty("key", _translate("MainWindow", "2 группа"))
        self.chb_form_all.setText(_translate("MainWindow", "Выбрать все"))
        self.l_form.setText(_translate("MainWindow", "Форма обучения"))
        self.chb_form_pay_dist.setText(_translate("MainWindow", "Платники заочно"))
        self.chb_form_pay_dist.setProperty("key", _translate("MainWindow", "платники заочно"))
        self.chb_form_bud_full.setText(_translate("MainWindow", "Бюджет очно"))
        self.chb_form_bud_full.setProperty("key", _translate("MainWindow", "бюджет очно"))
        self.chb_form_pay_full.setText(_translate("MainWindow", "Платники очно"))
        self.chb_form_pay_full.setProperty("key", _translate("MainWindow", "платники очно"))
        self.button_gen.setText(_translate("MainWindow", "Сгенерировать"))
        self.ledit_numb_stud.setPlaceholderText(_translate("MainWindow", "Файл студентов"))
        self.ledit_price.setPlaceholderText(_translate("MainWindow", "Файл расценок"))
        self.l_numb_stud.setText(_translate("MainWindow", "Количество студентов"))
        self.l_price.setText(_translate("MainWindow", "Расценки"))
        self.button_submit_file_stud.setText(_translate("MainWindow", "Выбрать"))
        self.button_submit_file_price.setText(_translate("MainWindow", "Выбрать"))