import numpy as np
import re

file = 'input_01.txt'

cal = 0

calmap = [
    'one',
    'two',
    'three',
    'four',
    'five',
    'six',
    'seven',
    'eight',
    'nine'
    ]

with open(file) as f:
    for yy,line in enumerate(f):
        tmp = []
        idx = []

        # parse forward
        for i in line:
            if i in '1234567890':
                tmp.append(i)
                idx.append(line.index(i))
                break #once found

        # parse backward
        for i in line[::-1]:
            if i in '1234567890':
                tmp.append(i)
                idx.append(len(line)-1-line[::-1].index(i))
                break #once found

        # for part 2
        for ix in calmap:
            for pattern in re.finditer(ix,line):
                tmp.append(str(calmap.index(ix)+1))
                idx.append(pattern.start())

        # merge first and last digit and convert to int
        cal += int(tmp[np.argmin(idx)] + tmp[np.argmax(idx)])

    f.close()

print(cal)
