import pandas as pd


class DataHandler:

    def __init__(self, stud_filename=None, prices_filename=None):

        def trim_strings(x):
            return x.strip() if isinstance(x, str) else x

        try:
            self.df_students = pd.read_excel(stud_filename).fillna(0).applymap(trim_strings)
        except Exception as e:
            raise AttributeError(f'Файл с с информацией о студентах\n{e}')
        try:
            self.df_prices_budget = pd.read_excel(prices_filename, sheet_name="Бюджет").applymap(trim_strings)
            self.df_prices_paid = pd.read_excel(prices_filename, sheet_name="Платники").applymap(trim_strings)
        except Exception as e:
            raise AttributeError(f'Файл с с информацией о затратах\n{e}')

    def result_table(self, degree, group, form):

        self._table_contains_keys(self.df_students, "Таблица с информацией о студентах",
                                  ['Ступень', 'Группа', 'Форма обучения'])

        counts = self.df_students.loc[(self.df_students['Ступень'] == degree) &
                                      (self.df_students['Группа'] == group) &
                                      (self.df_students['Форма обучения'] == form)]
        counts = counts[counts.columns[3:]]

        if form == "бюджетники" or form == "платники очно":
            df = self.df_prices_budget
        else:
            df = self.df_prices_paid

        self._table_contains_keys(df, "Таблица с информацией о затратах", ['Ступень', 'Группа'])

        prices = df.loc[(df['Ступень'] == degree) &
                        (df['Группа'] == group)]

        prices = prices[prices.columns[2:]]

        if counts.values.dtype == "object":
            raise ValueError("Таблица с информацией о студентах содержит нечисловые значения")
        if prices.values.dtype == "object":
            raise ValueError("Таблица с информацией о затратах содержит нечисловые значения")

        if counts.values.shape[0] == 0:
            raise ValueError(f"В таблице с информацией о студентах не нашлось значения по ключу "
                             f"('Ступень' = '{degree}', 'Группа' = '{group}', 'Форма обучения' = '{form}')")
        if prices.values.shape[0] == 0:
            raise ValueError(f"В таблице с информацией о затратах не нашлось значения по ключу "
                             f"('Ступень' = '{degree}', 'Группа' = '{group}')")

        if counts.values.shape[0] > 1:
            raise ValueError(f"В таблице с информацией о студентах нашлось несколько значений по ключу "
                             f"('Ступень' = '{degree}', 'Группа' = '{group}', 'Форма обучения' = '{form}')")
        if prices.values.shape[0] > 1:
            raise ValueError(f"В таблице с информацией о затратах нашлось несколько значений по ключу "
                             f"('Ступень' = '{degree}', 'Группа' = '{group}')")

        return counts.values * prices.values.transpose(), prices.columns.tolist(), counts.columns.tolist()

    @staticmethod
    def _table_contains_keys(df, table_name, keys):
        for key in keys:
            if key not in df.columns.tolist():
                raise KeyError(f'{table_name} не содержит ключа "{key}"')
