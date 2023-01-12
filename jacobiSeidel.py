from numpy import array, zeros, diag, diagflat, dot

def jacobiMethod(a, b, n, x = None):
    if x is None:
        x = zeros(len(a[0])) # if we dont have initial giess then we make it 0
                                                                                                                                                               
    D = diag(a) # take diagonal values from matrix
    R = a - diagflat(D) # by using this function from numpy library we remoe diagonals from matrix

    # print(D[0])
    # print(b[0])
    # print(R[0])
    # print(dot(R, x))
    l = len(x)
    # print((b[0] - dot(R[0],x[0]))/D[0])
    # iterate N times and every time remove result of x * matrix from augments                                                                                                                                                                        
    # for i in range(n):
    #     for j in range(l):
    #         # x[j] = (b[j] - dot(R,x))[j]/D[j]
    #         x = (b - dot(R,x))[j] / D[j]

    return x

matrix = array([[5, -1, 2], 
                [3, 8, -1],
                [1, 1, 4]], float)
augments = array([12, 1, 4])
x = array([0, 0, 0], float)
# print(matrix)
# print(augments)
# print("initial guess")
# print(x)
x = jacobiMethod(matrix, augments, 2, x)
print("result")
print(x)







