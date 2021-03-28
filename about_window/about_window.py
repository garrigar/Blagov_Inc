from PyQt5 import QtWidgets, QtGui

import definitions
from .about_window_design import Ui_Dialog


class AboutWindow(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        # Это здесь нужно для доступа к переменным, методам
        # и т.д. в файле about_window_design.py
        super().__init__()
        self.setupUi(self)  # Это нужно для инициализации нашего дизайна
        self.label_2.setPixmap(QtGui.QPixmap(definitions.resource_path('assets/logo2.png')))
