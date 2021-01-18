fin = open('in', 'r')
line = fin.readline()
assert len(line) == 5
assert line == '1234\n'
line = fin.readline()
assert len(line) == 4
assert line == '123\n'
line = fin.readline()
assert len(line) == 3
assert line == '12\n'
line = fin.readline()
assert len(line) == 2
assert line == '1\n'
line = fin.readline()
# 反直觉，最后一行不会读出换行符\n,
assert len(line) == 0
assert line == ''
# 继续读也全都是空字符串，
line = fin.readline()
assert len(line) == 0
assert line == ''
