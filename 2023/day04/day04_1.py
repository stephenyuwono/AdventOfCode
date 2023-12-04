from time import perf_counter
import re

start = perf_counter()

file = 'input_04.txt'

result = 0

with open(file) as f:
    for line in f:
        x = line.strip('\n').split(': ')[1]
        win, own = x.split(' | ')
        win = set([x.group() for x in re.finditer(r'[0-9]+',win)])
        own = set([x.group() for x in re.finditer(r'[0-9]+',own)])

        power=len(win&own)-1
        if power<0:
            continue
        else:
            result += 2**power

print(result)
print(f'time: {perf_counter()-start:.3f} s')