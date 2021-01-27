import queue
import time
from concurrent.futures import ThreadPoolExecutor

finish = False


def increase_n(n, blocking_queue):
    # finish之后queue中还有一个要处理，
    while not (finish and blocking_queue.empty()):
        # 反直觉，设置timeout情况是直接抛异常而不是返回空，block也一样，
        # 可能是考虑python很多情况空的后续处理会有未知异常，比如这里的解tuple,
        try:
            (delay, x, r) = blocking_queue.get(timeout=1)
        except queue.Empty as e:
            assert not e.args
            continue
        time.sleep(delay)
        n[0] += x
        assert n[0] == r


max_thread = 2
executor = ThreadPoolExecutor(max_thread)
n = [2]
blocking_queue = queue.Queue(maxsize=1)

# noinspection PyListCreation
futures = []
futures.append(executor.submit(increase_n, n, blocking_queue))
futures.append(executor.submit(increase_n, n, blocking_queue))
blocking_queue.put((0.3, 3, 9))  # thread 1
blocking_queue.put((0.2, 4, 6))  # thread 2
# 线程只有两个，但是queue最少也要能缓存一个，所以第三个put不会阻塞，
blocking_queue.put((0.4, 5, 20))  # thread 2
assert n[0] == 2
blocking_queue.put((0.1, 6, 15))  # thread 1
assert n[0] == 6
for t in futures:
    assert not t.done()
finish = True
executor.shutdown()
assert n[0] == 20
for t in futures:
    assert t.done()
