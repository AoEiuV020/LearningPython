import queue
import time
from concurrent.futures import ThreadPoolExecutor


class BlockingExecutor:
    def __init__(self, thread_count, cache_size):
        if cache_size <= 0:
            raise ValueError('cache_size must > 0')
        self.finish = False
        self.executor = ThreadPoolExecutor(thread_count)
        self.queue = queue.Queue(maxsize=cache_size)
        for i in range(thread_count):
            self.executor.submit(self.call_function)

    def call_function(self):
        # finish之后queue中还有至少一个要处理，
        while not (self.finish and self.queue.empty()):
            try:
                (task, args) = self.queue.get(timeout=1)
            except queue.Empty:
                continue
            task(*args)

    def submit(self, task, *args):
        self.queue.put((task, args))

    def shutdown(self):
        self.finish = True
        self.executor.shutdown()


def increase_n(n, delay, x, r):
    time.sleep(delay)
    n[0] += x
    assert n[0] == r


n = [2]
executor = BlockingExecutor(2, 1)
executor.submit(increase_n, n, 0.3, 3, 9)  # thread 1
executor.submit(increase_n, n, 0.2, 4, 6)  # thread 2
executor.submit(increase_n, n, 0.4, 5, 20)  # thread 2
assert n[0] == 2
executor.submit(increase_n, n, 0.1, 6, 15)  # thread 1
assert n[0] == 6
executor.shutdown()
assert n[0] == 20
