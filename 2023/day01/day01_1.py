import numpy as np

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
