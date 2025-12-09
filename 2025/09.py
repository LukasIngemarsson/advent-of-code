import sys


def p1(lines):
    red_tiles = [tuple(map(int, l.split(','))) for l in lines]
    N = len(red_tiles)

    ans = 0
    for i in range(N):
        ax, ay = red_tiles[i]
        for j in range(i + 1, N):
            bx, by = red_tiles[j]
            ans = max(ans, abs(ax - bx + 1) * abs(ay - by + 1))
    print(ans)


def p2(lines):
    red_tiles = [tuple(map(int, l.split(','))) for l in lines]
    N = len(red_tiles)

    def area(i, j):
        ax, ay = red_tiles[i]
        bx, by = red_tiles[j]
        return abs(ax - bx + 1) * abs(ay - by + 1)

    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    pairs.sort(key=lambda idxs: area(*idxs))
    while True:
        i, j = pairs.pop()
        ax, ay = red_tiles[i]
        bx, by = red_tiles[j]
        xmin = min(ax, bx)
        xmax = max(ax, bx)
        ymin = min(ay, by)
        ymax = max(ay, by)
        # print("iter", ax, ay, "/", bx, by)
        for k in range(-1, N - 1):
            xprev, yprev = red_tiles[k]
            x, y = red_tiles[k+1]
            # print(f"xprev {xprev} | yprev {yprev} | x {x} |\
                    # y {y} | xmin {xmin} | xmax {xmax} | ymin {ymin} | ymax {ymax}")
            between_x = xmin < x < xmax
            between_y = ymin < y < ymax
            crossed_x = xprev <= xmin and x > xmin or xprev >= xmax and x < xmax
            crossed_y = yprev <= ymin and y > ymin or yprev >= ymax and y < ymax
            if between_y and crossed_x or between_x and crossed_y:
                break
        else:
            ans = area(i, j)
            print(ans)
            break


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    p2(lines)
