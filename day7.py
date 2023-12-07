from aoc_tools import AoCPuzzle, flatten
import functools
from collections import Counter

label_order = ['A', 'K', 'Q', 'J', 'T', '9', '8', '7', '6', '5', '4', '3', '2']
label_order_joker = ['A', 'K', 'Q', 'T', '9', '8', '7', '6', '5', '4', '3', '2', 'J']

def hand(line: str):
    return line.strip().split(" ")[0]

def bid(line: str):
    return int(line.strip().split(" ")[1])

def rank(hand: str, joker: bool):
    if joker:
        if hand == 'JJJJJ':
            hand = 'AAAAA'
        else:
            hand = hand.replace('J', Counter(hand.replace('J', '')).most_common()[0][0])

    s = list(set(hand))
    most_common = Counter(hand).most_common()[0][1]
    if len(s) == 1: # five of a kind
        return 7
    if len(s) == 2: # four of a kind or full house
        return 6 if most_common == 4 else 5
    if len(s) == 3: # three of a kind or two pair
        return 4 if most_common == 3 else 3
    return 2 if len(s) == 4 else 1 # one pair (4 different labels), high card (5)

def cmp(a, b):
    return (a > b) - (a < b) 

def cmp_strength(a: str, b: str, joker = False):
    lo = label_order_joker if joker else label_order
    n = 0
    while n < len(a) and lo.index(a[n]) == lo.index(b[n]):
        n += 1
    la = lo.index(a[n])
    lb = lo.index(b[n])
    return cmp(lb, la)

def compare_hands(a: str, b: str):
    ra = rank(hand(a), False)
    rb = rank(hand(b), False)
    if ra == rb:
        return cmp_strength(a, b)
    return cmp(ra, rb)

def compare_hands_joker(a: str, b: str):
    ra = rank(hand(a), True)
    rb = rank(hand(b), True)
    if ra == rb:
        return cmp_strength(a, b, True)
    return cmp(ra, rb)

# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day7.txt')

s = sorted(p.lines, key=functools.cmp_to_key(compare_hands))
print(s)
print(sum([bid(s)*(n+1) for n,s in enumerate(s)]))

s = sorted(p.lines, key=functools.cmp_to_key(compare_hands_joker))
print(s)
print(sum([bid(s)*(n+1) for n,s in enumerate(s)]))