from ft_len_num import ft_len_num


def ft_sum_num(x):
    kol = ft_len_num(x)
    sm = 0
    cop = x
    for i in range(kol):
        sm += cop % 10
        cop //= 10
    return sm
