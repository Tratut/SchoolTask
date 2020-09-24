from ft_len_num import ft_len_num


def ft_min_num(x):
    kol = ft_len_num(x)
    mn = 10
    cop = x
    for i in range(kol):
        if cop % 10 < mn:
            mn = cop % 10
        cop //= 10
    return mn
