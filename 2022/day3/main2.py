# lowercase : ascii - 96
# uppercase : ascii - 38
sum = 0

def findLet():
    for i in group_one:
        for j in group_two:
            if i == j:
                for k in group_three:
                    if i == k:
                        return i

while (True):
    line = input()

    if line == "exit":
        print(sum)
        break

    group_one = list(line)
    group_two = list(input())
    group_three = list(input())
    let = findLet()

    if (let.islower()):
        sum += ord(let) - 96
    else:
        sum += ord(let) - 38