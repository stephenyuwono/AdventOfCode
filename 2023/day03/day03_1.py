from time import perf_counter
import re

start = perf_counter()

file = 'input_03.txt'

pattern = set('0123456789.')

num = 0

# feed input grid into a list of strings (y lines, x chars)
test = []
with open(file) as f:
    for line in f:
        test.append(line.strip('\n'))
    f.close()

for l,line in enumerate(test):
    # find occurrences of numbers
    for x in re.finditer(r'[0-9]+',line):

        xmin = max(0,x.start()-1)
        ymin = max(0,l-1)

        if x.end()==140:
            xmax = None
        else:
            xmax = x.end()+1
        if l==139:
            ymax = None
        else:
            ymax = l+1

        # create box surrounding number
        box = line[xmin:xmax]
        if l!=0:
            box = test[ymin][xmin:xmax] + box
        if l!=139:
            box +=test[ymax][xmin:xmax]

        # remove number from box, can be skipped
        # re.sub(r'[0-9]+','',box)

        # if there is a character in the box that is not in the pattern, add
        if len(set(box)&pattern) < len(set(box)):
            num += int(x.group())

print(num)
print(f'time: {perf_counter()-start:.3f} s')