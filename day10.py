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

def flood_fill(fm, dm, positions):
    while len(positions) > 0:
        x,y = positions[0]
        positions = positions[1:]

        if fm[y][x] != ' ':
            continue
    
        fm[y][x] = 'O'

        if x > 0: 
            positions += [(x-1, y)]
        if x < len(fm[0])-1:
            positions += [(x+1, y)]
        if y > 0:
            positions += [(x, y-1)]
        if y < len(fm)-1:
            positions += [(x, y+1)]

    return fm

def flood_map(dm, map):
    fm = [[None for x in l + l] for l in dm + dm]
    for y,l in enumerate(map):
        for x,e in enumerate(l):
            fm[y*2][x*2] = e if dm[y][x] is not None else ' '
            fm[y*2][x*2+1] = '-' if x < len(l)-1 and dm[y][x] is not None and connected(map, x, y, x+1, y) else ' '
            fm[y*2+1][x*2] = '|' if y < len(map)-1 and dm[y][x] is not None and connected(map, x, y, x, y+1) else ' '
            fm[y*2+1][x*2+1] = ' '

    return fm

def reduce_map(fm, dm):
    return [[fm[y*2][x*2] for x,e in enumerate(l)] for y,l in enumerate(dm)]

# ---------------------------------------------------------------

# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day10.txt')

map = [list(l.strip()) for l in p.lines]
start = find_start(p)
dm = distance_map(map, start)

# print("\n".join(["".join(y) for y in map]), "\n")
# print("\n".join(["".join([' ' if x is None else chr(x+ord('0')) for x in y]) for y in dm]))
print(max([f for f in flatten(dm) if f is not None]))


# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day10.txt')

map = [list(l.strip()) for l in p.lines]
start = find_start(p)
dm = distance_map(map, start)
fm = flood_map(dm, map)

# print("\n".join(["".join(y) for y in map]), "\n")
print("\n".join(["".join([' ' if x is None else chr((x%16)+ord('0')) for x in y]) for y in dm]), "\n")
print("\n".join(["".join(y) for y in fm]), "\n")

fm = flood_fill(fm, dm, [(0, 0), (0, len(fm)-1), (len(fm[0])-1, 0), (len(fm[0])-1, len(fm)-1)])
print("\n".join(["".join(y) for y in fm]), "\n")
fm = reduce_map(fm, dm)

print("\n".join(["".join(y) for y in fm]), "\n")
print(len([i for i in flatten(fm) if i == ' ']))
