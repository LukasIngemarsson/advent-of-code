from itertools import product

ans = 0
with open("input.txt", "r") as f:
    for line in f:
        con_rec, criteria = line.split()
        con_rec, criteria = list(con_rec), [int(x) for x in criteria.split(',')]
        unknowns = tuple(i for i, ch in enumerate(con_rec) if ch == '?')
        cmbs = tuple(cmb for cmb in product(('#', '.'), repeat=len(unknowns)))
        for cmb in cmbs:
            for i, unk in enumerate(unknowns):
                con_rec[unk] = cmb[i]
            streak, arr = 0, []
            for i, ch in enumerate(con_rec):
                if ch == '#':
                    streak += 1
                if streak > 0 and (ch == '.' or i == len(con_rec) - 1):
                    arr.append(streak)
                    if len(arr) > len(criteria) or not arr[-1] == criteria[len(arr)-1]:
                        break
                    streak = 0
            else:
                if arr == criteria:
                    ans += 1
print(ans)