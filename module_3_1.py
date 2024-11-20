#Задача "Счётчик вызовов":
#Вам необходимо написать 3 функции:
#Функция count_calls подсчитывающая вызовы остальных функций.
#Функция string_info принимает аргумент - строку и возвращает кортеж из: длины этой строки, строку в верхнем регистре,
    # строку в нижнем регистре.
#Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
    # False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
#Пункты задачи:
#Создать переменную calls = 0 вне функций.
#Создать функцию count_calls и изменять в ней значение переменной calls. Эта функция должна вызываться в остальных двух функциях.
#Создать функцию string_info с параметром string и реализовать логику работы по описанию.
#Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
#Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
#Вывести значение переменной calls на экран(в консоль).

#Решение:

calls = 0
def count_calls():
    global calls
    calls += 1
def string_info(string):
    count_calls()
    number = len(string)
    up = string.upper()
    low = string.lower()
    return (number, up, low)
def is_contains(string, list_to_search):
    count_calls()
    low_string = string.lower()
    return low_string in (item.lower() for item in list_to_search)
print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) #Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) #No matches
print(calls)
