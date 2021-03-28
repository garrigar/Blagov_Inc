from PyQt5 import QtWidgets, QtGui
import sys  # sys нужен для передачи argv в QApplication
import ctypes

import definitions
from main_window import MainWindow


def main():
    my_app_id = 'ru.garari.institutesincomeanalysis'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(my_app_id)
    app = QtWidgets.QApplication(sys.argv)  # Новый экземпляр QApplication
    app.setWindowIcon(QtGui.QIcon(definitions.resource_path('assets/logo1.png')))
    window = MainWindow()  # Создаём объект класса MainWindow
    window.show()  # Показываем окно
    app.exec_()  # и запускаем приложение


if __name__ == '__main__':  # Если мы запускаем файл напрямую, а не импортируем
    main()  # то запускаем функцию main()
