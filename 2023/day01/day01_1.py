from time import perf_counter
import numpy as np

start = perf_counter()

file = 'input_01.txt'

cal = []

with open(file) as f:
    for line in f:
        tmp = []
        for i in line:
            if i in '1234567890':
                tmp.append(i)
        tmp = tmp[0] + tmp[-1]
        cal.append(int(tmp))
    f.close()

print(np.sum(cal))
print(f'time: {perf_counter()-start:.3f} s')