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


def checker(x,y):
    '''
    check if we find
        M.M    S.S    M.S    S.M
        .A. or .A. or .A. or .A.
        S.S    M.M    M.S    S.M
    :param x: 'A' position in line
    :param y: line number
    :return: True if match found, else False
    '''

    MM = re.compile('M.M')
    SS = re.compile('S.S')
    MS = re.compile('M.S')
    SM = re.compile('S.M')

    return (MM.fullmatch(tmp[y-1],x-1,x+2) and SS.fullmatch(tmp[y+1],x-1,x+2)) or \
           (SS.fullmatch(tmp[y-1],x-1,x+2) and MM.fullmatch(tmp[y+1],x-1,x+2)) or \
           (MS.fullmatch(tmp[y-1],x-1,x+2) and MS.fullmatch(tmp[y+1],x-1,x+2)) or \
           (SM.fullmatch(tmp[y-1],x-1,x+2) and SM.fullmatch(tmp[y+1],x-1,x+2))

x_mas_count = 0

for i,line in enumerate(tmp):
    # skip first and last line
    if i==0 or i==len(tmp)-1:
        continue
    else:
        x = [x.start() for x in re.finditer('A', line)]
        for j in x:
            # skip first and last column
            if j==0 or j==len(line)-1:
                continue
            elif checker(j,i):
                x_mas_count += 1

print(x_mas_count)

print(f'time: {perf_counter()-start:.3f} s')