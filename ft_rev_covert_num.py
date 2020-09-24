from ft_len_num import ft_len_num


def ft_rev_covert_num(x, base):
    cop = x
    b = 0
    for i in range(ft_len_num(x)):
        b += cop % 10 * base ** i
        cop //= 10
        i += 1
    return b
