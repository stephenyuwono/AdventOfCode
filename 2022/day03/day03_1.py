f = "input03.txt"

def priority(x):
    if x in 'abcdefghijklmnopqrstuvwxyz':
        return ord(x)-96
    elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return ord(x)-38
    else:
        None

sum=0
with open(f,"r") as inpf:
    for i in inpf:
        i = i.strip()
        xl = len(i)
        x1=i[0:int(xl/2)]
        x2=i[int(xl/2):xl]

        y = str(''.join(set(x1) & set(x2)))
        # print(y)

        sum+=priority(y)

    inpf.close()

print(sum)


