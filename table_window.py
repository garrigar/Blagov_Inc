from itertools import groupby

from PyQt5 import QtWidgets


import numpy as np
import pandas as pd
import table_model
import table_window_design
import matplotlib.pyplot as plt


class TableWindow(QtWidgets.QWidget, table_window_design.Ui_Form):
    def __init__(self, dataframe, description):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        model = table_model.TableModel(dataframe)
        self.tableView.setModel(model)
        self.label_description.setText(description)

        self.btn_build_graphs.clicked.connect(self._handle_btn_build_graphs)

    def _handle_btn_build_graphs(self):
        selected_indexes = self.tableView.selectedIndexes()

        if len(selected_indexes) == 0:
            QtWidgets.QMessageBox.critical(self, "Ошибка", "Выберите ячейки")
            return

        selected_indexes = [(el.row(), el.column()) for el in selected_indexes]

        table_view_model = self.tableView.model()

        columns = table_view_model._data.columns.tolist()
        rows = [s[:1] + '-' + s[-5:] for s in table_view_model._data.index.tolist()]

        if self.comboBox_row_col.currentIndex() == 0:  # by rows
            component_to_look = 1
            x_axis_labels = columns
            graph_titles = rows

            def key(x):
                return x[0]

        else:  # by columns
            component_to_look = 0
            x_axis_labels = rows
            graph_titles = columns

            def key(x):
                return x[1]

        selected_indexes.sort(key=key)
        for graph_index, coordinates_tuples in groupby(selected_indexes, key=key):
            # нарисовать очередной график
            coordinates_tuples = list(coordinates_tuples)

            indexes = [t[component_to_look] for t in coordinates_tuples]

            xs = [x_axis_labels[i] for i in indexes]
            ys = [float(table_view_model.index(i, j).data()) for i, j in coordinates_tuples]

            plt.bar(xs, ys)
            plt.title(graph_titles[graph_index])
            plt.show()
#             TODO: multiple graphs simultaneously!
