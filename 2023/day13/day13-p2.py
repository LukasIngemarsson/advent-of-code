def find_pattern(grid, axis) -> int:
    if axis == 'x':
        for i in range(len(grid)-1):
            offx, smudge = 0, False
            while i-offx >= 0 and i+offx+1 < len(grid):
                for a, b in zip(grid[i-offx], grid[i+offx+1]):
                    if a != b:
                        if not smudge:
                            smudge = True
                        else:
                            break
                else:
                    offx += 1
                    continue
                break
            else:
                if smudge:
                    return i+1
    elif axis == 'y':
        for i in range(len(grid[0])-1):
            offy, smudge = 0, False
            while i-offy >= 0 and i+offy+1 < len(grid[0]):
                for a, b in zip([r[i-offy] for r in grid], [r[i+offy+1] for r in grid]):
                    if a != b:
                        if not smudge:
                            smudge = True
                        else:
                            break
                else:
                    offy += 1
                    continue
                break
            else:
                if smudge:
                    return i+1
    return 0

file = open("input.txt", "r")
tot_cols, tot_rows, grid = 0, 0, []
for line in file.readlines() + ['\n']:
    if line == '\n':
        tot_rows += find_pattern(grid, 'x')
        tot_cols += find_pattern(grid, 'y')
        grid = []
    else:
        grid.append(line.strip())
print(tot_cols + 100 * tot_rows)