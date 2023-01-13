from numpy import array, zeros, diag, diagflat, dot
import numpy.linalg as al
import matplotlib.pyplot as plt
import copy 


def jacobiMethod(a, b, n, x = None):
    c = 1
    coun = []
    x1 = []
    x2 = []
    x3 = []
    if x is None:
        x = zeros(len(a[0])) # if we dont have initial giess then we make it 0
                                                                                                                                                               
    D = diag(a) # take diagonal values from matrix
    R = a - diagflat(D) # by using this function from numpy library we remoe diagonals from matrix

    # iterate N times and every time remove result of x * matrix from augments                                                                                                                                                                        
    for i in range(n):
        x = (b - dot(R,x)) / D
        x1.append(x[0])
        x2.append(x[1])
        x3.append(x[2])
        coun.append(c)
        c += 1
    plt.plot(coun, x1, label = "x")
    plt.plot(coun, x2, label = "y")
    plt.plot(coun, x3, label = "z")
    plt.xlabel('iteration')
    plt.ylabel('values')
    plt.legend()
    plt.show()

    return x

matrix = array([[10, 1, 1], 
                [2, 10, 1],
                [2, 2, 10]], float)
augments = array([12, 13, 14])
x = array([0, 0, 0], float)
print(matrix)
print(augments)
print("initial guess")
print(x)
x = jacobiMethod(matrix, augments, 25, x)
print("result")
print(x)







