f = "input02.txt"

op = {"A":1, "B":2, "C":3}
me = {"X":0, "Y":3, "Z":6}

def score(ops,mes):
    if mes==0:
        if ops==1:
            return 3
        else:
            return ops-1
    elif mes==3:
        return ops+3
    else:
        if ops==3:
            return 7
        else:
            return ops+7


sum = 0
with open(f,"r") as inpf:
    for i in inpf:
        i = i.split()
        sum += score(op[i[0]],me[i[1]])
        # print(i,op[i[0]],me[i[1]],score(op[i[0]],me[i[1]]),sum)
    inpf.close()

print(sum)
