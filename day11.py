from aoc_tools import AoCPuzzle, flatten
import itertools

# ---------------------------------------------------------------

def expand_galaxies(p: AoCPuzzle, expansion):
    expansion -= 1
    galaxies = []
    empty_columns = [x for x in range(len(p.lines[0].strip())) if len([l for l in p.lines if l[x] == '#']) == 0]
    empty_rows = [y for y in range(len(p.lines)) if set(p.lines[y].strip()) == set('.')]
    empty_columns += [len(p.lines[0].strip())]
    empty_rows += [len(p.lines)]
    print(empty_rows, empty_columns)
    by = 0
    for y,l in enumerate(p.lines):
        while y > empty_rows[by] and by < len(empty_rows)-1:
            by += 1
        bx = 0
        for x,e in enumerate(l.strip()):
            while x > empty_columns[bx] and bx < len(empty_columns)-1:
                bx += 1
            if e == '#':
                galaxies += [(x + expansion*bx, y + expansion*by)]

    return galaxies

def distance(g1, g2):
    x1, y1 = g1
    x2, y2 = g2
    return abs(x2-x1) + abs(y2-y1)

def determine_distances(expansion: int):
    galaxies = expand_galaxies(p, expansion)
    print(galaxies)
    gc = itertools.combinations(range(len(galaxies)), 2)
    return sum([distance(galaxies[g1], galaxies[g2]) for (g1, g2) in gc])

# ---------------------------------------------------------------

# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day11.txt')

print(determine_distances(2))
# print(determine_distances(10))
# print(determine_distances(100))
print(determine_distances(1000000))
