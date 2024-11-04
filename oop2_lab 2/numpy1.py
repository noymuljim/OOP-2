import numpy as np
numbers = np.array([2,3,4,5,11])
arr1_2D=np.array([[2,3,4],[4,5,7],[9,6,7]])
arr2_2D=np.array([[2,36,4],[7,6,6],[8,9,7]])

num2= np.arange(1,6)

numbers<=5
print(numbers)



print(arr1_2D.size)
print(arr1_2D.itemsize)
print(arr1_2D.min)
print(arr1_2D)

print(numbers.dtype)
print(numbers.ndim)
print(arr2_2D.shape)
print(type(numbers))

print(numbers.max)
print(numbers.sum)


num2=numbers.view()
print(num2)

num2=numbers.copy()
print(num2)


