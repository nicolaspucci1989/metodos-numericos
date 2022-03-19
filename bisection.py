from numpy import sign


def linear_function(x):
    return 2 * x + 1  # solution -0.5


def polynomial(x):
    return x ** 3 + 4 * x ** 2 - 10  # real solution 1.3652


def bisection(a, b, f, e):
    c = 0
    while b - a >= e:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif (sign(f(c)) * sign(f(a))) < 0:
            b = c
        else:
            a = c

    return c


linear_function_result = bisection(-1, 1, linear_function, 0.1)
print('Linear function', linear_function_result)

polynomial_result = bisection(-2, 2, polynomial, 0.1)
print('Polynomial: ', polynomial_result)
