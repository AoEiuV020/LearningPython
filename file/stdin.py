import sys

sys.stdin = open('in', 'r')
line = input()
assert len(line) == 4
assert line == '1234'
line = input()
assert len(line) == 3
assert line == '123'
line = input()
assert len(line) == 2
assert line == '12'
line = input()
assert len(line) == 1
assert line == '1'
try:
    line = input()
except EOFError as e:
    assert e.args[0] == 'EOF when reading a line'
else:
    raise Exception
