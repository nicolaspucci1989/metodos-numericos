from numpy import sign


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
