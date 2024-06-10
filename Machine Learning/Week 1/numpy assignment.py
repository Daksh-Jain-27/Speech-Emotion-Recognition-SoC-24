import numpy as np 
# arr = np.array([[1,2,4],[7,13,21]])
# print(arr)
# print("shape:",arr.shape)

# n_rows = 2
# n_columns = 3
# x = np.random.randn(n_rows,n_columns)
# print(x)

# ZERO_ARR = np.zeros((4,5,2))
# print(ZERO_ARR)

# ONE_ARR = np.ones((4,5,2))
# print(ONE_ARR)

# y = np.array([[1, 2, 3],[4, 5, 6]])
# y_transpose = y.reshape(3,2)
# print(y_transpose)
# y_flat = y.reshape(6,1)
# print(y_flat)
# print(y.flatten())

# y = np.array([[4],[7],[11]])
# assert y.shape == (3,1)
# print(y)
# a = np.random.randn(2,4)
# z = np.dot(a,y)
# # c = np.matmul(a,y)
# # assert z.shape == (2,1)
# print(z)
# # print(c) 

# x = np.array([4, 1, 5, 6, 11])
# y = x[1:4]
# print(y)
# z = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
# w = z[::2]
# print(w)

# arr_2d = np.array([[4, 5, 2],
#           [3, 7, 9],
#           [1, 4, 5],
#           [6, 6, 1]])
# sliced_arr_2d = arr_2d[:3,1:]
# print(sliced_arr_2d)s

# arr1 = np.array([1, 2, 3, 4])
# b = 1
# arr1+=b
# print(arr1)
# arr2 = np.array([[1, 2, 3],
#                  [4, 5, 6]])
# arr3 = np.array([[4],
#                  [5]])
# arr2*= arr3
# print(arr2)

# import time
# import numpy as np
# arr_nonvectorized = np.random.rand(1000, 1000)
# arr_vectorized = np.array(arr_nonvectorized)

# start_nv = time.time()

# for i in range(1000):
#     for j in range(1000):
#         arr_nonvectorized[i,j]*=3
# end_nv = time.time()
# print("Time taken in non-vectorized approach:", 1000*(end_nv-start_nv), "ms")

# print(arr_nonvectorized)

# start_v = time.time()
# arr_vectorized*= 3
# end_v = time.time()
# print("Time taken in vectorized approach:", 1000*(end_v-start_v), "ms")

# print(arr_vectorized)