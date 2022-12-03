from PseudoRandom import PseudoRandom as pr
import Mult_Congruence as mc
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
    ln = np.log(1-seed)
    return -ln/rate

