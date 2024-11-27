import re

def find_intersections(hailstones):
    bound, count = (2 * 10**14, 4 * 10**14), 0
    for i, hs1 in enumerate(hailstones):
        px1, py1, vx1, vy1 = *hs1[0], *hs1[1]
        m1 = vy1 / vx1 # line slope
        b1 = py1 - m1 * px1 # line intersect with x = 0
        for hs2 in hailstones[i+1:]:
            px2, py2, vx2, vy2 = *hs2[0], *hs2[1]
            m2 = vy2 / vx2
            b2 = py2 - m2 * px2
            if m1 == m2: # parallel lines
                continue
            # m1 * x + b1 = m2 * x + b2 <=> x = (b2 - b1) / (m1 - m2)
            xintersect = (b2 - b1) / (m1 - m2) 
            yintersect = m1 * xintersect + b1
            if ((vx1 > 0 and px1 <= xintersect) or (vx1 < 0 and px1 >= xintersect)) and\
                ((vx2 > 0 and px2 <= xintersect) or (vx2 < 0 and px2 >= xintersect)) and\
                (bound[0] <= xintersect <= bound[1] and bound[0] <= yintersect <= bound[1]):
                count += 1
    return count

with open("input.txt", "r") as f:
    lines = [[int(x) for x in re.split(", | @ ", line.strip())] for line in f]
hailstones = [(line[:2], line[3:5]) for line in lines]
print(find_intersections(hailstones))