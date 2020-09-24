def rever(x):
    a1 = x % 10
    a2 = x // 10 % 10
    a3 = x // 100
    return a1 * 100 + a2 * 10 + a3


print(rever(321))