from time import perf_counter
import numpy as np
import re

start = perf_counter()

file = 'input_05.txt'

file_len = len([1 for _ in open(file)])
file_list = []
grrr = []

maps = {}

with open(file) as f:

    for l,line in enumerate(f):
        # print(l)
        # print(re.search('[a-zA-Z]',line))
        if re.search('[a-zA-Z]',line) != None:
            tmp = [l]
        if line == '\n':
            tmp.append(l)
            grrr.append(tmp)
            tmp = []
        if l==file_len-1:
            tmp.append(file_len)
            grrr.append(tmp)
        file_list.append(line.strip('\n'))

    grrr = np.array(grrr).astype('i8')

# print(grrr)

for i in grrr:
    if i[0]==0:
        tmp = np.array(file_list[i[0]].split(': ')[1].split(' '),dtype='i8')
        maps[file_list[i[0]].split(': ')[0]] = tmp
    else:
        tmp = []
        for x in file_list[i[0]+1:i[1]]:
            tmp.append([int(y) for y in x.split(' ')])
        maps[file_list[i[0]].strip(':')] = np.array(tmp,dtype='i8')

def mapper(x,xtoy):
    y = x
    for i in xtoy:
        tmp = x - i[1]
        if 0< tmp < i[2]:
            y = i[0] + (x - i[1])
            break
        else:
            continue
    return y

keys = [i for i in maps.keys()]

result = np.zeros(len(maps[keys[0]]),dtype='i8')

for i,seed in enumerate(maps[keys[0]]):
    tmp = seed
    for x in keys[1:]:
        tmp = mapper(tmp,maps[x])
    result[i] = tmp

print(np.min(result))

print(f'time: {perf_counter()-start:.3f} s')