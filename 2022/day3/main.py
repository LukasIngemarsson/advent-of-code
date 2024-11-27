# lowercase : ascii - 96
# uppercase : ascii - 38
sum = 0

def findLet():
    for i in comp_one:
        for j in comp_two:
            if i == j:
                return i        

while (True):
    line = input()

    if line == "exit":
        print(sum)
        break

    comp_one = list(line[:len(line)//2])
    comp_two = list(line[len(line)//2:])
    let = findLet()

    if (let.islower()):
        sum += ord(let) - 96
    else:
        sum += ord(let) - 38

                


