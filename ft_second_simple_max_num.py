from ft_len_num import ft_len_num
from ft_second_max_num import ft_second_max_num


def ft_second_simple_max_num(x):
    kol = ft_len_num(x)
    cop = x
    num = 0
    f_num = cop % 10
    if kol == 1:
        return -1
    for i in range(kol):
        if cop % 10 == f_num:
            num += 1
        else:
            return ft_second_max_num(x)
        cop //= 10
    if num == kol:
        return -1
