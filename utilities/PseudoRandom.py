import math
import statistics
from scipy.stats.distributions import chi2
from scipy import stats


class PseudoRandom:

    def __init__(self, ri):
        self.ri = ri

    def apply_mean_test(self):
        n = len(self.ri)
        m = statistics.mean(self.ri)
        z = 1.959964

        lim_in = (1 / 2) - (z * (1 / (math.sqrt(12 * n))))
        lim_sup = (1 / 2) + (z * (1 / (math.sqrt(12 * n))))

        if lim_in <= m <= lim_sup:
            return True
        else:
            return False

    def apply_variance_test(self):
        n = len(self.ri)
        x1 = chi2.ppf(0.025, n - 1)
        v = statistics.variance(self.ri)
        x2 = chi2.ppf(0.975, n - 1)

        lim_in = x1 / (12 * (n - 1))
        lim_sup = x2 / (12 * (n - 1))

        if lim_in <= v <= lim_sup:
            return True
        else:
            return False

    def verify_randomness(self):
        if self.apply_mean_test():
            if self.apply_variance_test():
                return True
            else:
                return False
        else:
            return False

    def apply_ks(self):
        n = len(self.ri)
        p = 1.36 / (math.pow(n, (1 / 2)))
        if (stats.kstest(self.ri, 'uniform', args=(0, 1))[0]) < p:
            return True
        else:
            return False

    def verify_uniformity(self):
        if self.apply_ks():
            return True
        else:
            return False

    def verify_ri(self):
        if self.verify_randomness() and self.verify_uniformity():
            return self.ri
        else:
            return False
