# Задача 30: Заполните массив элементами арифметической
# прогрессии. Её первый элемент, разность и количество
# элементов нужно ввести с клавиатуры. Формула для
# получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

a1= int(input('Введите первый элемент: a1 = '))
d = int(input('Введите разность: d = '))
n = int(input('Введите количество элементов: n = '))
def Arith_Progress(pr1, D, N):
    pr = []
    for i in range(1, N + 1):
        pr. append(pr1 + (i-1) * d)
    return pr
print(Arith_Progress(a1, d, n))
