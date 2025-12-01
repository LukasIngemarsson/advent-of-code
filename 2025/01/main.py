import sys


def p1(lines):
    DIAL_MIN = 0
    DIAL_MAX = 100

    dial = 50
    cnt = 0
    for line in lines:
        dir_, turns = line[0], int("".join(line[1:]))

        if dir_ == "R":
            dial = (dial + turns) % DIAL_MAX
        else:
            dial -= turns
            while dial < DIAL_MIN:
                dial += DIAL_MAX
        if dial == 0:
            cnt += 1
    print(cnt)


def p2(lines):
    DIAL_MIN = 0
    DIAL_MAX = 100

    dial = 50
    cnt = 0
    for line in lines:
        dir_, turns = line[0], int("".join(line[1:]))

        if dir_ == "R":
            cnt += (dial + turns) // DIAL_MAX
            dial = (dial + turns) % DIAL_MAX
        else:
            prev_dial = dial
            dial -= turns
            if dial < DIAL_MIN and prev_dial == 0:
                cnt -= 1
            while dial < DIAL_MIN:
                dial += DIAL_MAX
                cnt += 1
            if dial == DIAL_MIN:
                cnt += 1
    print(cnt)


if __name__ == "__main__":
    with sys.stdin as f:
        lines = [l.strip() for l in f.readlines()]

    p1(lines)
    p2(lines)
