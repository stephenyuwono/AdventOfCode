from time import perf_counter
import numpy as np
import re

start = perf_counter()

file = 'input_04.txt'

result = np.ones(np.sum([1 for _ in open(file)]),dtype='f8')

with open(file) as f:
    for l,line in enumerate(f):
        x = line.strip('\n').split(': ')[1]
        win, own = x.split(' | ')
        win = set([x.group() for x in re.finditer(r'[0-9]+',win)])
        own = set([x.group() for x in re.finditer(r'[0-9]+',own)])

        power = len(win & own)

        result[l+1:l+1+power] += result[l]

print(np.sum(result))
print(f'time: {perf_counter()-start:.3f} s')