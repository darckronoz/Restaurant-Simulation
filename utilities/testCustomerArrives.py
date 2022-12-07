import ctypes
import multiprocessing
import sys

from Utilities import generate_big_ri
from Utilities import get_arrival_time
import time

days = multiprocessing.Value(ctypes.c_int, 0)
hours = multiprocessing.Value(ctypes.c_int, 0)
#minutes = multiprocessing.Value(ctypes.c_int, 0)
#seconds = multiprocessing.Value(ctypes.c_int, 0)

customer_ri = generate_big_ri(30000)


def customer_distribution():
    customer_counter = 0
    t = multiprocessing.Process(target=timer)
    t.start()
    time.sleep(1)
    customer_arrives()
    for time_arrive in customer_ri:
        x = get_arrival_time((3/7), time_arrive)
        customer_counter += 1
        time.sleep(x/60)
        customer_arrives()
        print(customer_counter)
        if not t.is_alive():
            sys.exit(0)


def customer_arrives():
    print('customer arrives..')


def timer():
    global seconds, hours, minutes, days
    while days.value < 1:
        time.sleep(1)
        hours.value += 1
        if hours.value == 24:
            hours.value = 0
            days.value += 1
        print(('d: ', days.value, 'h: ', hours.value))


def get_timer():
    return str(('d: ', days.value, 'h: ', hours.value, 'm: ', minutes.value, 's: ', seconds.value))


if __name__ == '__main__':
    c = multiprocessing.Process(target=customer_distribution)
    c.start()
