from testutils import assert_raises

src = """
def valid_func():
    pass

yield 2
"""

try:
    compile(src, 'test.py', 'exec')
except SyntaxError as ex:
    assert ex.lineno == 5
else:
    raise AssertionError("Must throw syntax error")

with assert_raises(SyntaxError):
    compile('0xX', 'test.py', 'exec')
