
H = [0,0]
T = [0,0]
visits = [T]

while True:
    line = input()

    if line == "exit":
        print(len(visits))
        break

    comms = line.split(" ") # [0] = dir, [1] = nr
    for i in range (0, int(comms[1])):
        prev = H.copy()
        if comms[0] == "R":
            H[0] += 1

        elif comms[0] == "L":
            H[0] -= 1

        elif comms[0] == "U":
            H[1] += 1

        elif comms[0] == "D":    
            H[1] -= 1  
        if not (abs(T[0]-H[0]) <= 1 and abs(T[1]-H[1]) <= 1):
            T = prev
            if T not in visits:
                visits.append(T)
    