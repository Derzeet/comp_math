from numpy import array, zeros

def gaussElimination(matrix, augments):
    n = len(augments)
    x = zeros(n, float)
    # Elimination -> 
    for i in range(n-1): # map form start to end of the length of the matrix 
        for j in range(i+1,n): # map next rows and columns 
            if matrix[j, i]==0:continue
            ratio = matrix[i, i]/matrix[j, i]  #Calculate tha factor which will be used to get eliminate row
            for k in range(i, n):
                matrix[j, k] = matrix[i, k] - (ratio * matrix[j, k])
            augments[j] = augments[i] - (ratio * augments[j])

    # Back-substitution
    x[n-1] = augments[n-1]/matrix[n-1,n-1]
    for i in range (n-2, -1, -1):
        sum_ax = 0
        for j in range(i+1, n):
            sum_ax += matrix[i, j] * x[j]
        x[i] = (augments[i]-sum_ax)/matrix[i, i]
    
    return augments, matrix, x



matrix = array([[5, 1, 1, 1], 
                [1, 7, 1, 1], 
                [1, 1, 6, 1],
                [1, 1, 1, 4]], float)
augments = array([4, 11, -5, -6], float)

augments, matrix, x = gaussElimination(matrix, augments)

print(matrix)
print("Solution: ")
print(x)


