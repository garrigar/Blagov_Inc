from bidict import bidict

SPENDS_NAMES = bidict()
SPENDS_NAMES.update({
    '1': "Затраты на фонд оплаты труда институтов",
    '2': "Затраты на закупку материалов и оборудования",
    '3': "Затраты на командировки и стажировки",
    '4': "Затраты на культурно-массовую и физкультурно-оздоровительную работу со студентами",
    '5': "Затраты на фонд оплаты труда прочего персонала",
    '6': "Прочие затраты"
})

HEADER_COLOR_RGB = (207, 207, 207)

DIGITS_AFTER_DECIMAL = 2
DELIMITER_IS_SPACE = True


def format_number(value):
    string = ('{:,.' + str(DIGITS_AFTER_DECIMAL) + 'f}').format(value)
    if DELIMITER_IS_SPACE:
        return string.replace(',', ' ').replace('.', ',')
    else:
        return string.replace(',', 'X').replace('.', ',').replace('X', '.')
