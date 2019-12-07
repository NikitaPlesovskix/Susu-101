# Дано вещественное число A. Вычислить f(A), если f(x) = 0 при x ≤ 0; f(x) = x2 − x при 0 < x < 1,
# в противном случае f(x) = x2 − sin(πx2).
import math
a = float(input("Введите число А "))
x = a

if x <= 0:
    fx = 0
    print("x <= 2; f(a) = ", fx)
elif 0 < x < 1:
    fx = x**2 - x
    print("0 < x < 1; f(a) = ", fx)
else:
    fx = math.pow(x, 2) - math.sin((math.pi * x**2))
    print("x >= 1; f(a) = ", fx)
