import sys
from collections import deque


def p1(lines):
    """
    unsolved.

    tested naive solution (BFS of button pressing), but way
    too slow for worst case
    """
    LIGHT_ON = '#'
    N = len(lines)
    
    indicator_lights = []
    button_wiring = []
    for l in lines:
        split_line = l.split()
        indicator_lights.append(split_line[0])
        button_wiring.append(split_line[1:-1])
    indicator_lights = [set(i for i, ch in enumerate(s[1:-1]) if ch == LIGHT_ON) \
                            for s in indicator_lights]
    button_wiring = [[tuple(map(int, s[1:-1].split(','))) for s in lst] \
                        for lst in button_wiring]
    ans = 0
    for i in range(N):
        num_buttons = len(button_wiring[i])
        q = deque([(set(), 0)]) 
        while q:
            lights, depth = q.popleft()
            if lights == indicator_lights[i]:
                ans += depth
                break
            for j in range(num_buttons):
                new_lights = set(lights)
                for k in button_wiring[i][j]:
                    if k in new_lights:
                        new_lights.remove(k)
                    else:
                        new_lights.add(k)
                q.append((new_lights, depth + 1))
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    # p2(lines)
