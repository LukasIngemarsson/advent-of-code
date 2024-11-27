import math
file = open("input.txt", "r")
t, d_rec = int(''.join(file.readline().split()[1:])), int(''.join(file.readline().split()[1:]))
# d(x) = -x^2 + tx - d_rec = 0 <=> (x-t/2)^2 = -d_rec + (t/2)^2 <=> x = t/2 +- sqrt(-d_rec + t^2/4)
win_interval = (t/2 - math.sqrt(-d_rec + t**2/4), t/2 + math.sqrt(-d_rec + t**2/4))
print(math.floor(win_interval[1] - win_interval[0])) # d(x) >= 0 between roots, so width => number of wins