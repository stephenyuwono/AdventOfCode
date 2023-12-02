import numpy as np

f = "input03.txt"

inpf = np.loadtxt(f,dtype=str)
inpf = inpf.reshape(int(len(inpf)/3),3)

def priority(x):
    if x in 'abcdefghijklmnopqrstuvwxyz':
        return ord(x)-96
    elif x in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        return ord(x)-38
    else:
        None

sum=0
for i in range(len(inpf)):
    y = str(''.join(set(inpf[i,0]) & set(inpf[i,1]) & set(inpf[i,2])))
    sum += priority(y)

print(sum)