
regVals = []
reg = 1
while True:
    line = input()
    if line == "#":
        for i in range (0, 240, 40):
            out = []
            for j in range (0, 40):
                if abs(regVals[i+j]-j) < 2:
                    out.append('#')
                else:
                    out.append('.')

            print("".join(out))

        break
    if line == "noop":
        regVals.append(reg) 
    else:
        regVals.append(reg) 
        regVals.append(reg)
        reg += int(line[5:])

