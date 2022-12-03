import math
import statistics
from scipy.stats.distributions import chi2
from scipy import stats
from read_ri import get_ri

ri = get_ri()


def apply_mean_test():
    n = len(ri)
    m = statistics.mean(ri)
    z = 1.959964

    lim_in = (1 / 2) - (z * (1 / (math.sqrt(12 * n))))
    lim_sup = (1 / 2) + (z * (1 / (math.sqrt(12 * n))))

    if lim_in <= m <= lim_sup:
        return True
    else:
        return False


def apply_variance_test():
    n = len(ri)
    x1 = chi2.ppf(0.025, n - 1)
    v = statistics.variance(ri)
    x2 = chi2.ppf(0.975, n - 1)

    lim_in = x1 / (12 * (n - 1))
    lim_sup = x2 / (12 * (n - 1))

    if lim_in <= v <= lim_sup:
        return True
    else:
        return False


def verify_randomness():
    if apply_mean_test():
        if apply_variance_test():
            return True
        else:
            return False
    else:
        return False


print('randomness: ', verify_randomness())


def apply_ks():
    n = len(ri)
    p = 1.36 / (math.pow(n, (1 / 2)))
    if (stats.kstest(ri, 'uniform', args=(0, 1))[0]) < p:
        return True
    else:
        return False


def verify_uniformity():
    if apply_ks():
        return True
    else:
        return False


print('uniformity: ', verify_uniformity())
