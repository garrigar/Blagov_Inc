from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import Qt, QModelIndex
import copy

import definitions
import pandas as pd


class TableModel(QtCore.QAbstractTableModel):

    def __init__(self, dataframe):
        super(TableModel, self).__init__()
        self._orig_df = dataframe
        self._shown_df = copy.deepcopy(self._orig_df)
        self._recalculate_total()

    def data(self, index: QModelIndex, role: int = ...):
        if role == Qt.DisplayRole:
            value = self._shown_df.iloc[index.row(), index.column()]

            if index.column() == self.columnCount(index) - 1:
                if index.row() == self.rowCount(index) - 1:
                    return ""
                return f'{value:.3f}'

            return definitions.format_number(value)

        if role == Qt.TextAlignmentRole:
            if index.column() == self.columnCount(index) - 1:
                return Qt.AlignCenter
            return Qt.AlignRight + Qt.AlignVCenter
        if role == Qt.BackgroundColorRole:
            if index.column() == self.columnCount(index) - 1:
                return QtGui.QBrush(QtGui.QColor(*definitions.HEADER_COLOR_RGB))
            if (index.column() == self.columnCount(index) - 2) or (index.row() == self.rowCount(index) - 1):
                return QtGui.QBrush(QtGui.QColor(*definitions.TOTAL_COLOR_RGB))

    def rowCount(self, parent: QModelIndex = ...) -> int:
        return self._orig_df.shape[0]

    def columnCount(self, parent: QModelIndex = ...) -> int:
        return self._orig_df.shape[1]

    def headerData(self, section: int, orientation: Qt.Orientation, role: int = ...):
        # section is the index of the column/row.
        if role == Qt.DisplayRole:
            if orientation == Qt.Horizontal:
                return str(self._orig_df.columns[section])

            if orientation == Qt.Vertical:
                return str(self._orig_df.index[section])

        if role == Qt.TextAlignmentRole:
            return Qt.AlignCenter

    def flags(self, index):
        flags = super(self.__class__, self).flags(index)

        if index.column() == self.columnCount(index) - 1:
            if index.row() != self.rowCount(index) - 1:
                flags |= Qt.ItemIsEditable

        return flags

    def setData(self, index: QModelIndex, value, role: int = ...) -> bool:
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

    def get_output_dataframe(self):
        spends_short = self._shown_df.index.tolist()
        spends_long = [definitions.SPENDS_NAMES[spend_name] for spend_name in spends_short[:-1]]
        spends_long.append(spends_short[-1])  # ИТОГО не удлинняется
        df = pd.DataFrame(self._shown_df.values, columns=self._shown_df.columns.tolist(), index=spends_long)
        df.iloc[-1, -1] = None  # rightmost bottom cell is getting "muted"
        return df

    def get_cell_value(self, i, j):
        return self._shown_df.iloc[i, j]

    def get_coefficients(self):
        return self._shown_df.iloc[:, -1].values[:-1]

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
