from numpy import sign


def trisection(a, b, f, e):
    if sign(f(a)) == sign(f(b)):
        raise Exception('Invalid input')

    i = 1
    while b - a >= e:
        if (i % 2) == 0:
            c = (2 * a + b) / 3
            d = (a + 2 * b) / 3
            if f(c) == 0:
                return c
            elif f(d) == 0:
                return d
            elif sign(f(a)) * sign(f(c)) < 0:
                b = c
            elif sign(f(c)) * sign(f(d)) < 0:
                a = c
                b = d
            else:
                a = d
        else:
            c = (a + b) / 2
            if f(c) == 0:
                return c
            elif sign(f(c)) * sign(f(a)) < 0:
                b = c
            else:
                a = c
        i += 1

    return (a + b) / 2
