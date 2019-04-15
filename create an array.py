import numpy as np
# Create an array of zeros
a = np.zeros((3,4))
# Create an array of ones
b = np.ones((2,3,4),dtype=np.int16)
# Create an array of evenly
d = np.arange(10,25,5)
# spaced values (step value)
c = np.linspace(0,2,9)
# Create an array of evenly
# spaced values (number of samples)
e = np.full((2,2),7)
# Create a constant array
f = np.eye(2)
# Create a 2X2 identity matrix
g = np.random.random((2,2))
# Create an array with random values
h = np.empty((3,2))
# Create an empty array

print(a,b,c,d,e,f,g,h,sep="\n\n")
'''[[ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]
 [ 0.  0.  0.  0.]]

[[[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]

 [[1 1 1 1]
  [1 1 1 1]
  [1 1 1 1]]]

[ 0.    0.25  0.5   0.75  1.    1.25  1.5   1.75  2.  ]

[10 15 20]

[[7 7]
 [7 7]]

[[ 1.  0.]
 [ 0.  1.]]

[[ 0.96427982  0.11239701]
 [ 0.4103786   0.0930024 ]]

[[  6.91613054e-310   1.97619223e-316]
 [  3.77476654e-096   1.05191680e-153]
 [  6.03095097e-154   4.56340418e-072]]'''
