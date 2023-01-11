import math 


def f(x):
    return x**10 - 1

def bisection(x0,x1,e):
    step = 1
    print('\n\nFunction: x*10 - 1 = 0')
    condition = True
    while condition:
        x2 = (x0 + x1)/2
        print('Iteration-%d, x2 = %0.3f and f(x2) = %0.3f' % (step, x2, f(x2)))
        if f(x0) * f(x2) < 0:
            x1 = x2
        else:
            x0 = x2
        
        step = step + 1
        condition = abs(f(x2)) > e

    print('\nFound Root is : %0.3f' % x2)

x0 = input('First guess: ')
x1 = input('Second guess: ')
# e = input('Tolerable Error: ')

x0 = float(x0)
x1 = float(x1)
e = 0.0001


if f(x0) * f(x1) > 0.0:
    print('Given guess values do not bracket the root.')
    print('Try Again with different guess values.')
else:
    bisection(x0,x1,e)

