import random
import math
N = 11
M = 3
K = 4

def init_random_list(list_size):
 list = []
 while list_size > 0:
  list.append(random.randint(-1, 1))
  list_size = list_size - 1
 
 return list

lst = init_random_list(N)
print("source array:", lst)

i = 0
j = len(lst)
while i < j:
 if lst[i] == 0:
  del lst[i]
  j -= 1
 else:
  i += 1
 print("modiffied array:", lst)
