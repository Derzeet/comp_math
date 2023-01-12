from numpy import array, zeros, fabs

def gaussJordanElimination(matrix, augments):
    n = len(matrix[0])
    l = len(augments)
    
    for i in range(l):
        if fabs(matrix[i, i]) == 0 : #check whether diagonal elements are zero 
            for j in range(i+1, n):
                if fabs(matrix[j, i]) > 0: # check if we can replace next some rows with row where diagonal == 0 
                    for k in range(i, n):
                        matrix[i, k], matrix[j, k] = matrix[j, k], matrix[i, k] # swaping rows 
                    augments[i], augments[j] = augments[j], augments[i] # swaping augments
                break
        pivot = matrix[i, i] # establishing pivor element
        for k in range(i, n):
            matrix[i, k] /= pivot # changing values of each row so pivot will equal to 1
        augments[i] /= pivot
        for j in range(l):
            if j == i or matrix[j, i] == 0: continue #starting elimination to gen identity matrix
            ratio = matrix[j, i]
            for k in range(i, n):
                matrix[j, k] -= ratio * matrix[i, k]
            augments[j] -= ratio*augments[i]
    return augments, matrix

matrix = array([[2, 1, 5, 1], 
                [1, 1, -3, 4]], float)
augments = array([5, -1], float)
print(matrix)
print("Augments: ")
print(augments)

augments, matrix = gaussJordanElimination(matrix, augments)
print("Transformed matrix:")
print(matrix)
print("Solution: ")
print(augments)
