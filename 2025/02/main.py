import sys


def p1(lines):
    assert len(lines) == 1
    ranges = [tuple(map(int, rstr.split('-'))) for rstr in lines[0].split(',')]

    ans = 0
    for a, b in ranges:
        for x in range(a, b + 1):
            xstr = str(x)

            if len(xstr) % 2 != 0:
                continue

            mid = len(xstr) // 2
            if xstr[:mid] == xstr[mid:]:
                ans += x
    print(ans)


def p2(lines):
    assert len(lines) == 1
    ranges = [tuple(map(int, rstr.split('-'))) for rstr in lines[0].split(',')]

    ans = 0
    for a, b in ranges:
        for x in range(a, b + 1):
            xstr = str(x)

            for seqlen in range(1, len(xstr) // 2 + 1):
                if len(xstr) % seqlen != 0:
                    continue

                seqs = {xstr[i:i+seqlen] for i in range(0, len(xstr), seqlen)}

                if len(seqs) == 1:
                    ans += x
                    break
    print(ans)


if __name__ == "__main__":
    with sys.stdin as f:
        lines = [l.strip() for l in f.readlines()]

    p1(lines)
    p2(lines)
