file = open("input.txt", "r")
ans = 0
num_width = 0
engine_grid = [[c for c in line.strip()] + ['.'] for line in file] # append '.' to handle num at end of row
engine_height, engine_width = len(engine_grid), len(engine_grid[0])
gears = dict() # key: '*' coordinates, val: adjacent numbers
for i in range(engine_height):
    for j in range(engine_width):
        if engine_grid[i][j].isdigit():
            num_width += 1
        elif num_width > 0: # search for adjacent symbol
            row_search_bound = (i - 1 if i > 0 else 0,
                                i + 2 if i + 1 < engine_height else engine_height) 
            col_search_bound = (j - num_width - 1 if j - num_width > 0 else 0, 
                                j + 1 if j + 1 < engine_width else engine_width)
            for m in range(*row_search_bound):
                for n in range(*col_search_bound):
                    if engine_grid[m][n] == '*':
                        gears[(m, n)] = gears.get((m, n), []) + [int(''.join(engine_grid[i][j - num_width: j]))]
                        break
                else:
                    continue
                break
            num_width = 0      
ans = sum([val[0] * val[1] for val in gears.values() if len(val) == 2])
print(ans)