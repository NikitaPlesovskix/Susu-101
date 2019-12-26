import random

N = 2  # строк
M = 3  # столбцов


def get_row(column):
    col = []
    for i in range(0, column):
        col.append(random.randint(-9, 9))

    return col


def get_matrix(row, column):
    matrix = []
    for i in range(0, row):
        matrix.append(get_row(column))

    return matrix


def print_matrix(matrix):
    i = 0
    while i < len(matrix):
        j = 0
        row = matrix[i]
        while j < len(row):
            column = row[j]
            print(column, end=' ')
            j += 1

        print()
        i += 1


A = get_matrix(N, M)
print("Исходная матрица:")
print_matrix(A)

new_row = []

i = 0
while i < len(A):
    j = 0

    count_row_negative = 0
    while j < len(A[i]):
        is_negative = A[i][j] < 0

        if is_negative:
            count_row_negative += 1

        if len(new_row) <= j:
            new_row.append(1 if is_negative else 0)
        else:
            new_row[j] += 1 if is_negative else 0

        j += 1

    A[i].append(count_row_negative)
    i += 1

A.append(new_row)

print("Модифицированная матрица:")
print_matrix(A)
