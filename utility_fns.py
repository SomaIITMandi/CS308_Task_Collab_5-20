#CS308 : Task - colaboration1
#Some utility functions
#Ocotober 5, 2020 

import numpy as np

#min-max function
def max_min(data):
  l = data[0]
  u = data[0]
  for num in data:
    if num< l:
      l = num
    elif num> u:
        u = num
  return l, u

#add two arrays

#average an array


#Input array
a = [0, 10, 15, 40, -5, 42, 17, 28, 75]

#output
min, max = np.array(max_min(a))

print('Maximum value = {:.2f}, minimum value = {:.2f}'.format(max, min))
# computing the length of the array
n = len(a);
print('length of the array', n);
# computing the sum of the array
sum1 = sum(a);
print('sum of the array', sum1);
