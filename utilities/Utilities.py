from utilities.PseudoRandom import PseudoRandom as pr
import utilities.Mult_Congruence as mc
import matplotlib.pyplot as plt
from matplotlib import style
import numpy as np
import pandas as pd


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
    print(seed)
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


def generate_cheff_error():
    n = generate_Ni_min_max(5, 10)
    return n / 100


def calculate_tip(total_mesa):
    n = generate_Ni_min_max(5, 15)
    return total_mesa * (n / 100)


def calculate_plate_preparation(margin):
    n = generate_small_ri(1)[0]
    if n <= margin:
        return False
    else:
        return True


def generate_cheff_graph(c1, c2, c3):
    data = {'cheff 1:': c1, 'cheff 2:': c2, 'cheff 3:': c3}
    style.use('dark_background')
    plt.figure(figsize=(4, 4))
    plt.bar(list(data.keys()), list(data.values()), color='purple', width=0.4)
    plt.title('eficiencia cocineros')
    plt.show()


def best_seller_plate(entry, strong, dessert):
    lol = [f'Entrada mas vendida: {entry}', f'Plato Fuerte mas vendido: {strong}', f'Postre mas vendido: {dessert}']
    return lol


def best_score_plate(d):
    scores = list(d.values())
    plates = list(d.keys())
    lol = [f'Mejor Entrada: {plates[0]}, {scores[0]}', f'Mejor Plato Fuerte: {plates[1]}, {scores[1]}',
           f'Mejor Postre: {plates[2]}, {scores[2]}']
    return lol


def best_score_plate_graph(d):
    data = d
    style.use('dark_background')
    plt.figure(figsize=(4, 4))
    plt.bar(list(data.keys()), list(data.values()), color='purple', width=0.4)
    plt.title('eficiencia cocineros')
    plt.show()


def best_daily_waiter(waiter, score):
    return f'Mejor mesero: {waiter}, con {score} puntos!'


def profit_restaurant(value):
    return f'Gannacias totales: {value}'


def common_payment_mode(mode):
    return f'Modalidad de pago mas común: {mode}'
