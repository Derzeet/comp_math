from numpy import array, zeros, diag, diagflat, dot
import numpy.linalg as al
import copy 


def jacobiMethod(a, b, n, x = None):
    if x is None:
        x = zeros(len(a[0])) # if we dont have initial giess then we make it 0
                                                                                                                                                               
    D = diag(a) # take diagonal values from matrix
    R = a - diagflat(D) # by using this function from numpy library we remoe diagonals from matrix

    # iterate N times and every time remove result of x * matrix from augments                                                                                                                                                                        
    for i in range(n):
        x = (b - dot(R,x)) / D
    return x

matrix = array([[5, -1, 1], 
                [2, 4, 0],
                [1, 1, 5]], float)
augments = array([10, 12, -1])
x = array([2, 3, 0])
print(matrix)
print(augments)
print("initial guess")
print(x)
x = jacobiMethod(matrix, augments, 25, x)
print("result")
print(x)







