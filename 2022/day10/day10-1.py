
regVals = [1]
reg = 1
while True:
    line = input()
    if line == "#":
        out = 0
        for i in range (20, 221, 40):
            print(regVals[i])
            out += i*regVals[i]
        print(out) 
        print(regVals) 
        break
    if line == "noop":
        regVals.append(reg) 
    else:
        regVals.append(reg) 
        regVals.append(reg)
        reg += int(line[5:])

       

