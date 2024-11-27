with open("input.txt", "r") as f:
    grid = [list(line.strip())for line in f.readlines()]
    ans = len(grid) * grid[0].count('O')
    for i, row in enumerate(grid[1:], start=1):
        rrocks = [i_ for i_, ch in enumerate(row) if ch == 'O']
        for rri in rrocks:
            off = 0
            for j in reversed(range(i)):
                if grid[j][rri] == '.':
                    off += 1
                else:
                    break
            if off:
                grid[i-off][rri], grid[i][rri] = 'O', '.'
            ans += len(grid)-(i-off)
print(ans)