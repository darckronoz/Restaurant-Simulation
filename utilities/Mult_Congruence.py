import random as r

g = 16
m = 2 ** g
global seed
k = r.randint(3, 17)
a = 8 * k + 3


def get_ri(n):
    global seed
    seed = r.randint(0, m)
    xi_list = fillXi(n)
    return fillRi(n, xi_list)


def calculateXi(x):
    return (a * x) % m


def calculateRi(x):
    return x / (m - 1)


def fillXi(n):
    xi_list = [int(calculateXi(seed))]
    for t in range(int(n)):
        xi_list.append(int(calculateXi(xi_list[t])))
    return xi_list


def truncate(number: float, max_decimals: int) -> float:
    int_part, dec_part = str(number).split(".")
    return float(".".join((int_part, dec_part[:max_decimals])))


def fillRi(n, xi_list):
    ri_list = []
    for t in range(int(n)):
        ri_list.append(truncate(calculateRi(xi_list[t]), 5))
    return ri_list
