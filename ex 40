import random
import math
N = 11
M = 3
K = 4

def init_random_list(list_size):
 list = []
 while list_size > 0:
  list.append(random.randint(-3, 3))
  list_size = list_size - 1
 
 return list
 
lst = init_random_list(N)
print("source array:", lst)

i = 0
j = len(lst)
while i < j:
  if lst[i]< 0:
   lst.insert(i+1, lst[i]* lst[i])
   j += 1
  i += 1 
  print ("modified array:", lst)
