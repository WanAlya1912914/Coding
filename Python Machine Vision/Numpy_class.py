import numpy as np

array1 = np.array([1,2,3,4,5])
array2 = np.array([[1,2,3,4,5],[1,2,3,4,5]])
array3 = np.array([[1,2,3],[4,5,6],[7,8,9]])
array5 = np.array([[1,2,3],[4,5,6],[7,8,9]])

# print(array1)
# print(array2)
# print(array3)
# print(array3[1])
# print(array3[1,0])
# print(array3[:,2])
# print(array3[1:3,1:3])

# array3[1,0] = 100
# print(array3)

array4 = array2*100
# print(array4)

# print(array3*array5)
# print(array3.shape)
# print(np.mean(array3))
# print(np.mean(array3,0)) #mean for every row

array6 = array3.reshape(1,9)
# print(array6)

print(array2.transpose())



