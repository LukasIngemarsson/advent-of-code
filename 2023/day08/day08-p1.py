file = open("input.txt", "r")
instr, graph, start, end = tuple(file.readline().strip()), dict(), 'AAA', 'ZZZ'
file.readline() # skip new line
for line in file:
    elem, dst = line.replace('(', '').replace(',', '').replace(')', '').split(' = ')
    graph[elem] = tuple(dst.split())
curr, steps = start, 0
while True:
    for ch in instr:
        steps += 1
        curr = graph[curr][0] if ch == 'L' else graph[curr][1]
        if curr == end: break
    else: continue
    break
print(steps)