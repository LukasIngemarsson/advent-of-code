import copy

snake = [] # [0] = H, [9] = T
for i in range(0,10):
    snake.append([0,0])
visits = [copy.deepcopy(snake[9])]

def checkDirection(diff, knot, coord):
    if diff[coord] > 0:
        snake[knot][coord] += 1
    elif diff[coord] < 0:
        snake[knot][coord] -= 1

while True:
    line = input()

    if line == "exit":
        print(len(visits))
        break

    comms = line.split(" ") # [0] = dir, [1] = nr
    for i in range (0, int(comms[1])):
        if comms[0] == "R":
            snake[0][0] += 1

        elif comms[0] == "L":
            snake[0][0] -= 1

        elif comms[0] == "U":
            snake[0][1] += 1

        elif comms[0] == "D":    
            snake[0][1] -= 1

        for j in range(1, len(snake)):
            diff = [snake[j-1][0]-snake[j][0], snake[j-1][1]-snake[j][1]]
            if diff[0] == 2:
                snake[j][0] += 1
                checkDirection(diff, j, 1)   
 
            elif diff[0] == -2:
                 snake[j][0] -= 1
                 checkDirection(diff, j, 1)

            elif diff[1] == 2:
                 snake[j][1] += 1
                 checkDirection(diff, j, 0)

            elif diff[1] == -2:    
                 snake[j][1] -= 1
                 checkDirection(diff, j, 0)
            
        if snake[9] not in visits:
           visits.append(copy.deepcopy(snake[9]))              
    