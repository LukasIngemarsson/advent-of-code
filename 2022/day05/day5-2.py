import re    

stacks = []
stacks.append(['Q','H','C','T','N','S','V','B'])
stacks.append(['G','B','D','W'])
stacks.append(['B', 'Q', 'S', 'T', 'R','W','F'])
stacks.append(['N','D','J','Z','S','W','G','L'])
stacks.append(['F','V','D','P','M'])
stacks.append(['J','W','F'])
stacks.append(['V','J','B','Q','N','L'])
stacks.append(['N','S','Q','J','C','R','T','G'])
stacks.append(['M','D','W','C','Q','S','J'])

#stacks = [['N', 'Z'], ['D', 'C', 'M'], ['P']]

while True:
    line = input()
    if (line == "exit"):
        output = ""
        for x in stacks:
            output += x.pop(0)
        print(output)
        break
    comms = re.split(' ', line) # index 1,3,5 have the numbers.
    comms = [int(comms[1]), int(comms[3]), int(comms[5])]
    counter = 0
    while counter < comms[0]:
        stacks[comms[2]-1].insert(counter, stacks[comms[1]-1].pop(0))
        counter += 1  
