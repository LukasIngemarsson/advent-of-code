import math
file = open("input.txt", "r")
times = [int(x) for x in file.readline().split()[1:]]
distances = [int(x) for x in file.readline().split()[1:]]
race_wins = []
for d_rec, t in zip(distances, times):
    wins = 0
    for i in range(1, t): # excludes case 0 and t
        d = i * (t - i)
        if d > d_rec: wins += 1
    race_wins.append(wins)
print(math.prod(race_wins))