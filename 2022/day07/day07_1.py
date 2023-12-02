f = "input07.txt"

def cmd_parser(x):
    return None

def size(x):
    return

cmd = []

with open(f,"r") as inpf:
    for i in inpf:
        i = i.strip().split()
        cmd.append(i)

    inpf.close()

# skip first line
cmd = cmd[1:]

cdup = []
cddn = []

for i in range(len(cmd)):
    if 'cd' in cmd[i]:
        if '..' in cmd[i]:
            cdup.append(i)
        else:
            cddn.append(i)

for i in range(len(cmd)):


root = {}
size = {}

