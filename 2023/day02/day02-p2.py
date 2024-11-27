ans = 0
file = open("input.txt", "r")
line = file.readline()
while line:
    min_cubes = dict()
    parts = line.replace(',', '').replace(':', '').replace('\n', '').replace(';', '').split(' ')
    for i in range(2, len(parts), 2):
        if int(parts[i]) > min_cubes.get(parts[i + 1], 0):
            min_cubes[parts[i + 1]] = int(parts[i])
    ans += min_cubes['red'] * min_cubes['green'] * min_cubes['blue']
    line = file.readline()
print(ans)