# 2. * (вместо задачи 1) Доработать предыдущую функцию num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы. Например:
#
# >>> >>> num_translate_adv("One")
# "Один"
# >>> num_translate_adv("two")
# "два"

numbers = {
    'zero': 'ноль',
    'one': 'один',
    'two': 'два',
    'three': 'три',
    'four' : 'четыре',
    'five' : 'пять',
    'six' : 'шесть',
    'seven' : 'семь',
    'eight' : 'восемь',
    'nine' : 'девять',
    'ten' : 'десять',


    'Zero': 'Ноль',
    'One': 'Один',
    'Two': 'Два',
    'Three': 'Три',
    'Four' : 'Четыре',
    'Five' : 'Пять',
    'Six' : 'Шесть',
    'Seven' : 'Семь',
    'Eight' : 'Восемь',
    'Nine' : 'Девять',
    'Ten' : 'Десять'

}

number = input('Введите необходимое английское число для перевода: ')


def num_translate_adv():
    print(numbers.get(number))



num_translate_adv()