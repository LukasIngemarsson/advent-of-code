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

def get_hand_type(list_):
    t_key = 0 # default high card
    if list_ == [5]: # five of a kind
        t_key = 6
    elif list_ == [1, 4]: # four of a kind
        t_key = 5
    elif list_ == [2, 3]: # full house
        t_key = 4
    elif list_ == [1, 1, 3]: # three of a kind
        t_key = 3
    elif list_ == [1, 2, 2]: # two pair
        t_key = 2
    elif list_ == [1, 1, 1, 2]: # one pair
        t_key = 1
    return t_key

def get_best_joker_hand(dict_):
    jokers, best_key = dict_.get('J', 0), 0
    if not jokers or jokers == 5: 
        best_key = get_hand_type(sorted(list(dict_.values())))
    else:
        cards_to_try = [k for k, v in dict_.items() if k != 'J']
        while(cards_to_try):
            counts = dict_.copy()
            k = cards_to_try.pop()
            counts[k] += jokers
            del counts['J']
            counts = sorted(list(counts.values()))
            t_key = get_hand_type(counts)
            if t_key > best_key: best_key = t_key
    return best_key

file = open("input.txt", "r")
types = {i: [] for i in range(7)}
card_order = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J'][::-1]
for line in file:
    hand, bid = line.split()
    t_key = get_best_joker_hand(Counter(hand))
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