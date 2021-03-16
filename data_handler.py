import pandas as pd


class DataHandler:

    def __init__(self, stud_filename=None, prices_filename=None):

        def trim_strings(x):
            return x.strip() if isinstance(x, str) else x

        self.df_students = pd.read_excel(stud_filename).fillna(0).applymap(trim_strings)
        self.df_prices_budget = pd.read_excel(prices_filename, sheet_name="Бюджет").applymap(trim_strings)
        self.df_prices_paid = pd.read_excel(prices_filename, sheet_name="Платники").applymap(trim_strings)

    def result_table(self, degree, group, form):
        counts = self.df_students.loc[(self.df_students['Ступень'] == degree) &
                                      (self.df_students['Группа'] == group) &
                                      (self.df_students['Форма обучения'] == form)]
        counts = counts[counts.columns[3:]]

        df = None
        if form == "бюджет очно" or form == "платники очно":
            df = self.df_prices_budget
        else:
            df = self.df_prices_paid

        prices = df.loc[(df['Ступень'] == degree) &
                        (df['Группа'] == group)]

        prices = prices[prices.columns[2:]]

        return counts.values * prices.values.transpose(), prices.columns.tolist(), counts.columns.tolist()
