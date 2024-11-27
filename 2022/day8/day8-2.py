

grid = []

while True:
    line = input()

    if line == "exit":
        score = 0
        for i in range(1,len(grid)-1):
            for j in range (1, len(grid[i])-1):
                num = 0
                temp = 0
                dir = False # false == down, true = up
                k = i-1
                while (True):
                    temp += 1
                    if k == 0 or k == len(grid)-1 or grid[i][j] <= grid[k][j]:
                        if k > i:
                            num *= temp
                            break
                        dir = True
                        num = temp  
                        temp = 0  
                        k = i
                    if dir:
                        k += 1
                    else:
                        k -= 1    

                temp = 0
                dir = False
                k = j-1
                while (True):
                    temp += 1
                    if k == 0 or k == len(grid[i])-1 or grid[i][j] <= grid[i][k]:
                        if k > j:
                            num *= temp
                            break
                        dir = True
                        num *= temp
                        temp = 0
                        k = j
                    if dir:
                        k += 1
                    else:
                        k -= 1        
                if num > score:
                    score = num    
        print(score)
        break

    row = list(map(int, list(line)))
    grid.append(row)