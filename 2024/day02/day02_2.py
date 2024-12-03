from time import perf_counter
import numpy as np

start = perf_counter()

file = 'input_02.txt'

with open(file, 'r') as f:
    safe_count = 0
    for l,line in enumerate(f):
        x = np.array(line.split(),dtype='i8')

        diff = x[1:] - x[:-1]

        if (np.all(diff >= 1) and np.all(diff <= 3)) or (np.all(diff >= -3) and np.all(diff <= -1)):
            safe_count += 1
        else:
            # brute force popping one element at a time
            x = x.tolist()
            for i in range(len(x)):
                tmp = x.copy()
                tmp.pop(i)
                tmp = np.array(tmp,dtype='i8')
                diff = tmp[1:] - tmp[:-1]
                if (np.all(diff >= 1) and np.all(diff <= 3)) or (np.all(diff >= -3) and np.all(diff <= -1)):
                    safe_count += 1
                    break

    print(safe_count)

    f.close()



print(f'time: {perf_counter()-start:.3f} s')