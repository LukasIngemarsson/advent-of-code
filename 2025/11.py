import sys


def p1(lines):
    N = len(lines)
    SRC = "you"
    DST = "out"

    adj = [[] for _ in range(N + 1)]
    device_to_id = {DST: N}
    for i, l in enumerate(lines):
        device, neighbor_str = l.split(": ")
        device_to_id[device] = i
        adj[i] = neighbor_str.split()
    adj = [[device_to_id[nbr] for nbr in nbrs] for nbrs in adj]

    memo = [-1] * (N + 1)
    def dfs(device_id):
        if device_id == device_to_id[DST]:
            return 1
        if memo[device_id] == -1:
            memo[device_id] = sum(dfs(nbr) for nbr in adj[device_id])
        return memo[device_id]
    ans = dfs(device_to_id[SRC])
    print(ans)


def p2(lines):
    N = len(lines)
    SRC = "svr"
    DST = "out"

    adj = [[] for _ in range(N + 1)]
    device_to_id = {DST: N}
    for i, l in enumerate(lines):
        device, neighbor_str = l.split(": ")
        device_to_id[device] = i
        adj[i] = neighbor_str.split()
    adj = [[device_to_id[nbr] for nbr in nbrs] for nbrs in adj]

    def dfs(device_id, dst_id, memo=None):
        if memo is None:
            memo = [-1] * (N + 1)
        if device_id == dst_id:
            return 1
        if memo[device_id] == -1:
            memo[device_id] = sum(dfs(nbr, dst_id, memo) for nbr in adj[device_id])
        return memo[device_id]
    ans = 0
    for a, b in [("fft", "dac"), ("dac", "fft")]:
        res = 1
        res *= dfs(device_to_id[SRC], device_to_id[a])
        res *= dfs(device_to_id[a], device_to_id[b])
        res *= dfs(device_to_id[b], device_to_id[DST])
        ans += res
    print(ans)


if __name__ == "__main__":
    lines = sys.stdin.read().splitlines()

    p1(lines.copy())
    p2(lines)
