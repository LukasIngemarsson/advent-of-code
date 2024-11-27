import re

sum = 0

while True:
    line = input()

    if line == "exit":
        print(sum)
        break

    sections = re.split('-|,', line) # [a,b,c,d]
    
    if (int(sections[0]) <= int(sections[2]) and int(sections[1]) >= int(sections[3])) or (int(sections[2]) <= int(sections[0]) and int(sections[3]) >= int(sections[1])):
        sum += 1
