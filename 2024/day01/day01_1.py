from time import perf_counter
import numpy as np

start = perf_counter()

file = 'input_01.txt'

test = np.loadtxt(file, dtype='i8')

test[:,0] = np.sort(test[:,0])
test[:,1] = np.sort(test[:,1])

diff = np.abs(test[:,0] - test[:,1])

print(np.sum(diff))

print(f'time: {perf_counter()-start:.3f} s')