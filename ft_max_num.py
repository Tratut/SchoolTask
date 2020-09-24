from ft_len_num import ft_len_num


def ft_max_num(x):
    kol = ft_len_num(x)
    mx = 0
    cop = x
    for i in range(kol):
        if cop % 10 > mx:
            mx = cop % 10
        cop //= 10
    return mx
