from time import perf_counter
import re

start = perf_counter()

file = 'input_03.txt'

num = 0

# feed input grid into a list of strings (y lines, x chars)
test = []
with open(file) as f:
    for line in f:
        test.append(line.strip('\n'))
    f.close()

for l,line in enumerate(test):
    # find occurrences of '*'
    for x in re.finditer('\*',line):

        # make a box surrounding '*'
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

        # start finding patterns
        gears = []

        # find patterns on the same line (left and right of '*')
        for y in re.finditer(r'[0-9]+',line):
            if set(i for i in range(xmin, xmax)) & set(i for i in range(y.start(), y.end())):
                gears.append(y.group())

        # find patterns on the line above '*'
        if l!=0:
            for y in re.finditer(r'[0-9]+',test[l-1]):
                if set(i for i in range(xmin,xmax)) & set(i for i in range(y.start(),y.end())):
                    gears.append(y.group())

        # find patterns on the line below '*'
        if l!=139:
            for y in re.finditer(r'[0-9]+',test[l+1]):
                if set(i for i in range(xmin, xmax)) & set(i for i in range(y.start(), y.end())):
                    gears.append(y.group())

        # if not exactly 2 numbers are adjacent to '*', skip
        if len(gears)!=2:
            continue
        else:
            num += int(gears[0])*int(gears[1])

print(num)
print(f'time: {perf_counter()-start:.3f} s')