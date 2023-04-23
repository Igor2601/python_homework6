# Задача 32: Определить индексы элементов массива (списка),
# значения которых принадлежат заданному диапазону (т.е. не
# меньше заданного минимума и не больше заданного
# максимума)
a = [int(i) for i in input('Введите элементы массива: ').split()]
minimum = int(input('Введите минимум: '))
maximum = int(input('Введите максимум: '))
def Index_Def(array, min_num, max_num):
    for i in range(len(array)):
        if min_num <= array[i] <= max_num:
            print (i, end = ', ')
Index_Def(a, minimum, maximum) 

