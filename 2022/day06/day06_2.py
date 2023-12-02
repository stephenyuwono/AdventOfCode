f = "input06.txt"

with open(f,"r") as inpf:
    test = inpf.readline()
    inpf.close()

for i in range(14,len(test)):
    x = set(test[i-14:i])
    if len(x)==14:
        print('Bingo! Start marker is ',i)
        break