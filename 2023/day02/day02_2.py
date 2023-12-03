from time import perf_counter
import numpy as np

start = perf_counter()

file = 'input_02.txt'

id = 0

with open(file) as f:
    for l,line in enumerate(f):

        # dict of current min number of colored stones
        power = {'red':0,'green':0,'blue':0}

        # get the list of games after ': '
        games = line.split(': ')[1]

        # games as list separated by '; '
        games = [x.split(', ') for x in games.strip('\n').split('; ')]

        for game in games:
            for rgb in game:
                # separate stone no. and color
                num = int(rgb.split(' ')[0])
                col = rgb.split(' ')[1]

                # check against power, update
                if num > power[col]:
                    power[col] = num
                else:
                    continue

        id += np.prod(list(power.values()))

print(id)
print(f'time: {perf_counter()-start:.3f} s')