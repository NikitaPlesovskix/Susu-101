# Вводятся положительные числа. Определить сумму чисел, делящихся на положительное число B нацело.
# При вводе отрицательного числа закончить работу.

import random
B = random.randint(1,10)
print("B = " + str(B))
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0


for i in range(M):
    arr[i] = input()

for i in range(M):
    if int(arr[i]) < 0:
        print("END")
        break
    elif int(arr[i]) % B == 0:
        a += int(arr[i])
print("Конечный результат " + str(a))
