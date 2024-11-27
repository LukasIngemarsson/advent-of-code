

grid = []

while True:
    line = input()

    if line == "exit":
        sum = 2*len(grid[0])
        sum += 2*(len(grid)-2)

        for i in range(1,len(grid)-1):
            for j in range (1, len(grid[i])-1):
                k = 0
                while (k < len(grid)):
                    if k == i:
                        k = len(grid)-1
                    elif grid[i][j] <= grid[k][j]:
                        if k < i:
                            k = i
                        else:
                            break
                    k += 1    
                else:
                    sum += 1 
                    continue   

                k = 0
                while (k < len(grid[i])):
                    if j == k:
                        k = len(grid[i])-1
                    elif grid[i][j] <= grid[i][k]:
                        if k < j:
                            k = j
                        else:
                            break
                    k += 1
                else:
                    sum += 1     
        print(sum)
        break

    row = list(map(int, list(line)))
    grid.append(row)