from time import perf_counter

start = perf_counter()

file = 'input_02.txt'

id = 0

# dict of max allowed number of colored stones
std = {'red':12,'green':13,'blue':14}

with open(file) as f:
    for l,line in enumerate(f):

        # get the list of games after ': '
        games = line.split(': ')[1]

        # games as list separated by '; '
        games = [x.split(', ') for x in games.strip('\n').split('; ')]

        # add or no add?
        add = True

        for game in games:
            for rgb in game:
                # separate stone no. and color
                num = int(rgb.split(' ')[0])
                col = rgb.split(' ')[1]

                # check against std
                if num > std[col]:
                    add = False
                    break
                else:
                    continue

            # break as soon as game is impossible
            if not add:
                break

        if add: id += l+1

print(id)
print(f'time: {perf_counter()-start:.3f} s')