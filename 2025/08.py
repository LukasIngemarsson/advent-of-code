import sys
from collections import Counter


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.rank = [0] * n

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        a_root = self.find(a)
        b_root = self.find(b)
        if a_root == b_root:
            return
        if self.rank[a_root] < self.rank[b_root]:
            self.parent[a_root] = self.parent[b_root]
        elif self.rank[a_root] > self.rank[b_root]:
            self.parent[b_root] = self.parent[a_root]
        else:
            self.parent[a_root] = self.parent[b_root]
            self.rank[b_root] += 1

    def same(self, a, b):
        return self.find(a) == self.find(b)


def eucl_dist(p1, p2):
    p1x, p1y, p1z = p1
    p2x, p2y, p2z = p2
    return ((p1x - p2x)**2 + (p1y - p2y)**2 + (p1z - p2z)**2)**0.5


def p1(lines):
    pts = [tuple(map(int, l.split(','))) for l in lines]
    N = len(pts)

    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    pairs.sort(key=lambda p_idxs: eucl_dist(pts[p_idxs[0]], pts[p_idxs[1]]), reverse=True)
    uf = UnionFind(N)
    for _ in range(N):
        a, b = pairs.pop()
        uf.union(a, b)

    for i in range(N):
        uf.find(i)
    cnts = sorted(Counter(uf.parent).values())
    ans = cnts[-1] * cnts[-2] * cnts[-3]
    print(ans)


def p2(lines):
    pts = [tuple(map(int, l.split(','))) for l in lines]
    N = len(pts)

    pairs = [(i, j) for i in range(N) for j in range(i + 1, N)]
    pairs.sort(key=lambda p_idxs: eucl_dist(pts[p_idxs[0]], pts[p_idxs[1]]), reverse=True)
    uf = UnionFind(N)
    a, b = -1, -1
    num_circuits = N
    while num_circuits > 1:
        a, b = pairs.pop()
        if not uf.same(a, b):
            num_circuits -= 1
            uf.union(a, b)

    ans = pts[a][0] * pts[b][0]
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    p2(lines)
