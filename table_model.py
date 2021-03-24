from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt
import copy

import definitions


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, dataframe):
        super(TableModel, self).__init__()
        self._orig_df = dataframe
        self._shown_df = copy.deepcopy(self._orig_df)
        self._recalculate_total()

    def data(self, index, role):
        if role == Qt.DisplayRole:
            value = self._shown_df.iloc[index.row(), index.column()]

            if index.column() == self.columnCount(index) - 1:
                if index.row() == self.rowCount(index) - 1:
                    return ""
                return f'{value:.3f}'

            return f'{value:.1f}'

        if role == Qt.TextAlignmentRole:
            if index.column() == self.columnCount(index) - 1:
                return Qt.AlignCenter
            return Qt.AlignRight + Qt.AlignVCenter
        if role == Qt.BackgroundColorRole:
            if index.column() == self.columnCount(index) - 1:
                return QtGui.QBrush(QtGui.QColor(*definitions.HEADER_COLOR_RGB))

    def rowCount(self, index):
        return self._orig_df.shape[0]

    def columnCount(self, index):
        return self._orig_df.shape[1]

    def headerData(self, section, orientation, role):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._orig_df.columns[section])

            if orientation == Qt.Vertical:
                return str(self._orig_df.index[section])
        # if role == Qt.BackgroundColorRole:
        #     return QtGui.QBrush(Qt.gray)

    def flags(self, index):
        flags = super(self.__class__, self).flags(index)

        if index.column() == self.columnCount(index) - 1:
            if index.row() != self.rowCount(index) - 1:
                flags |= Qt.ItemIsEditable

        return flags

    def setData(self, index, value, role):
        if role == Qt.EditRole:
            if index.column() == self.columnCount(index) - 1:
                if self._validate_coefficient(value):
                    self._recalculate_row(index.row(), float(value))
                    return True
        return False

    def _recalculate_total(self):
        self._shown_df.iloc[-1] = self._shown_df.iloc[:-1].sum()

    def _recalculate_row(self, row_index, coefficient):
        self._shown_df.iloc[row_index] = self._orig_df.iloc[row_index] * coefficient
        self._recalculate_total()

    def get_dataframe(self):
        return self._shown_df

    def get_cell_value(self, i, j):
        return self._shown_df.iloc[i, j]

    @staticmethod
    def _validate_coefficient(value) -> bool:
        if value is None:
            return False
        if value == "":
            return False
        try:
            float_value = float(value)
            if 0 <= float_value <= 1:
                return True
            return False
        except ValueError:
            return False
