from copy import deepcopy

def tilt_grid(grid: list, dir_: str) -> int:
    n, m = len(grid), len(grid[0])         
    match dir_:
        case 'n':
            line_range, get_line = range(1, n), lambda x: grid[x]
            get_search_range, get_line_char = lambda x: reversed(range(x)), lambda a, b: grid[a][b] 
        case 's':
            line_range, get_line = reversed(range(n - 1)), lambda x: grid[x]
            get_search_range, get_line_char = lambda x: range(x + 1, n), lambda a, b: grid[a][b]
        case 'w':
            line_range, get_line = range(1, m), lambda x: [r[x] for r in grid]
            get_search_range, get_line_char = lambda x: reversed(range(x)), lambda a, b: grid[b][a]
        case 'e':
            line_range, get_line = reversed(range(m - 1)), lambda x: [r[x] for r in grid]
            get_search_range, get_line_char = lambda x: range(x + 1, m), lambda a, b: grid[b][a]
    for i in line_range:
        for rri in [i_ for i_, ch in enumerate(get_line(i)) if ch == 'O']:
            off = 0
            for j in get_search_range(i):
                if get_line_char(j, rri) == '.':
                    off += 1
                else:
                    break
            if off:
                match dir_:
                    case 'n':
                        grid[i-off][rri], grid[i][rri] = 'O', '.'
                    case 's':
                        grid[i+off][rri], grid[i][rri] = 'O', '.'
                    case 'w':
                        grid[rri][i-off], grid[rri][i] = 'O', '.'
                    case 'e':
                        grid[rri][i+off], grid[rri][i] = 'O', '.'                   
    return grid

with open("input.txt", "r") as f:
    grid = [list(line.strip())for line in f.readlines()]
state, prev = deepcopy(grid), []
for i in range(1000000000):
    for dir_ in ('n', 'w', 's', 'e'): # cycle
        state = tilt_grid(state, dir_)
    # printed out the total load on the north suppport beams for each iteration
    print(i, sum([(len(state) - i_) * row.count('O') for i_, row in enumerate(state)]))
    # based on this output, a pattern could be recognized, and with that
    # the 1000000000th iteration's result could be calculated