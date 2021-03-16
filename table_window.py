import sys  # sys нужен для передачи argv в QApplication
import os  # Отсюда нам понадобятся методы для отображения содержимого директорий

from PyQt5 import QtWidgets

import main_window_design  # Это наш конвертированный файл дизайна
import data_handler
import os.path
import numpy as np
import pandas as pd
import table_model
import table_window_design

class TableWindow(QtWidgets.QWidget, table_window_design.Ui_Form):
    def __init__(self, dataframe, description):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле main_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна

        model = table_model.TableModel(dataframe)
        self.tableView.setModel(model)
        self.label_description.setText(description)


