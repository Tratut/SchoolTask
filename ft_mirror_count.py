from ft_rev_num import ft_rev_num


def ft_mirror_count(x):
    kol = 0
    for i in range(1, x):
        if ft_rev_num(i) == i:
            kol += 1
    return kol
