import _thread
import time


def increase_n(n, delay, x, r):
    time.sleep(delay)
    n[0] += x
    assert n[0] == r
    print(n[0])


n = [2]
_thread.start_new_thread(increase_n, (n, 0.3, 3, 9))
_thread.start_new_thread(increase_n, (n, 0.2, 4, 6))
_thread.start_new_thread(increase_n, (n, 0.4, 5, 14))
time.sleep(1)
assert n[0] == 14
