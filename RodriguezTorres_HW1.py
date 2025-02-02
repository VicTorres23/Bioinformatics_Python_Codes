#!/usr/bin/env python
# coding: utf-8

# In[125]:


import pandas as pd

matA = [[1, 3, 7], [5, 1, 2], [0, 1, 2]]
matB = [[2, 0, 1], [4, 1 ,3], [3, 5, 2]]
matC = [[1,3,7], [5,1,2]]
matD = [[1], [5], [1]]


def MxM(matrix1, matrix2):
    matAdf = pd.DataFrame(matrix1)
    matBdf = pd.DataFrame(matrix2)

    if (matAdf.shape[1] != matBdf.shape[0]):
        print("Dimensions are incompatible. No solution available.")
        return
    
    result = pd.DataFrame(0, range(matAdf.shape[0]), range(matBdf.shape[1]))
    for i in range(matAdf.shape[0]):
        for j in range(matBdf.shape[1]):
            result.iloc[i,j] = sum(matAdf.iloc[i,:]*matBdf.iloc[:,j])
    print(result)

MxM(matA,matB)
MxM(matA,matC)
MxM(matA,matD)


# In[128]:


import numpy as np
import time

matA = np.array([[1, 3, 7], [5, 1, 2], [0, 1, 2]])
matB = np.array([[2, 0, 1], [4, 1 ,3], [3, 5, 2]])
matC = np.array([[1,3,7], [5,1,2]])
matD = np.array([[1], [5], [1]])

start_time = time.perf_counter()
MxM(matA,matB)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Total time with my function:" + str(elapsed_time))

start_time = time.perf_counter()
result = np.dot(matA,matB)
end_time = time.perf_counter()
elapsed_time = end_time - start_time
print("Total time for the numpy function:" + str(elapsed_time))

