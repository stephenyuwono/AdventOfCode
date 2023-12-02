f = "input04.txt"

def ovl(r1,r2):
    # fill with 1s from 0 to r1[0]-1 and r1[1]-1, do OR
    a = ((1 << (r1[0] - 1)) - 1) ^ ((1 << (r1[1])) - 1)
    # fill with 1s from 0 to r2[0]-1 and r2[1]-1, do OR
    b = ((1 << (r2[0] - 1)) - 1) ^ ((1 << (r2[1])) - 1)

    ovlrange = min((bin(a).count("1"),bin(b).count("1")))

    if (bin(a&b).count("1")) == ovlrange:
        return 1
    else:
        return 0

sum = 0
with open(f,"r") as inpf:
    for i in inpf:
        # process text
        i = i.strip().split(',')
        r1 = i[0].split('-')
        r2 = i[1].split('-')
        r1 = [int(i) for i in r1]
        r2 = [int(i) for i in r2]

        # call ovl function
        sum += ovl(r1,r2)

print(sum)


