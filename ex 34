# Дан одномерный массив числовых значений, насчитывающий N элементов. Поменять местами первую и вторую половины массива.
import random

N = int(input("Введите количество элементов массива "))
a = [random.randint(0, 100) for i in range(0, N)]
print(a)

for i in range(len(a) // 2):
    a[i], a[i + len(a) // 2] = a[i + len(a) // 2], a[i]
print(a)
