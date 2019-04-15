import numpy as np
a = np.array([1, 2, 3])
print(a, "\n")

# a simple matrix elements are float
b = np.array([(1.5, 2, 3), (4, 5, 6)], dtype=float)
print(b, "\n")

m = np.zeros((3, 3))  # 3x3 matrix
print(m, "\n")

c = np.array([[(1.5,2,3), (4,5,6)], [(3,2,1), (4,5,6)]],dtype = float)
print(c)
'''[[[ 1.5  2.   3. ]
  [ 4.   5.   6. ]]

 [[ 3.   2.   1. ]
  [ 4.   5.   6. ]]]'''
# it Returns two 3x4 matrices which the elements were one
print(np.ones((2,3,4),dtype=np.int16))
'''[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]'''

print(np.arange(10,25,5)) # start stop step, [10 15 20]
