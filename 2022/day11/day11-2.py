import re

monkeys = {}

def updateVal(list_item):
    key = list(monkeys.keys())[-1]
    monkeys[key].append(list_item)

while len(monkeys) < 8:
    while True:
        line = input()
        if line == "":
            break
        elif line.startswith("Monkey"):
            monkeys[int(line[7:8])] = []
        elif line.startswith("  Starting items"):
            splitLine = re.split(": |, ", line)
            items = []
            for i in range(1, len(splitLine)):
                items.append(int(splitLine[i]))
            updateVal(items)
        elif line.startswith("  Operation"):
            op = line.replace("  Operation: new = old ", "").split(" ")
            updateVal(op)
        elif line.startswith("  Test"):
            updateVal(int(line[20:]))
        elif line.startswith("    If true"):
            updateVal(int(line[29:]))    
        else:
            updateVal(int(line[30:]))
else:
    round = 0
    inspections = [0,0,0,0,0,0,0,0]
    common_denominator = 1
    for m in range(0, len(monkeys)):
        common_denominator *= monkeys[m][2]
    while round < 10000:
        for i in range(0, len(monkeys)):
            # mItems = monkeys[i][0]
            # mOp = monkeys[i][1]
            # mTest = monkeys[i][2]
            # mTrue = monkeys[i][3]
            # mFalse = monkeys[i][4]
            while monkeys[i][0]:
                inspections[i] += 1
                item = monkeys[i][0].pop(0)
                num = 0
                if monkeys[i][1][1] == "old":
                        num = item
                else:
                    num = int(monkeys[i][1][1])
                if monkeys[i][1][0] == "*":
                    item *= num
                else:
                    item += num
                item %= common_denominator   
                if item % monkeys[i][2] == 0:
                    monkeys[monkeys[i][3]][0].append(item)
                else:
                    monkeys[monkeys[i][4]][0].append(item)
        round += 1  
    inspections.sort()
    print(inspections)
    print(inspections[-1]*inspections[-2])
