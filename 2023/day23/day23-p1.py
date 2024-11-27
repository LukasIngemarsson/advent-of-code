def DFS(graph, start, end):
    stack, paths = [(start, [start])], []
    while stack:
        node, path = stack.pop()
        if node == end:
            paths.append(path)
        for neighbor in graph[node]:
            if neighbor not in path:
                stack.append((neighbor, path + [neighbor]))
    return paths

with open("input.txt", "r") as f:
    grid = [[ch for ch in line.strip()] for line in f]
n, m = len(grid), len(grid[0])
up, down, left, right = (-1, 0), (1, 0), (0, -1), (0, 1)
graph, start, end = {}, (0, 1), (n - 1, m - 2)
for i, row in enumerate(grid):
    for j, ch in enumerate(row):
        dirs = []
        match ch:
            case '.':
                dirs.extend([up, down, left, right])
            case '>':
                dirs.append(right)
            case '<':
                dirs.append(left)
            case '^':
                dirs.append(up)
            case 'v':
                dirs.append(down)
        for ri, ci in dirs:
            if 0 <= i + ri < n and 0 <= j + ci < m:
                if grid[i + ri][j + ci] != '#':
                    graph[(i, j)] = graph.get((i, j), []) + [(i + ri, j + ci)]
print(max([len(path) - 1 for path in DFS(graph, start, end)]))