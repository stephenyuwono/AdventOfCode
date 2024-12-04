from time import perf_counter
import numpy as np
import re

start = perf_counter()

file = 'input_04.txt'

with open(file, 'r') as f:
    tmp = []
    for line in f:
        tmp.append(line.strip('\n'))
    f.close()

# check forward and backward match
xmas = re.compile('XMAS')
samx = re.compile('SAMX')

counts = 0

# check horizontal match
for i in tmp:
    counts += len(xmas.findall(i))
    counts += len(samx.findall(i))

# check vertical match
for i in range(len(tmp[0])):
    tmp2 = ''.join([tmp[x][i] for x in range(len(tmp))])
    counts += len(xmas.findall(tmp2))
    counts += len(samx.findall(tmp2))

for i in range(len(tmp)):
    # check antidiagonal match from 0,0
    x = np.zeros((i+1,2),dtype='i8')
    x[:,0] = np.arange(i+1,dtype='i8')
    x[:,1] = np.arange(i+1,dtype='i8')[::-1]
    tmp2 = ''.join([tmp[j[0]][j[1]] for j in x])
    counts += len(xmas.findall(tmp2))
    counts += len(samx.findall(tmp2))

    # check antidiagonal match from end,end but skip the (0,end)->(end,0) line
    if i < len(tmp)-1:
        x = (len(tmp)-1) - x
        print('diag from end',x)
        tmp2 = ''.join([tmp[j[0]][j[1]] for j in x])
        print(tmp2)
        counts += len(xmas.findall(tmp2))
        counts += len(samx.findall(tmp2))

    # check diagonal match from 0,end
    x[:,0] = np.arange(i+1,dtype='i8')
    x[:,1] = (len(tmp)-1-i) + np.arange(i+1,dtype='i8')
    print('antidiag from 0,end',x)
    tmp2 = ''.join([tmp[j[0]][j[1]] for j in x])
    print(tmp2)
    counts += len(xmas.findall(tmp2))
    counts += len(samx.findall(tmp2))

    # check diagonal match from end,0 but skip the (0,0)->(end,end) line
    if i < len(tmp)-1:
        x = x[:,[1,0]]
        tmp2 = ''.join([tmp[j[0]][j[1]] for j in x])
        print(tmp2)
        counts += len(xmas.findall(tmp2))
        counts += len(samx.findall(tmp2))


print(counts)

print(f'time: {perf_counter()-start:.3f} s')