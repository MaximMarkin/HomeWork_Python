#1. В проекте, где вы решаете домашние задания, создайте модуль 'module_1_4.py'
# и напишите весь код в нём.
#2. Организуйте программу:

#Создайте переменную my_string и присвойте ей значение строки с произвольным текстом (функция input()).
#Вывести количество символов введённого текста

# Работа с методами строк:
#Используя методы строк, выполните следующие действия:

#Выведите строку my_string в верхнем регистре.
#Выведите строку my_string в нижнем регистре.
#Измените строку my_string, удалив все пробелы.
#Выведите первый символ строки my_string.
#Выведите последний символ строки my_string.

my_string = input('Введите название университета: ')
#print(len(my_string))
#print(type(my_string))
print(my_string, '- отличный выбор!')


print(my_string.upper())
print(my_string.lower())
print(my_string.replace(' ','#'))
print(my_string[0])
print(my_string[-1])