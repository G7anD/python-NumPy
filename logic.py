import numpy as np

# Return True if none of the elements of x is zero
x = np.array([1, 2, 3])
print(np.all(x))  # True

x = np.array([1, 0, 4])
print(np.all(x))  # False


# Return True if any of the elements of x is non-zero.
x = np.array([1, 0, 0])
print(np.any(x))  # True

x = np.array([0, 0, 0])
print(np.any(x))  # False

x = np.array([1, 0, np.nan, np.inf])
print(np.isfinite(x))  # [ True  True False False]

# Return True if x is infinity.
x = np.array([1, 0, np.nan, np.inf])
print(np.isinf(x))  # [False False False  True]

# Return True if x is not a number.
x = np.array([1, 0, np.nan, np.inf])
print(np.isnan(x))  # [False False  True False]

# Return True if x is complex number.
x = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])
print(np.iscomplex(x))  # [ True False False False False  True]

# Return True if x is real number.
x = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])
print(np.isreal(x))  # [False  True  True  True  True False]

# Return True if x is scalar number.
print(np.isscalar(3))  # True
print(np.isscalar([3]))  # False
print(np.isscalar(True))  # True

# simple logical operators.
print(np.logical_and([True, False], [False, False]))
# [False False]
print(np.logical_or([True, False, True], [True, False, False]))
# [ True False  True]
print(np.logical_xor([True, False, True], [True, False, False]))
# [False False  True]
print(np.logical_not([True, False, 0, 1]))
# [False  True  True False]

# Return True if args are equal.
print(np.allclose([3], [2.999999]))  # True
print(np.array_equal([3], [2.999999]))  # False

# other functions
x = np.array([4, 5])
y = np.array([2, 5])
print(np.greater(x, y))  # [ True False]
print(np.greater_equal(x, y))  # [ True  True]
print(np.less(x, y))  # [False False]
print(np.less_equal(x, y))  # [False  True]
