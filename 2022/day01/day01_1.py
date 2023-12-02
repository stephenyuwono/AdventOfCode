f = "input01.txt"

max = 0
cur = 0

with open(f,"r") as inpf:
    for i in inpf:
        if i=='\n':
            cur = 0
        else:
            cur += int(i)
            if cur > max:
                max = cur

    inpf.close()

    print(max)
