from ft_len_num import ft_len_num


def ft_rev_num(x):
    kol = ft_len_num(x)
    razryad = kol
    out = 0
    cop = x
    for i in range(kol):
        out += (cop % 10) * 10 ** razryad
        cop //= 10
        razryad -= 1
    return out // 10
