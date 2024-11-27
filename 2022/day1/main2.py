totatm = 0
temp = 0
elfVals = []

while(True):
    temp = input()

    if temp == "exit":
        elfVals.sort()
        elfVals.reverse()
        print(elfVals[0] + elfVals[1] + elfVals[2])
        break
    elif temp != "":
        totatm += int(temp)
    else:
        elfVals.append(totatm)
        totatm = 0
        