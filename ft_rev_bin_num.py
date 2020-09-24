from ft_len_num import ft_len_num


def ft_rev_bin_num(x):
    cop = x
    b = 0
    for i in range(ft_len_num(x)):
        b += cop % 10 * 2 ** i
        cop //= 10
        i += 1
    return b
