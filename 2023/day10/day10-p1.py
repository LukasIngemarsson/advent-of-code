def search_loop(grid, start, directions, tiles):
    crd = start
    for dir_ in directions: # find starting direction for loop
        row, col = crd[0] + dir_[0], crd[1] + dir_[1]
        tile = grid[row][col]
        if tile == ".":
            continue
        elif (-1*dir_[0], -1*dir_[1]) in tiles[tile]:
            new_dir = [a for a in tiles[tile] if a != (-1*dir_[0], -1*dir_[1])][0]
            crd = (row, col)
            break
    steps = 1 # account for starting step
    while True:
        crd = (crd[0] + new_dir[0], crd[1] + new_dir[1])
        tile = grid[crd[0]][crd[1]]
        steps += 1
        if tile == 'S':
            return int(steps / 2) # point farthest from start
        new_dir = [a for a in tiles[tile] if a != (-1*new_dir[0], -1*new_dir[1])][0]

file = open("input.txt", "r")
grid = [list(line.strip()) for line in file.readlines()]
n, m = len(grid), len(grid[0])
start = [(r, c) for r in range(n) for c in range(m) if grid[r][c] == 'S'][0]
north, south, east, west = (-1,0), (1,0), (0,1), (0,-1)
tiles = {'|': (north, south),
         '-': (east, west),
         'L': (north, east),
         'J': (north, west),
         '7': (south, west),
         'F': (south, east),
        }
print(search_loop(grid, start, (north, south, east, west), tiles))