import numpy as np
matrix =[
    [4,8,9],
    [1,1,2],
    [3,6,8],
    ]
matrix2=[
    [7,4,8],
    [6,9,5],
    [33,99,77]
]
array1= np.array(matrix)
array2 = np.array(matrix2)
print(array1.__invert__())
