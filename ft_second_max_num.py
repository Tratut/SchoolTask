from ft_len_num import ft_len_num


def ft_second_max_num(x):
    kol = ft_len_num(x)
    mx_1 = 0
    mx_2 = mx_1
    cop = x
    for i in range(kol):
        if cop % 10 > mx_1:
            mx_2 = mx_1
            mx_1 = cop % 10
        if mx_1 > cop % 10 > mx_2:
            mx_2 = cop % 10
        cop //= 10
    return mx_2
