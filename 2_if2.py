"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""
def main(str_1, str_2):
    if type(str_1) != str and type(str_2) != str:
        return 0
    elif str_1 == str_2:
        return 1
    elif str_2 != 'learn' or (len(str_1) > len(str_2)):
        return 2 
    elif str_1 != str_2 and str_2 == 'learn':
        return 3

new_enter = main(1, 2)
print(new_enter)
new_enter = main('hello', 'hello')
print(new_enter)
new_enter = main('helllo', 'hello')
print(new_enter)
new_enter = main('hello', 'learn')
print(new_enter)