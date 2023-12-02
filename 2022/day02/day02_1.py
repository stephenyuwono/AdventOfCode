import numpy as np

f = "input02.txt"

op = {"A":1, "B":2, "C":3}
me = {"X":1, "Y":2, "Z":3}

# Scoring table, row = op, column = me
score = np.array(
    [[3,6,0],
     [0,3,6],
     [6,0,3]]
)

# add RPS score to each column
for i in range(3):
    score[:,i]+=i+1

sum = 0
with open(f,"r") as inpf:
    for i in inpf:
        i = i.split()
        sum += score[op[i[0]]-1,me[i[1]]-1]
    inpf.close()

print(sum)
