from multiprocessing import Process

from Utilities import generate_big_ri
from Utilities import get_arrival_time
import time

global days
global hours
global minutes
global seconds

customer_ri = generate_big_ri(30000)


def customer_distribution():
    customer_arrives()
    print(get_timer())
    for t in customer_ri:
        time.sleep(get_arrival_time((180 / 7), t))
        customer_arrives()
        print(get_timer())


def customer_arrives():
    print('customer arrives..')


def timer():
    global days
    global hours
    global minutes
    global seconds
    seconds, hours, minutes, days = 0, 0, 0, 0
    while days < 1:
        time.sleep(1 / 60)
        seconds += 1
        if seconds == 60:
            seconds = 0
            minutes += 1
        if minutes == 60:
            minutes = 0
            hours += 1
        if hours == 24:
            hours = 0
            days += 1


def get_timer():
    return str(('d: ', days, 'h: ', hours, 'm: ', minutes, 's: ', seconds))




