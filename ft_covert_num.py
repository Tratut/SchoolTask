def ft_covert_num(x, base):
    cop = x
    b = 0
    i = 0

    while cop > 0:
        b = (cop % base) * 10 ** i + b
        cop //= base
        i += 1
    return b
