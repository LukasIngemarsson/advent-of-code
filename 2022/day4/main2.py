import re

sum = 0

def checkOverlap():
    for j in list1:
            for k in list2:
                if j == k:
                    global sum 
                    sum += 1
                    return


while True:
    line = input()

    if line == "exit":
        print(sum)
        break

    sections = re.split('-|,', line)
    sections = [int(i) for i in sections]

    list1 = []
    list2 = []    
    
    for x in range(sections[0], sections[1] + 1):
        list1.append(x)
    for y in range(sections[2], sections[3] + 1):
        list2.append(y)

    checkOverlap()
    
