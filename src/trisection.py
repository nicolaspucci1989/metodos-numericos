from numpy import sign, log2, abs, ceil


def my_print(i, a, b):
    print('{:<8} {:<20} {:<20}'.format(i, a, b))


def trisection(a, b, f, e):
    if sign(f(a)) == sign(f(b)):
        raise Exception('Invalid input')
    elif e > b - a:
        raise Exception('e must be smaller than the difference between a and b')

    steps = int(ceil(log2(abs(b - a) / e))) + 1
    i = 1
    print('\n')
    my_print('Index', 'a', 'b')
    while b - a >= e or i <= steps:
        if (i % 2) == 0:
            c = (2 * a + b) / 3
            d = (a + 2 * b) / 3
            fc = f(c)
            fd = f(d)
            sign_fc = sign(fc)
            if fc == 0:
                return c
            elif fd == 0:
                return d
            elif sign(f(a)) * sign_fc < 0:
                b = c
            elif sign_fc * sign(fd) < 0:
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

        my_print(i, a, b)
        i += 1

    my_print(i, a, b)
    return a
