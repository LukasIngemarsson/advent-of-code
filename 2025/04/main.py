import sys


def p1(lines):
    grid = lines
    n, m = len(grid), len(grid[0])

    MAX_ADJ = 3
    PAPER_ROLL = '@'

    def can_be_accessed(r, c):
        cnt = 0
        for dr in range(-1, 1 + 1):
            for dc in range(-1, 1 + 1):
                nr, nc = r + dr, c + dc
                oob = nr >= n or nr < 0 or nc >= m or nc < 0

                if oob or (nr == r and nc == c):
                    continue

                if grid[r+dr][c+dc] == PAPER_ROLL:
                    cnt += 1

                if cnt > MAX_ADJ:
                    return False
        return True

    ans = 0
    for r in range(n):
        for c in range(m):
            if grid[r][c] == PAPER_ROLL:
                ans += can_be_accessed(r, c)

    print(ans)


def p2(lines):
    grid = [[ch for ch in l] for l in lines]
    n, m = len(grid), len(grid[0])

    MAX_ADJ = 3
    PAPER_ROLL = '@'

    def can_be_accessed(r, c):
        cnt = 0
        for dr in range(-1, 1 + 1):
            for dc in range(-1, 1 + 1):
                nr, nc = r + dr, c + dc
                oob = nr >= n or nr < 0 or nc >= m or nc < 0

                if oob or (nr == r and nc == c):
                    continue

                if grid[r+dr][c+dc] == PAPER_ROLL:
                    cnt += 1

                if cnt > MAX_ADJ:
                    return False
        return True

    ans = 0
    accessible = True
    while accessible:
        accessible = False
        for r in range(n):
            for c in range(m):
                if grid[r][c] == PAPER_ROLL and can_be_accessed(r, c):
                    ans += 1
                    grid[r][c] = 'x'
                    accessible = True

    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines)
    p2(lines)
