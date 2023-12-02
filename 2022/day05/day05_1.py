f = "input05.txt"

def mover(x,inv):
    x = x.split()
    move = int(x[1])
    posi = int(x[3])-1
    posf = int(x[5])-1

    for i in range(move):
        # pop item one by one from the end
        inv[posf].append(inv[posi].pop(-1))

    return inv

def loader(temp):
    # initialize empty list
    inv = [[] for _ in range(9)]
    for i in temp[:-1]:
        for j in range(9):
            x = i[1+j*4]
            # skip empty column
            if x==' ':
                continue
            # lazy regex
            elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                inv[j].append(x)
    # could have used different looping direction
    for i in inv:
        i = i.reverse()

    return inv

with open(f,"r") as inpf:
    inpl = []
    for i in inpf:
        inpl.append(i)

    inpf.close()

temp = []
instruction = []
idx=0

for i in range(len(inpl)):
    # add lines to instruction after idx>0
    if idx>0:
        instruction.append(inpl[i])
    # empty line trigger switch from inventory to instruction
    elif inpl[i]=='\n':
        idx=1
        continue
    # add lines to inventory while idx==0
    elif idx==0:
        temp.append(inpl[i])

inv = loader(temp)

for i in instruction:
    inv = mover(i, inv)

for i in inv:
    print(i[-1])