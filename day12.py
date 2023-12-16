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

def arrangement(l: str):
    springs, verification = l.strip().split(" ")
    verification = [int(s) for s in verification.split(",")]
    q = [m.start() for m in re.finditer('\\?', springs)]
    c = itertools.product(['#', '.'], repeat=len(q))

    print(springs, verification)
    return [r for r in c if verify_spring(springs, q, r, verification)]

def unfold(l: str, copies: int):
    springs, verification = l.strip().split(" ")
    return "?".join([springs]*copies) + " " + ",".join([verification]*copies)

# ---------------------------------------------------------------

p = AoCPuzzle('day_debug.txt')
# p = AoCPuzzle('day12.txt')

arrangements = [arrangement(l) for l in p.lines]
print(sum([len(a) for a in arrangements]))

# todo: iets slims
arrangements = [arrangement(unfold(l, 5)) for l in p.lines]
print(sum([len(a) for a in arrangements]))