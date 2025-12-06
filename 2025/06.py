import sys


def p1(lines):
    ops = lines.pop().split()
    problems = [[] for _ in range(len(ops))]
    for line in lines:
        nums = list(map(int, line.split()))
        for i, n in enumerate(nums):
            problems[i].append(n)
    
    ans = 0
    for op, nums in zip(ops, problems):
        if op == "*":
            res = 1
            for n in nums:
                res *= n
        else:
            res = sum(nums)
        ans += res
    print(ans)


def p2(lines):
    ROWS = len(lines) - 1
    COLS = len(lines[0])

    ops = lines.pop().split()
    problems = [[] for _ in range(len(ops))]
    p_idx = 0
    for c in range(COLS):
        nstr = ""
        for r in range(ROWS):
            if lines[r][c] != ' ':
                nstr += lines[r][c]
        if nstr == "":
            p_idx += 1
            continue
        problems[p_idx].append(int(nstr))
    print(problems) 

    ans = 0
    for op, nums in zip(ops, problems):
        if op == "*":
            res = 1
            for n in nums:
                res *= n
        else:
            res = sum(nums)
        ans += res
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    p2(lines)
