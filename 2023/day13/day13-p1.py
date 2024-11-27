def find_pattern(grid, axis) -> int:
    if axis == 'x':
        for i in range(len(grid)-1):
            offx = 0
            while i-offx >= 0 and i+offx+1 < len(grid):
                if not grid[i-offx] == grid[i+offx+1]:
                    break
                offx += 1
            else:
                return i+1
    elif axis == 'y':
        for i in range(len(grid[0])-1):
            offy = 0
            while i-offy >= 0 and i+offy+1 < len(grid[0]):
                if not [r[i-offy] for r in grid] == [r[i+offy+1] for r in grid]:
                    break
                offy += 1
            else:
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