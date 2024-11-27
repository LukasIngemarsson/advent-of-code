def get_shortest_path_sum(graph, start_node, end_nodes, col_exps, row_exps):
    visited, queue, sum_ = [start_node], [[start_node]], 0
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        for neighbor in graph[curr]:
            if neighbor not in visited:
                if neighbor in end_nodes:
                    exps, exp_coeff = len([n for n in path if n[0] in row_exps or n[1] in col_exps]), 10**6
                    sum_ += len(path) + ((exp_coeff-1) * exps)
                    end_nodes.remove(neighbor)
                    if not end_nodes:
                        return sum_
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
                visited.append(neighbor)

file = open("input.txt", "r")
grid = [list(line.strip()) for line in file]
n, m = len(grid), len(grid[0])

# record rows/cols with no galaxies ("#")
col_expansions, row_expansions = [], []
for i in range(m):
    col = [row[i] for row in grid]
    if all(c == '.' for c in col):
        col_expansions.append(i)
for i, row in enumerate(grid):
    if all(c == '.' for c in row):
        row_expansions.append(i)

# store galaxy coordinates and translate grid to graph
galaxies, graph = [(i, j) for i in range(n) for j in range(m) if grid[i][j] == '#'], {}
for i in range(n):
    for j in range(m):
        neighbors = []
        for dir_ in [(1, 0), (0, -1), (0, 1)]: # exclude (-1, 0) since shortest path for rows above will be cleared
            crd = i + dir_[0], j + dir_[1]
            if crd[0] >= 0 and crd[0] < n and crd[1] >= 0 and crd[1] < m:
                neighbors.append(crd)
        graph[(i, j)] = neighbors
ans = 0
for i, glx in enumerate(galaxies[:-1]):
    ans += get_shortest_path_sum(graph, glx, galaxies[i+1:], col_expansions, row_expansions)
    print(i)
print(ans)