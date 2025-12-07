import sys
from collections import deque


def p1(lines):
    START = 'S'
    EMPTY_SPACE = '.'

    grid = [list(l) for l in lines]
    N, M = len(grid), len(grid[0])
    start_pos = next((r, c) for r in range(N) for c in range(M) if grid[r][c] == START)

    ans = 0
    seen = set()
    q = deque([start_pos])
    while q:
        r, c = q.popleft()
        if r + 1 >= N or (r + 1, c) in seen or c < 0 or c >= M:
            continue
        next_cell = grid[r+1][c]
        if next_cell == EMPTY_SPACE:
            q.append((r + 1, c))
            seen.add((r + 1, c))
        else: # splitter
            beams = [(r + 1, c - 1), (r + 1, c + 1)]
            q.extend(beams)
            seen.update(set(beams))
            ans += 1
    print(ans)


def p2(lines):
    START = 'S'
    EMPTY_SPACE = '.'

    grid = [list(l) for l in lines]
    N, M = len(grid), len(grid[0])
    sr, sc = next((r, c) for r in range(N) for c in range(M) if grid[r][c] == START)

    memo = [[-1] * M for _ in range(N)]
    def dfs(r, c):
        if c < 0 or c >= M:
            return 0
        if r + 1 >= N:
            return 1
        if memo[r+1][c] == -1:
            next_cell = grid[r+1][c]
            if next_cell == EMPTY_SPACE:
                memo[r+1][c] = dfs(r + 1, c)
            else: # splitter
                memo[r+1][c] = dfs(r + 1, c - 1) + dfs(r + 1, c + 1)
        return memo[r+1][c]
    ans = dfs(sr, sc)
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    p2(lines)
