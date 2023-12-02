f = "input06.txt"

with open(f,"r") as inpf:
    test = inpf.readline()
    inpf.close()

for i in range(4,len(test)):
    x = set(test[i-4:i])
    if len(x)==4:
        print('Bingo! Start marker is ',i)
        break