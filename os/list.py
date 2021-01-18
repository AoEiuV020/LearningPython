import glob
import os

print(__file__)
# listdir是不包括路径的文件名，
assert any(map(lambda x: x in __file__, os.listdir()))
assert os.listdir('.') == os.listdir()
assert glob.glob("*.py") == list(filter(lambda x: x.endswith(".py"), os.listdir()))
