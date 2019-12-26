import random

N = 4
M = 5
L = 2

def get_row(column):
  col = []
  for i in range(0, column):
    col.append(random.randint(0, 9))
    
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
print("Исходная матрица")
print_matrix(A)

i = 0
while i < len(A):
  j = 0
  max_element = max(A[i])
  while j < len(A[i]):
    A[i][j] /= max_element
    A[i][j] = round(A[i][j], 1)
    j += 1
    
  i += 1
  
print("Модифицированная матрица")
print_matrix(A)
