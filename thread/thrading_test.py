import threading
import time


class TestThread(threading.Thread):
    def __init__(self, n, delay, x, r):
        threading.Thread.__init__(self)
        self.n = n
        self.delay = delay
        self.x = x
        self.r = r

    def run(self):
        time.sleep(self.delay)
        self.n[0] += self.x
        assert self.n[0] == self.r


n = [2]
TestThread(n, 0.3, 3, 9).start()
TestThread(n, 0.2, 4, 6).start()
TestThread(n, 0.4, 5, 14).start()
for t in threading.enumerate():
    if t != threading.current_thread():
        t.join()

assert n[0] == 14
