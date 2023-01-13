from numpy import array, zeros, diag, diagflat, dot
import matplotlib.pyplot as plt

def seidel(a, b, x):
    n = len(a)
    c = 1
    coun = []
    x1 = []
    x2 = []
    x3 = []
    for j in range(0, n):
        d = b[j]
        for i in range(0, n):
            if(j != i):
                d-=a[j][i] * x[i]
            x[j] = d / a[j][j]
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
    print(c)
    return x



matrix = array([[10, 1, 1], 
                [2, 10, 1],
                [2, 2, 10]], float)
augments = array([12, 13, 14])
x = array([0, 0, 0], float)
print(matrix)
print(augments)
x = seidel(matrix, augments, x)
print("result")
print(x)







