from ft_rev_num import ft_rev_num


def ft_mirror_num(x):
    if ft_rev_num(x) == x:
        return True
    else:
        return False
