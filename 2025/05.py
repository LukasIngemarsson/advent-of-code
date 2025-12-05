import sys


def p1(lines):
    ranges = []
    q_idx = -1
    for i, line in enumerate(lines):
        if line == '':
            q_idx = i + 1
            break
        rng = tuple(map(int, line.split('-')))
        ranges.append(rng)
    assert q_idx != -1

    fresh = set()
    for line in lines[q_idx:]:
        q = int(line)
        for a, b in ranges:
            if a <= q <= b:
                fresh.add(q)
    ans = len(fresh)
    print(ans)


def p2(lines):
    ranges = []
    for line in lines:
        if line == '':
            break
        rng = tuple(map(int, line.split('-')))
        ranges.append(rng)

    ranges.sort()
    end = -1
    ans = 0
    for a, b in ranges:
        if b <= end:
            continue
        ans += b - max(a, end) + (end < a)
        end = b
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines)
    p2(lines)

