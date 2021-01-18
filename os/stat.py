import os

files = os.listdir()
times = list(map(lambda x: os.stat(x).st_mtime, files))
lastPy = files[times.index(max(times))]
print(lastPy)
