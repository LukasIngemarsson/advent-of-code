def traverse_grid(grid: list) -> int:
    n, m, max_energized = len(grid), len(grid[0]), 0
    starts = [((i, 0), (0, 1)) for i in range(n)]\
        + [((i, m - 1), (0, -1)) for i in range(n)]\
        + [((0, i), (1, 0)) for i in range(m)]\
        + [((n - 1, i), (-1, 0)) for i in range(m)]
    for start in starts:
        beams, visited = [start], set()
        while beams:
            crd, dir_, new_dirs = *beams.pop(0), []
            match grid[crd[0]][crd[1]]:
                case '/':
                    new_dirs.append((-1 * dir_[1], -1 * dir_[0]))
                case '\\': # <- single backslash is parsed as two
                    new_dirs.append((dir_[1], dir_[0]))
                case '-':
                    if dir_ == (1, 0) or dir_ == (-1, 0):
                        new_dirs.extend([(0, 1), (0, -1)])
                    else:
                        new_dirs.append(dir_)
                case '|':
                    if dir_ == (0, 1) or dir_ == (0, -1):
                        new_dirs.extend([(1, 0), (-1, 0)])
                    else:
                        new_dirs.append(dir_)
                case '.':
                    new_dirs.append(dir_)
            for nd in new_dirs:
                new_crd = (crd[0] + nd[0], crd[1] + nd[1])
                if 0 <= new_crd[0] < n and 0 <= new_crd[1] < m and (new_crd, nd) not in visited:
                    beams.append((new_crd, nd))
                visited.add((crd, dir_))
        energized = len(set(x[0] for x in visited))
        if energized > max_energized:
            max_energized = energized 
    return max_energized

with open("input.txt", "r") as f:
    grid = [list(row.strip()) for row in f.readlines()]
print(traverse_grid(grid))