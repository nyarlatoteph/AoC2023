from aoc_tools import AoCPuzzle, flatten
import itertools
import re

# ---------------------------------------------------------------

def verify(l: str, verification: [int]):
    springs = [len(f) for f in l.split('.') if len(f) > 0]
    return springs == verification

def verify_spring(spring: str, positions: [int], replacements: [str], verification: [int]):
    result = spring
    for n,r in enumerate(replacements):
        result = result[:positions[n]] + r + result[positions[n]+1:]
    
    return verify(result, verification)

def find_combos(springs):
    q = [m.start() for m in re.finditer('\\?', springs)]
    c = itertools.product(['#', '.'], repeat=len(q))
    return q,c

def arrangement(l: str):
    springs, verification = l.strip().split(" ")
    verification = [int(s) for s in verification.split(",")]

    q,c = find_combos(springs)
    print(springs, verification)
    return [r for r in c if verify_spring(springs, q, r, verification)]

def unfold_arrangement(l: str, unfold: int):
    springs1, verification = l.strip().split(" ")
    springs2 = springs1 + '?'
    springs3 = '?' + springs1 
    verification = [int(s) for s in verification.split(",")]
    q1, c1 = find_combos(springs1)
    q2, c2 = find_combos(springs2)
    q3, c3 = find_combos(springs3)

    result1 = [r for r in c1 if verify_spring(springs1, q1, r, verification)]
    r2 = [r for r in c2 if verify_spring(springs2, q2, r, verification)]
    r3 = [r for r in c3 if verify_spring(springs3, q3, r, verification)]
    result2 = r3 if len(r3) > len(r2) and springs1[-1] != '#' else r2 if springs1[0] != '#' else result1
    # r = list(itertools.product(result2, repeat=unfold-1))
    # return len(r)*len(result1)
    print(springs1, verification, list(result1), list(result2), list(r2), list(r3))
    return len(result2)**(unfold-1)*len(result1)

# ---------------------------------------------------------------

p = AoCPuzzle('day_debug.txt')
# p = AoCPuzzle('day12.txt')

# arrangements = [arrangement(l) for l in p.lines]
# print(sum([len(a) for a in arrangements]))

arrangements = [unfold_arrangement(l, 5) for l in p.lines]
print(arrangements)
print(sum(arrangements))