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

# get ends of "do()" and starts of "don't()" occurences
# I hate apostrophes
do_match   = [i.end() for i in re.finditer('do\(\)',mem)]
dont_match = [i.start() for i in re.finditer('don\'t\(\)',mem)]

current_pos = 0
sum_product = 0
# iterate over don'ts, start with mem[0:dont_match[0]]
for dont in dont_match:

    # if the current don't() is still before the current position, skip
    if dont < current_pos:
        continue

    # find and process all mul(xxx,yyy) between current position and the next don't()
    found = mul_pattern.findall(mem[current_pos:dont])
    for i in found:
        sum_product += np.prod([int(x) for x in num_pattern.findall(i)])

    # check do occurences
    for ido,do in enumerate(do_match):
        # find the next do() after the current don't(), update current position
        if do > dont:
            current_pos = do
            break

        # if we iterate over all do() and none is greater than don't(), we're done
        elif ido == len(do_match)-1:
            print(sum_product)

            print(f'time: {perf_counter() - start:.3f} s')
            exit(0)

# just in case the last do() is greater than the last don't(), process the last chunk
found = mul_pattern.findall(mem[current_pos:])
for i in found:
    sum_product += np.prod([int(x) for x in num_pattern.findall(i)])
print(sum_product)

print(f'time: {perf_counter()-start:.3f} s')