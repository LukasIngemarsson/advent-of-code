import sys


def p1(lines):
    ans = 0

    for line in lines:
        maxv = 0

        for i in range(len(line)):
            for j in range(i + 1, len(line)):
                maxv = max(maxv, int(line[i] + line[j]))
        ans += maxv

    print(ans)


def p2(lines):
    SEQ_LEN = 12
    ans = 0

    for line in lines:
        seq = []
        nums = [int(ch) for ch in line] 
        idx = 0

        while len(seq) < SEQ_LEN:
            maxv = 0
            new_idx = 0
            end = len(nums) - (SEQ_LEN - len(seq) - 1)
            for i in range(idx, end):
                if nums[i] > maxv:
                    maxv = nums[i]
                    new_idx = i
            idx = new_idx + 1
            seq.append(maxv)
        ans += int("".join(map(str, seq)))

    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines)
    p2(lines)
