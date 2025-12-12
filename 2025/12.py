import sys
import numpy as np


def p1(lines):
    """
    unsolved.
    """
    presents = []
    regions = []
    i = 0
    while i < len(lines):
        l = lines[i]
        if l[1] == ':':
            present = []
            i += 1
            while lines[i] != '':
                present.append([int(ch == '#') for ch in lines[i]])
                i += 1
            presents.append(np.stack(present))
        elif 'x' in l:
            a, b = l.split(': ')
            dim = tuple(map(int, a.split('x')))
            freq = tuple(map(int, b.split()))
            regions.append([dim, freq])
        i += 1

    # print(*presents, sep='\n\n')
    # print()
    # print(*regions, sep='\n')
    

if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    # p2(lines)
