from time import perf_counter
import numpy as np
import re

start = perf_counter()

file = 'input_03.txt'

with open(file, 'r') as f:
    # concatenate all the lines first
    mem = ''
    for line in f:
        mem += line.strip('\n')
    f.close()

# check pattern of the mul(xxx,yyy) type
mul_pattern = 'mul\([0-9]+,[0-9]+\)'
mul_pattern = re.compile(mul_pattern)

# check pattern of the number
num_pattern = '[0-9]+'
num_pattern = re.compile(num_pattern)

sum_product = 0

# find all occurences of mul_pattern in mem
found = mul_pattern.findall(mem)
for i in found:
    # for each mul(xxx,yyy), extract xxx and yyy as int64 and multiply them
    sum_product += np.prod([int(x) for x in num_pattern.findall(i)])

print(sum_product)

print(f'time: {perf_counter()-start:.3f} s')