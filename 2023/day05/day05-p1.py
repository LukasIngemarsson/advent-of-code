file = open("input.txt", "r")
seeds, ranges, expect_new_map, min_loc = [], [], False, float('inf')
for i, line in enumerate(file):
    if i == 0: # read in seeds
        seeds = [int(x) for x in line.strip().split(':')[1].split()]
    elif line == '\n': # new line, expect new map next iteration
        expect_new_map = True
    elif expect_new_map: # new map
        expect_new_map = False
        new_map = line.strip().replace(' map:', '').split('-to-')
        ranges.append([])
    else: # range
        map_range = [int(x) for x in line.strip().split()] # 0: dest range start, 1: src range start, 2: range length
        ranges[-1].append(map_range)
for seed in seeds:
    curr_key = seed
    for ranges_ in ranges:
        for r in ranges_:
            if curr_key >= r[1] and curr_key < r[1] + r[2]:
                curr_key = r[0] + (curr_key - r[1])
                break
    if curr_key < min_loc: min_loc = curr_key
print(min_loc)