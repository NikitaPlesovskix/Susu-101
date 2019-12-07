# Дан одномерный массив числовых значений, насчитывающий N элементов.
# Поменять местами элементы, стоящие на чётных и нечётных местах: A[1] ↔ A[2]; A[3] ↔ A[4] ...

import random
import sys
n = 25
a = [random.randint(0, 100) for i in range(0,n)]
print(a)

if (len(a) % 2 == 1):
    end = n
else:
    end = n-1


for i in range(0, end-1, 2):
    a[i], a[i + 1] = a[i + 1], a[i]
print(a)
