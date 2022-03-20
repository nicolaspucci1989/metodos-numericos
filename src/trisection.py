from numpy import sign


def trisection(a, b, f, e):
    if sign(f(a)) == sign(f(b)):
        raise Exception('Invalid input')

    i = 1
    while b - a >= e:
        if (i % 2) == 0:
            c = (2 * a + b) / 3
            d = (a + 2 * b) / 3
            fc = f(c)
            fd = f(d)
            if fc == 0:
                return c
            elif fd == 0:
                return d
            elif sign(f(a)) * sign(fc) < 0:
                b = c
            elif sign(fc) * sign(fd) < 0:
                a = c
                b = d
            else:
                a = d
        else:
            c = (a + b) / 2
            fc = f(c)
            if fc == 0:
                return c
            elif sign(fc) * sign(f(a)) < 0:
                b = c
            else:
                a = c
        i += 1

    return (a + b) / 2
