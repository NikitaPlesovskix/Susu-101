def create_array(array):
 positive= 0
 negative= 0
 for element in array:
  if element <0:
   negative -= element
  if element >0:
   positive -= element
 if positive>negative:
  array.append (positive - negative)
  
 if positive<negative:
  array.append (negative-positive)
  
 return array

array = [2,1,0,-1,3,4,-2,4]
print (create_array(array))
