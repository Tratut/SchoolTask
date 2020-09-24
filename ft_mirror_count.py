from ft_rev_num import ft_rev_num


def ft_mirror_count(x):
    kol = 0
    for i in range(x):
        if ft_rev_num(i) == i > 10:
            kol += 1
    return kol


print(ft_mirror_count(23))