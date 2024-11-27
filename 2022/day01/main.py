totatm = 0
temp = 0
max = []

while(True):
    temp = input()

    if temp == "exit":
        print(max)
        print(max[0] + max[1] + max[2])
        break

    elif temp != "":
        totatm += int(temp)

    else:
        if len(max) < 3:
            max.append(totatm)
            max.sort()
            max.reverse()
            print(max)
        else:    
            for i in range(len(max)):
                if totatm > max[i]:
                    max[i] = totatm
                    break
        totatm = 0
        