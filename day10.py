from aoc_tools import AoCPuzzle, flatten
import functools

# ---------------------------------------------------------------

def find_start(p: AoCPuzzle):
    for y,l in enumerate(p.lines):
        x = l.find('S')
        if x >= 0:
            return (x,y)

def connected(map, x1, y1, x2, y2):
    a = map[y1][x1]
    b = map[y2][x2]
    return (a in ['|', 'S'] and b == '|' and x1 == x2) or \
        (a in ['|', 'S', '7', 'F'] and b == 'L' and y1 < y2) or \
        (b in ['|', 'S', '7', 'F'] and a == 'L' and y1 > y2) or \
        (a in ['|', 'S', '7', 'F'] and b == 'J' and y1 < y2) or \
        (b in ['|', 'S', '7', 'F'] and a == 'J' and y1 > y2) or \
        (a in ['|', 'S', 'L', 'J'] and b == 'F' and y1 > y2) or \
        (b in ['|', 'S', 'L', 'J'] and a == 'F' and y1 < y2) or \
        (a in ['|', 'S', 'L', 'J'] and b == '7' and y1 > y2) or \
        (b in ['|', 'S', 'L', 'J'] and a == '7' and y1 < y2) or \
        (a in ['-', 'S'] and b == '-' and y1 == y2) or \
        (a in ['-', 'S', 'J', '7'] and b == 'L' and x1 > x2) or \
        (b in ['-', 'S', 'J', '7'] and a == 'L' and x1 < x2) or \
        (a in ['-', 'S', 'L', 'F'] and b == 'J' and x1 < x2) or \
        (b in ['-', 'S', 'L', 'F'] and a == 'J' and x1 > x2) or \
        (a in ['-', 'S', '7', 'J'] and b == 'F' and x1 > x2) or \
        (b in ['-', 'S', '7', 'J'] and a == 'F' and x1 < x2) or \
        (a in ['-', 'S', 'F', 'L'] and b == '7' and x1 < x2) or \
        (b in ['-', 'S', 'F', 'L'] and a == '7' and x1 > x2) 

def calc_distance(dm: [[int]], map: [[str]], next):
    (pos, distance, dm) = next[0]
    next = next[1:]

    y = pos[1]
    x = pos[0]
    if dm[y][x] is not None and dm[y][x] < distance:
        return (dm, next)
    
    dm[y][x] = distance
    if y > 0 and connected(map, x, y, x, y-1):
        next = next + [((x, y-1), distance+1, dm)]
    if y < len(map)-1 and connected(map, x, y, x, y+1):
        next = next + [((x, y+1), distance+1, dm)]
    if x > 0 and connected(map, x, y, x-1, y):
        next = next + [((x-1, y), distance+1, dm)]
    if x < len(map[y])-1 and connected(map, x, y, x+1, y):
        next = next + [((x+1, y), distance+1, dm)]

    return (dm, next)

def distance_map(map: [[str]], start: tuple): 
    dm = [[None for x in l] for l in map]
    next = [(start, 0, dm)]
    while len(next) > 0:
        (dm, next) = calc_distance(dm, map, next)

    return dm

def flood_fill(dm):
    fm = [['.' if x is None else 'x' for x in l] for l in dm]
    return fm

# ---------------------------------------------------------------

# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day10.txt')

map = [list(l.strip()) for l in p.lines]
start = find_start(p)
dm = distance_map(map, start)

# print("\n".join(["".join(y) for y in map]), "\n")
# print("\n".join(["".join(['.' if x is None else chr(x+ord('0')) for x in y]) for y in dm]))
print(max([f for f in flatten(dm) if f is not None]))


# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day10.txt')

map = [list(l.strip()) for l in p.lines]
start = find_start(p)
dm = distance_map(map, start)
fm = flood_fill(dm)

print("\n".join(["".join(y) for y in map]), "\n")
# print("\n".join(["".join(['.' if x is None else chr(x+ord('0')) for x in y]) for y in dm]), "\n")
print("\n".join(["".join(y) for y in fm]), "\n")
