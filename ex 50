def check_array(array):
 count_3=0
 sum_even=0.0
 count_even=0
 for element in array:
  if element % 3 ==0:
   count_3 += 1
  if element % 2 == 0:
   sum_even += element
   count_even += 1
 mean =0
 if count_even:
  mean= sum_even/count_even
  
 array.insert(0, count_3)
 array.append(mean)
 return array

array=[2,1,7,6,5,68,29,3]
print (check_array(array))
