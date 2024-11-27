
grid = []
end = ()
startPositions = []

def getShortestPath(graph, start_node, end_node):
    visited = set()
    visited.add(start_node)
    queue = [[start_node]]
    while queue:
        path = queue.pop(0)
        curr = path[-1]
        for neighbor in graph[curr]:
            if neighbor == end_node:
                return len(path)
            elif neighbor not in visited:
                newPath = list(path)
                newPath.append(neighbor)
                queue.append(newPath)
                visited.add(neighbor)    
    return 1000000                         

while True:
    line = input()
    if line == "#":
        graph = {}
        for i in range(0, len(grid)):
            for j in range(0, len(grid[i])):
                temp = []
                if j > 0 and (1 >= grid[i][j-1][1] - grid[i][j][1] >= 0 or grid[i][j][1] > grid[i][j-1][1]):
                    temp.append(grid[i][j-1][0])
                if j < len(grid[i])-1 and (1 >= grid[i][j+1][1] - grid[i][j][1] >= 0 or grid[i][j][1] > grid[i][j+1][1]):   
                    temp.append(grid[i][j+1][0]) 
                if i > 0 and (1 >= grid[i-1][j][1] - grid[i][j][1] >= 0 or grid[i][j][1] > grid[i-1][j][1]):
                    temp.append(grid[i-1][j][0])
                if i < len(grid)-1 and (1 >= grid[i+1][j][1] - grid[i][j][1] >= 0 or grid[i][j][1] > grid[i+1][j][1]):    
                    temp.append(grid[i+1][j][0])
                graph[grid[i][j][0]] = temp   

        shortest = 100000000
        count = 1
        for s in startPositions:
            short = getShortestPath(graph, s, end)
            count += 1
            if short < shortest:
                shortest = short         
        print(shortest)
        break

    temp = []
    rowList = list(line)
    for i in range(0, len(rowList)):
        asciiVal = ord(rowList[i])
        if rowList[i] == 'E':
            end = (len(grid), i)
            asciiVal = 123
        elif rowList[i] == 'a' or rowList[i] == 'S':
            startPositions.append((len(grid), i))
        temp.append([(len(grid), i), asciiVal])       
    grid.append(temp)