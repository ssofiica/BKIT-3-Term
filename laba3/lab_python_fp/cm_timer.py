from time import perf_counter, sleep
from contextlib import contextmanager

class cm_timer_1:

    def __init__(self):
        self.time_1 = None

    def __enter__(self):
        self.time_1 = perf_counter()

    def __exit__(self, exp_type, exp_value, traceback):
        print('time: {}'.format(perf_counter() - self.time_1))

@contextmanager
def cm_timer_2():
    n = perf_counter()
    yield
    print('time: {}'.format(perf_counter() - n))

def main6():
        with cm_timer_1():
            sleep(3.2)
        with cm_timer_2():
            sleep(3.2)
if __name__ == '__main__':
    main6()