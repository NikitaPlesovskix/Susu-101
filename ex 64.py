# Суммировать вводимые числа, среди которых нет нулевых. При вводе нуля обеспечить вывод текущего значения суммы. При вводе числа 99999 закончить работу.
import random
M = random.randint(1,4)
arr = [random.randint(1,10) for i in range(M)]
a = 0
for i in range(M):
    arr[i] = input()
for i in range(M):
    if int(arr[i]) == 99999:
        print("END")
        break
    elif int(arr[i]) == 0:
       print(a)
    elif int(arr[i]) > 0:
        a += int(arr[i])
print("Конечный результат " + str(a))
