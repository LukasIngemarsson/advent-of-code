def hash_algorithm(ch):
    return (ch * 17) % 256

ans = 0
with open("input.txt") as f:
    sequences = [list(x) for x in f.readline().split(',')]
for seq in sequences:
    curr = 0
    for ch in seq:
        curr = hash_algorithm(curr + ord(ch))
    ans += curr
print(ans)