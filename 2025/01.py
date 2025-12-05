import sys


def p1(lines):
    DIAL_MIN = 0
    DIAL_MAX = 100

    dial = 50
    ans = 0
    for line in lines:
        dir_, turns = line[0], int(line[1:])

        if dir_ == "R":
            dial = (dial + turns) % DIAL_MAX
        else:
            dial -= turns
            while dial < DIAL_MIN:
                dial += DIAL_MAX
        if dial == DIAL_MIN:
            ans += 1
    print(ans)


def p2(lines):
    DIAL_MIN = 0
    DIAL_MAX = 100

    dial = 50
    ans = 0
    for line in lines:
        dir_, turns = line[0], int(line[1:])

        if dir_ == "R":
            ans += (dial + turns) // DIAL_MAX
            dial = (dial + turns) % DIAL_MAX
        else:
            if dial == DIAL_MIN:
                ans -= 1
            dial -= turns
            while dial < DIAL_MIN:
                dial += DIAL_MAX
                ans += 1
            if dial == DIAL_MIN:
                ans += 1
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines)
    p2(lines)
