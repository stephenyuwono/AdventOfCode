f = "input01.txt"

max1 = 0
max2 = 0
max3 = 0
cur = 0

with open(f,"r") as inpf:
    for i in inpf:
        if i=='\n':
            cur = 0
        else:
            cur += int(i)
            if cur > max1:
                max3 = max2
                max2 = max1
                max1 = cur
            elif cur > max2:
                max3 = max2
                max2 = cur
            elif cur > max3:
                max3 = cur
            else:
                None

    inpf.close()

    print(max1,max2,max3)
    print(max1+max2+max3)

