import time
import multiprocessing


def test(c, b):
    c = c
    while c > 0:
        c -= 1
        time.sleep(b)
        print('1')
    print(f'end: {b}')


if __name__ == '__main__':
    c1 = multiprocessing.Process(target=test, args=(100, 0.016))
    c2 = multiprocessing.Process(target=test, args=(100, 0.030))
    c1.start()
    c2.start()
