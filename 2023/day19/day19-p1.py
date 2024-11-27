import re

def assess_part(xmas, workflows, start):
    curr = workflows[start]
    while True:
        for var, rule, dst in curr[0]:
            if rule(xmas[var]):
                if dst == 'A':
                    return sum(xmas.values())
                elif dst == 'R':
                    return 0
                else:
                    curr = workflows[dst]
                    break
        else:
            if curr[1] == 'A':
                return sum(xmas.values())
            elif curr[1] == 'R':
                return 0
            else:
                curr = workflows[curr[1]]

workflows = {}
with open("input.txt", "r") as f:
    for line in f:
        if line == '\n':
            break
        data = re.split("{|,", line.strip()[:-1])
        rules = []
        for elem in data[1:-1]:
            con = re.split("<|>|:", elem)
            rules.append((con[0],
                          (lambda x, n=int(con[1]): x < n) if '<' in elem else (lambda x, n=int(con[1]): x > n),
                          con[2]))
        workflows[data[0]] = (rules, data[-1])
    ans = 0
    for line in f: 
        xmas = {k: int(ch) for k, ch in zip(('x', 'm', 'a', 's'), re.findall(r'\d+', line))}
        ans += assess_part(xmas, workflows, 'in')
print(ans)