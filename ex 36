import random
import math

N = 11
M = 3
K = 5

def init_random_list(list_size):
 list = []
 while list_size > 0:
  list.append(random.randint(1, 100))
  list_size = list_size - 1
 return list
lst = init_random_list(N)
print("source array:", lst)
lst[K:K+M] = init_random_list(M)
print("modified array:", lst)
