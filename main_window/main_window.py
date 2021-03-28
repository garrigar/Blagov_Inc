import os  # Отсюда нам понадобятся методы для отображения содержимого директорий
import os.path

import numpy as np
import pandas as pd
from PyQt5 import QtWidgets

import data_handler
from about_window import AboutWindow
from table_window import TableWindow
from .main_window_design import Ui_MainWindow
import definitions


class MainWindow(QtWidgets.QMainWindow, Ui_MainWindow):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self._about_window = AboutWindow()
        self.action_about.triggered.connect(self._about_window.show)

        self._list_chb_st = [self.chb_st_bak, self.chb_st_mag, self.chb_st_asp]
        self._list_chb_group = [self.chb_group_1, self.chb_group_2, self.chb_group_3]
        self._list_chb_form = [self.chb_form_budget, self.chb_form_pay_full, self.chb_form_pay_dist]

        self._bind_master_and_servants(self.chb_st_all, self._list_chb_st)
        self._bind_master_and_servants(self.chb_group_all, self._list_chb_group)
        self._bind_master_and_servants(self.chb_form_all, self._list_chb_form)

        self.button_submit_file_stud.clicked.connect(lambda: self._handle_file_select_button(
            "Выберите файл с информацией о студентах", self.ledit_numb_stud))

        self.button_submit_file_price.clicked.connect(lambda: self._handle_file_select_button(
            "Выберите файл с информацией о затратах", self.ledit_price))

        self.button_gen.clicked.connect(self._handle_gen_button)

        # self.ledit_numb_stud.setText(r'C:/Users/Admin/Documents/PROGRAMMING/Python/Projects/Blagov_Inc/xls/1.xls')
        # self.ledit_price.setText(r'C:/Users/Admin/Documents/PROGRAMMING/Python/Projects/Blagov_Inc/xls/2.xlsx')

        self._table_windows = []

    def _open_table(self, dataframe, description):
        tw = TableWindow(dataframe, description)
        tw.show()
        self._table_windows.append(tw)

    def _bind_master_and_servants(self, master_checkbox, servant_checkboxes: list):

        def main_handler():
            is_checked = master_checkbox.isChecked()
            for chb1 in servant_checkboxes:
                chb1.setChecked(is_checked)

        master_checkbox.clicked.connect(main_handler)

        def servant_handler():
            if not self.sender().isChecked():
                master_checkbox.setChecked(False)

        for chb2 in servant_checkboxes:
            chb2.clicked.connect(servant_handler)

    def _handle_file_select_button(self, prompt, label_edit):
        filename = QtWidgets.QFileDialog.getOpenFileName(self, prompt, "", "Excel-файлы (*.xls *.xlsx)")
        label_edit.setText(filename[0])

    def _check_file_exists(self, file, filename):
        if filename is None or filename == '':
            QtWidgets.QMessageBox.critical(self, file, "Пустое имя файла")
            return False
        if not os.path.isfile(filename):
            QtWidgets.QMessageBox.critical(self, file, f"Файл \n'{filename}'\n не существует")
            return False
        return True

    @staticmethod
    def _filter_selected_checkboxes(list_chb):
        return [chb for chb in list_chb if chb.isChecked()]

    def _handle_gen_button(self):

        try:
            filename_stud = self.ledit_numb_stud.text()
            filename_prices = self.ledit_price.text()

            if self._check_file_exists("Файл с информацией о студентах", filename_stud) \
                    and self._check_file_exists("Файл с информацией о затратах", filename_prices):

                data_hnd = data_handler.DataHandler(filename_stud, filename_prices)

                list_chb_st = self._filter_selected_checkboxes(self._list_chb_st)
                list_chb_group = self._filter_selected_checkboxes(self._list_chb_group)
                list_chb_form = self._filter_selected_checkboxes(self._list_chb_form)

                if len(list_chb_st) == 0 or len(list_chb_form) == 0 or len(list_chb_group) == 0:
                    QtWidgets.QMessageBox.about(self, "Внимание", "Не все параметры выбраны")
                    return

                array_sample, spends_list, institutes_list = data_hnd.result_table(list_chb_st[0].property("key"),
                                                                                   list_chb_group[0].property("key"),
                                                                                   list_chb_form[0].property("key"))
                ans = np.zeros_like(array_sample, dtype=np.float64)

                desc_degrees = [chb_st.property("key") for chb_st in list_chb_st]
                desc_groups = [chb_group.property("key") for chb_group in list_chb_group]
                desc_forms = [chb_form.property("key") for chb_form in list_chb_form]

                # k = 0

                for chb_st in list_chb_st:
                    for chb_group in list_chb_group:
                        for chb_form in list_chb_form:
                            # k += 1
                            degree = chb_st.property("key")
                            group = chb_group.property("key")
                            form = chb_form.property("key")
                            ans += data_hnd.result_table(degree, group, form)[0]

                # print(k)

                # обрезаем "ИТОГО"
                ans = ans[:-1]
                spends_list = spends_list[:-1]

                spends_short_list = [definitions.SPENDS_NAMES.inv[spend_name] for spend_name in spends_list]

                data = pd.DataFrame(ans, columns=institutes_list, index=spends_short_list)

                desc_str = "ступени: {" + ', '.join(desc_degrees) + "}; " \
                           "группы: {" + ', '.join(desc_groups) + "}; " \
                           "формы: {" + ', '.join(desc_forms) + "}"

                self._open_table(data, desc_str)

        except Exception as e:
            print(e)
            QtWidgets.QMessageBox.critical(self, "Ошибка: возникло исключение", str(e))

