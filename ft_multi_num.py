from ft_len_num import ft_len_num


def ft_multi_num(x):
    kol = ft_len_num(x)
    sm = 1
    cop = x
    for i in range(kol):
        sm *= cop % 10
        cop //= 10
    return sm
