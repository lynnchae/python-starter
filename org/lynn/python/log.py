import logging

logging.basicConfig(level=logging.INFO)
s = '0'
n = int(s)
assert isinstance(n, int), 'n is not a number'
logging.info('n = %d' % n)
print(10 / n)
