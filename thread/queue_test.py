import queue

maxsize = 3
q = queue.Queue(maxsize=maxsize)
assert q.empty()
for i in range(maxsize):
    q.put(i)
    assert q.qsize() == i + 1
assert q.full()
assert not q.empty()
try:
    # 默认阻塞，
    q.put(8, timeout=0.1)
except queue.Full as e:
    assert not len(e.args)
try:
    q.put(8, block=False)
except queue.Full as e:
    assert not len(e.args)
for i in range(maxsize):
    assert q.get() == i
assert q.empty()
assert not q.full()
try:
    q.get(timeout=0.1)
except queue.Empty as e:
    assert not len(e.args)
try:
    q.get(block=False)
except queue.Empty as e:
    assert not len(e.args)
