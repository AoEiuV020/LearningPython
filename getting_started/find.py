assert 'asdf'.find('d') == 'asdf'.index('d')
assert -1 == 'asdf'.find('dd')
try:
    'asdf'.index('dd')
    raise Exception
except ValueError as e:
    assert e.args[0] == 'substring not found'
assert 'hello'.find('l') == 2
assert 'hello'.rfind('l') == 3
