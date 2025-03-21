import re

path = []
dirs = {}

def getPath(s):
    if len(path) == 1 and s == "":
        return "/"

    t = ""
    for i in range(1,len(path)):
        t += "/" + path[i]

    if s != "":    
        t += "/" + s 
    return t      

while True:
    line = re.split(' ', input())
    if line[0] == "exit":
        #print(dirs)
        sums = {}
        keys = list(dirs.keys())
        for i in reversed(range(0,len(keys))):
            sum = 0
            vals = dirs.get(keys[i])
            for x in vals:
                if x.isnumeric():
                    sum += int(x)
                else:
                    sum += sums.get(x)
            sums[keys[i]] = sum

        #print(sums)

        output = 0
        for s in sums:
            if int(sums[s]) <= 100000:
                output += int(sums[s])        
        print(output)
        break

    if line[0] == "$":
        if line[1] == "cd":
            if line[2] == "/":
                path = ["/"]
            elif line[2] == "..":
                path.pop()
            else:
                path.append(line[2])

    else:
        key = getPath("")
        val = ""
        if line[0] == "dir":
            val = getPath(line[1])
        else:
            val = line[0]    

        if key in dirs:
            temp = dirs.get(key)
            temp.append(val)
            dirs[key] = temp
        else:
            dirs[key] = [val] 



