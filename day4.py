from aoc_tools import AoCPuzzle, flatten
import functools
import re

def to_numbers(i: str):
    return [int(d) for d in i.strip().split(" ") if d is not None and len(d) > 0]

def check1(set1: [int], set2: [int]):
    # print(f"comparing {set1} with {set2}")
    return len([x for x in set1 if x in set2])

def check2(set1: [int], set2: [int]):
    total = check1(set1, set2)
    return pow(2, total-1) if total > 0 else 0

def score(m):
    return check2(to_numbers(m.groups()[1]), to_numbers(m.groups()[3]))

def winning_numbers(m):
    return check1(to_numbers(m.groups()[1]), to_numbers(m.groups()[3]))

p = AoCPuzzle('day4.txt', "Card\\s*(\\d+):\\s*((\\d+\\s+)*)\\s*\\|\\s*((\\d+\\s+)*)")
print(sum([score(m) for m in p.matchers]))

cards = [int(m.groups()[0]) for m in p.matchers]
pos = 0
while pos < len(cards):
    card = cards[pos]
    n = winning_numbers(p.matchers[card-1])
    # print(f"Card {card} has {n} winning numbers")
    for e in range(1, n+1):
        cards += [card + e]
    # print(f"pos: {pos}, cards: {cards}")
    pos +=1
    print(f"{pos}, {len(cards)}")

print(len(cards))