def ft_oct_num(x):
    cop = x
    b = 0
    i = 0

    while cop > 0:
        b = (cop % 8) * 10 ** i + b
        cop //= 8
        i += 1
    return b
