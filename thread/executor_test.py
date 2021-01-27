import time
from concurrent.futures import ThreadPoolExecutor


def increase_n(n, delay, x, r):
    time.sleep(delay)
    n[0] += x
    assert n[0] == r


with ThreadPoolExecutor(max_workers=2) as executor:
    n = [2]
    # noinspection PyListCreation
    futures = []
    futures.append(executor.submit(increase_n, n, 0.3, 3, 9))
    futures.append(executor.submit(increase_n, n, 0.2, 4, 6))
    futures.append(executor.submit(increase_n, n, 0.4, 5, 14))
    assert n[0] == 2
    for t in futures:
        t.result()
for t in futures:
    assert t.done()
assert n[0] == 14
