# Чтобы лучше разобраться в типах параметров функций Инна создала inspect_function(),
# которая в качестве аргумента принимает другую функцию
# (главное, не встроенную, built-in). В результате работы она выводит следующие данные:
# название анализируемой функции, наименование всех принимаемых ею параметров и их типы
# (позиционные, ключевые и т.п.). Попробуйте повторить результат девушки.
# Задачу увы решил не я, а чат GPT. Нужно разобрать её

import inspect


def inspect_function(function):
    """
    Функция для вывода информации о функции, принимаемой в качестве аргумента.

    Выводит информацию о названии функции, типах принимаемых параметров
    (позиционные, ключевые и т.п.).
    """
    # Получаем информацию о названии и аргументах функции
    function_name = function.__name__
    function_params = inspect.signature(function).parameters
    # Выводим информацию
    print("Function Name: {}".format(function_name))
    for param_name, param_details in function_params.items():
        print("Parameter Name: {}, Parameter Type: {}".format(param_name, param_details.kind))


# Тестируем функцию
def example_func(arg1, arg2, *args, keyword_arg1=None, keyword_arg2="default"):
    pass


inspect_function(example_func)
