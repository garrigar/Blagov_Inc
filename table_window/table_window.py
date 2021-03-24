from itertools import groupby

import matplotlib.pyplot as plt
import numpy as np
from PyQt5 import QtWidgets

import table_model
from .table_window_design import Ui_Form


class TableWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, dataframe, description):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self._description = description
        self.label_description.setText(self._description)

        dataframe['Коэффициент'] = np.ones(dataframe.shape[0])
        dataframe.loc['ИТОГО'] = np.zeros(dataframe.shape[1])

        self._columns_names = dataframe.columns.tolist()
        self._rows_names = dataframe.index.tolist()

        self._model = table_model.TableModel(dataframe)
        self.tableView.setModel(self._model)

        self.btn_save_table.clicked.connect(lambda: self._handle_btn_save_table(
            "Сохранение таблицы"))
        self.btn_build_graphs.clicked.connect(self._handle_btn_build_graphs)

    def _handle_btn_build_graphs(self):
        selected_indexes = self.tableView.selectedIndexes()

        selected_indexes = [(el.row(), el.column()) for el in selected_indexes
                            if el.column() != (len(self._columns_names) - 1)]

        if len(selected_indexes) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Выберите ячейки")
            return

        def first(x):
            return x[0]

        def second(x):
            return x[1]

        if self.comboBox_row_col.currentIndex() == 0:  # by rows
            key_sort_groupby = first
            graph_titles = self._rows_names
            key_indexes = second
            x_axis_labels = self._columns_names

        else:  # by columns
            key_sort_groupby = second
            graph_titles = self._columns_names
            key_indexes = first
            x_axis_labels = self._rows_names

        selected_indexes.sort(key=key_sort_groupby)
        for graph_index, coordinates_tuples in groupby(selected_indexes, key=key_sort_groupby):
            # нарисовать очередной график
            coordinates_tuples = list(coordinates_tuples)

            xs = [x_axis_labels[i] for i in map(key_indexes, coordinates_tuples)]
            ys = [self._model.get_cell_value(i, j) for i, j in coordinates_tuples]

            self._show_graph(xs, ys, graph_titles[graph_index])

        plt.show()

    def _show_graph(self, xs, ys, title):
        fig = plt.figure()
        fig.canvas.set_window_title(title)
        plt.bar(xs, ys)
        plt.grid()
        plt.ylabel("Рублей (тыс.)")
        for index in range(len(ys)):
            plt.text(index, ys[index] + 1, round(ys[index], 1), horizontalalignment='center')

        plt.title(title + '\n' + self._description.replace(";", ";\n"))

    def _handle_btn_save_table(self, prompt):
        # Данный метод сохраняет выведенную на экран таблицу (в table_window) по нажатию на кнопку сохранить
        filename = QtWidgets.QFileDialog.getSaveFileName(self, prompt, "", "Excel-файлы (*.xlsx)")
        if filename[0] == "":
            return
        # print(f'"{filename[0]}"')
        try:
            self._model.get_dataframe().to_excel(filename[0], sheet_name=self._description)  # TODO: description
        except Exception as e:
            print("Ошибка сохранения таблицы!")
            print(e)
