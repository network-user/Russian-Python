import re


class RussianTransformer:
    """
    Класс переводит русские слова на английские.
    """
    # Замены для синтаксических конструкций
    syntax_replacements = {
        'пока': 'while',
        'для': 'for',
        'если': 'if',
        'иначе': 'else',
        'попробовать': 'try',
        'поймать': 'except',
        'наконец': 'finally',
        'выход': 'break',
        'продолжить': 'continue',
        'импорт': 'import',
    }

    # Замены для арифметических операций
    arithmetic_replacements = {
        'сложение': 'add',
        'вычитание': 'sub',
        'умножение': 'mul',
        'деление': 'div',
        'целдел': 'floordiv',
        'ост': 'mod',
        'степень': 'pow',
        'логический': 'bool',
    }

    # Замены для логических операций
    logical_replacements = {
        'и': 'and',
        'или': 'or',
        'не': 'not',
    }

    # Замены для функций и методов
    function_replacements = {
        "абс": "abs",
        "длина": "len",
        "округлить": "round",
        "максимум": "max",
        "минимум": "min",
        "строка": "str",
        "число": "int",
        "нецелое": "float",
        "комплексное": "complex",
        "сортировать": "sort",
        "добавить": "append",
        "удалить": "remove",
        "вставить": "insert",
        "разделить": "split",
        "обрезать": "strip",
        "свойство": "property",
    }

    # Замены для обработки ошибок
    error_replacements = {
        "ОшибкаАрифметики": "ArithmeticError",
        "ОшибкаИндекса": "IndexError",
        "ОшибкаКлюча": "KeyError",
        "ОшибкаЗначения": "ValueError",
    }

    # Замены для структур данных
    data_structure_replacements = {
        "список": "list",
        "словарь": "dict",
        "множество": "set",
        "кортеж": "tuple",
    }

    # Замены для неопределенных команд
    other_replacements = {
        "вывод": "print",
        "ввод": "input",
    }

    replacements = {
        **syntax_replacements,
        **arithmetic_replacements,
        **logical_replacements,
        **function_replacements,
        **error_replacements,
        **data_structure_replacements,
        **other_replacements
    }

    @staticmethod
    def transform(code):
        """
        Преобразует русские ключевые слова в данном коде в английские
        эквиваленты.
        """
        for russian, english in RussianTransformer.replacements.items():
            code = re.sub(rf'\b{russian}\b', english, code)
        return code
