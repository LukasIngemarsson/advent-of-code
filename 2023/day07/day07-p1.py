from collections import Counter

def get_ordered_index(elem, list_, order):
    if list_:
        for i, item in enumerate(list_):
            for j in range(5):
                if order.index(elem[j]) > order.index(item[j]):
                    break
                elif order.index(elem[j]) < order.index(item[j]):
                    return i
        return len(list_)
    return 0

file = open("input.txt", "r")
types = {i: [] for i in range(7)}
card_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2'][::-1]
for line in file:
    hand, bid = line.split()
    counts = sorted(list(Counter(hand).values()))
    t_key = 0 # default high card
    if counts == [5]: # five of a kind
        t_key = 6
    elif counts == [1, 4]: # four of a kind
        t_key = 5
    elif counts == [2, 3]: # full house
        t_key = 4
    elif counts == [1, 1, 3]: # three of a kind
        t_key = 3
    elif counts == [1, 2, 2]: # two pair
        t_key = 2
    elif counts == [1, 1, 1, 2]: # one pair
        t_key = 1
    eq_types = types[t_key]
    eq_types.insert(get_ordered_index(hand, [v[0] for v in eq_types], card_order),
                    (hand, int(bid)))
    types[t_key] = eq_types
ans, rank = 0, 1
for key, val in types.items():
    for j, v in enumerate(val):
        ans += v[1] * rank
        rank += 1
print(ans)
        