import utilities.PseudoRandom as pr
import utilities.Mult_Congruence as mc
import numpy as np


def define_chef_margin_error():
    return


def generate_big_ri(n):
    ri_verified = False
    ri = []
    while not ri_verified:
        ri = mc.get_ri(n)
        ri_verified = pr(ri).verify_ri()
    return ri


def generate_small_ri(n):
    return mc.get_ri(n)


def get_arrival_time(rate, seed):
    ln = np.log(1 - seed)
    return -ln / rate


def generate_Ni_min_max(min, max):
    m = max + 1
    rand = generate_small_ri(1)[0]
    return int(min + (m - min) * rand)


def generate_Customers_n():
    return generate_Ni_min_max(1, 5)


def generate_Tip():
    rand = generate_small_ri(1)[0]
    if rand < 0.5:
        return True
    else:
        return False


def generate_Share():
    rand = generate_small_ri(1)[0]
    if rand > 0.5:
        return True
    else:
        return False


def generate_custm_capacity():
    return generate_Ni_min_max(1, 4)


def generate_pay_mode():
    return generate_Ni_min_max(1, 3)


def generate_pay_type():
    return generate_Ni_min_max(1, 3)
