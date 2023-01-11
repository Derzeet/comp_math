import math
import matplotlib.pyplot as plt

def f(x):
    return x**3 - 5*x - 9

def falsePosition(x0,x1,e):
    step = 1
    print('(FP)Function: 10x-1=0 ')
    condition = True
    x_axis = []
    y_axis = []
    while condition:
        x2 = x0 - (x1-x0) * f(x0)/( f(x1) - f(x0) )
        print('Iteration-%d, x2 = %0.6f and f(x2) = %0.6f' % (step, x2, f(x2)))

        if (f(x0) * f(x2)) < 0:
            x1 = x2
        else:
            x0 = x2
        x_axis.append(x2)
        y_axis.append(step)
        step = step + 1
        condition = abs(f(x2)) > e

    plt.plot(y_axis, x_axis)
    plt.xlabel("Iteration")
    plt.ylabel("Value")
    print('\nRequired root is: %0.8f' % x2)
    plt.show()


x0 = input('First guess: ')
x1 = input('Second guess: ')
e = 0.000001

x0 = float(x0)
x1 = float(x1)
e = float(e)

if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    falsePosition(x0,x1,e)