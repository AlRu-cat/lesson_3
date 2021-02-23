# 3. Написать функцию thesaurus(), принимающую в качестве аргументов имена сотрудников и возвращающую словарь,
# в котором ключи — первые буквы имен, а значения — списки, содержащие имена, начинающиеся с соответствующей буквы.
# Например:
#
# >>> >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки? Сможете ли вы вернуть отсортированный по ключам словарь?
from typing import List, Any

import kwargs

workers = "Иван", "Мария", "Петр", "Илья", "Павел", "Марина"


# noinspection PyArgumentList
def thesaurus(workers):
    workers_in_work = list(workers)
    names = {}
    for i in range(len(workers_in_work)):

        a = workers_in_work[i]
        b = a[0]

        names.setdefault(b, []).append(a)






    print(names)

thesaurus(workers)