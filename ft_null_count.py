from ft_len_num import ft_len_num


def ft_null_count(x):
    kol = ft_len_num(x)
    cop = x
    count = 0
    for i in range(kol):
        if cop % 10 == 0:
            count += 1
    return count
