from ft_sqrt import ft_sqrt


def ft_str(x, y, z):
    p = (x + y + z) / 2
    S = p * (p - x) * (p - y) * (p - z)
    return ft_sqrt(S)


print(ft_str(3, 4, 5))
