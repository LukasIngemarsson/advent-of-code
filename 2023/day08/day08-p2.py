import math
file = open("input.txt", "r")
instr, graph = tuple(file.readline().strip()), dict()
file.readline() # skip new line
for line in file:
    elem, dst = line.replace('(', '').replace(',', '').replace(')', '').split(' = ')
    graph[elem] = tuple(dst.split())
starts, elem_steps = [k for k in list(graph.keys()) if k.endswith('A')], dict()
for start in starts:
    curr, steps = start, 0
    while True:
        for ch in instr:
            steps += 1
            curr = graph[curr][0] if ch == 'L' else graph[curr][1]
            if curr.endswith('Z'): 
                elem_steps[start] = steps
                break
        else: continue
        break
print(math.lcm(*elem_steps.values())) # least common multiple