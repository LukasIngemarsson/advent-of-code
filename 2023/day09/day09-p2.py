file = open("input.txt", "r")
ans = 0
for line in file:
    sequences = [[int(c) for c in line.split()]]
    while True:
        new_seq, prev_seq = [], sequences[-1]
        for i in range(1, len(prev_seq)):
            new_seq.append(prev_seq[i] - prev_seq[i-1])
        if all(n == 0 for n in new_seq):
            break
        sequences.append(new_seq)
    temp = 0
    for seq in reversed(sequences): # extrapolate backwards
        temp = seq[0] - temp
    ans += temp
print(ans)