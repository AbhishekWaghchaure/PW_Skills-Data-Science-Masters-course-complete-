# first_array=[1,2,3]
# second_array = [2,3,4,5]
# common_array = [element for element in first_array if element in second_array]
# print(common_array)
## output_array =[0, 1, 1]
# from collections import Counter
# one_array = [1,2,3,4]
# two_array = [2,3,3,4,4,5,5,6]
# array_counter = Counter(one_array)
# ## output = [0,1,2,2]
# element_count = [array_counter[element]for element in two_array]

# print(element_count)   


first_array = [1,2,3]
second_array = [2,3,2,2,2] 

print(first_array[2])
first_array.append([4,5])
print(first_array)
first_array[3] = 9
print(first_array)
first_array.remove(9)
print(first_array)
first_array.remove(first_array[1])
print(first_array)
print(second_array[1:4])

import numpy as np
np_second_array = np.array (second_array)
print(type(second_array))
print(type(np_second_array))
