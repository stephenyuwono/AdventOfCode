from time import perf_counter
import numpy as np

start = perf_counter()

file = 'input_01.txt'

test = np.loadtxt(file, dtype='i8')

left  = np.unique(test[:,0],return_counts=True)
right = np.unique(test[:,1],return_counts=True)

left_set = set(left[0])
right_set = set(right[0])

left_right = left_set.intersection(right_set)

left_dict = dict(zip(left[0],left[1]))
right_dict = dict(zip(right[0],right[1]))

sum_times = 0
for i in left_right:
    sum_times += left_dict[i] * i * right_dict[i]

print(sum_times)

print(f'time: {perf_counter()-start:.3f} s')