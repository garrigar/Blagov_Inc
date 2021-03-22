from itertools import groupby

import matplotlib.pyplot as plt
from PyQt5 import QtWidgets

import table_model
from .table_window_design import Ui_Form


class TableWindow(QtWidgets.QWidget, Ui_Form):
    def __init__(self, dataframe, description):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        self._dataframe = dataframe
        self._description = description

        model = table_model.TableModel(self._dataframe)
        self.tableView.setModel(model)
        self.label_description.setText(self._description)

        self.btn_build_graphs.clicked.connect(self._handle_btn_build_graphs)

    def _handle_btn_build_graphs(self):
        selected_indexes = self.tableView.selectedIndexes()

        if len(selected_indexes) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Выберите ячейки")
            return

        selected_indexes = [(el.row(), el.column()) for el in selected_indexes]

        table_view_model = self.tableView.model()

        columns = table_view_model._data.columns.tolist()
        rows = [s[:1] + '. ' + s.split()[-1] for s in table_view_model._data.index.tolist()]

        def first(x):
            return x[0]

        def second(x):
            return x[1]

        if self.comboBox_row_col.currentIndex() == 0:  # by rows
            key_sort_groupby = first
            graph_titles = rows
            key_indexes = second
            x_axis_labels = columns

        else:  # by columns
            key_sort_groupby = second
            graph_titles = columns
            key_indexes = first
            x_axis_labels = rows

        selected_indexes.sort(key=key_sort_groupby)
        for graph_index, coordinates_tuples in groupby(selected_indexes, key=key_sort_groupby):
            # нарисовать очередной график
            coordinates_tuples = list(coordinates_tuples)

            xs = [x_axis_labels[i] for i in map(key_indexes, coordinates_tuples)]
            ys = [float(table_view_model.index(i, j).data()) for i, j in coordinates_tuples]

            self._show_graph(xs, ys, graph_titles[graph_index])

        plt.show()

    def _show_graph(self, xs, ys, title):
        fig = plt.figure()
        fig.canvas.set_window_title(title)
        plt.bar(xs, ys)
        plt.title(f'{title}\n{self._description}')
