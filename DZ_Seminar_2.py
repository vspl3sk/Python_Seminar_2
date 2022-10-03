from os import system
system('cls')

# 1. Напишите программу, которая принимает на вход
# вещественное число и показывает сумму его цифр.

# Пример:
# - 6782 -> 23
# - 0,56 -> 11

# float_number = input('Введите вещественное число: ')
# sum = 0
# for i in float_number:
#     if i != '.':
#         sum += int(i)
# print(sum)

# 2. Напишите программу, которая принимает на вход
# число N и выдает набор произведений чисел от 1 до N.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] (1, 1*2, 1*2*3, 1*2*3*4)

# n = int(input('Введите N: '))
# factorial = 1
# for i in range(1, n+1):
#     factorial *= i
#     print(factorial, end=' ')

# 3. Задайте список из n чисел последовательности (1+1/n)^n
# и выведите на экран их сумму.

# n = int(input('Введите число: ')) 
# def sequence(n):
#     return[round((1 + 1 / x)**x, 2) for x in range (1, n + 1)]       
# print(sequence(n))
# print(round(sum(sequence(n))))

# 4. Задайте список из N элементов, заполненных числами
# из промежутка [-N, N] (например, [-3, -2, 1, 0, 1, 2, 3].
# Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.

# from random import randint

# with open('Python_Seminar_2/file.txt', 'w') as data:
#     data.write('0\n')
#     data.write('1\n')
#     data.write('5\n')
#     data.write('8\n')
#     data.write('10\n')

# def get_numbers(n):
#     return [randint(-n/2, n) for i in range(-n, n + 1)]

# def get_data_from_file(path):
#     data = open(path, 'r')
#     dlist = [int(line.strip()) for line in data]
#     data.close()
#     return dlist

# def get_mult(numbers, datalist):
#     mult = 1
#     for i in datalist:
#         mult *= numbers[i]
#     return mult

# path = 'Python_Seminar_2/file.txt'
# n = 10 
# datalist = get_data_from_file(path)
# numbers = get_numbers(n)

# print(numbers)
# print(datalist)
# print(get_mult(numbers, datalist))

# 5 Реализуйте алгоритм перемешивания списка.

import random

def get_list(n, lft, rght):
    return [random.randint(lft, rght) for i in range(n)]

def shuffle_list(lst):
    return random.shuffle(lst)

n = 10
lft = -20
rght = 50

mylist = get_list(n, lft, rght)
print(mylist)
shuffle_list(mylist)
print(mylist)