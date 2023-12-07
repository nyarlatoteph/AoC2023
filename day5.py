from aoc_tools import AoCPuzzle, flatten
import functools
import re


def map_value(map: [[int]], source: int):
    for (d, s, r) in map:
        if source >= s and source < s+r:
            return d+source-s
    return source

def location(maps: dict, current_value: int, map_traversal: [str]):
    x = None
    for y in map_traversal:
        if x != None:
            map = maps[f'{x}-to-{y}']
            # print(f"{x} {current_value}")
            current_value = map_value(map, current_value)
        x = y
    return current_value

def read_maps(lines: [str]):
    maps = {}
    for line in [l for l in lines if len(l.strip()) > 0]:
        if line.find('map:') > 0:
            current_dict = line[0: line.find('map:')-1]
            maps[current_dict] = []
        else:
            maps[current_dict] = maps[current_dict] + [[int(i) for i in line.strip().split(' ') if len(i) > 0]]
    return maps


# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day5.txt')

seeds = [int(s) for s in p.lines[0][7:].split(' ')]
print(seeds)

maps = read_maps(p.lines[2:])
print(maps)

map_traversal = ['seed', 'soil', 'fertilizer', 'water', 'light', 'temperature', 'humidity', 'location']
print(min([location(maps, seed, map_traversal) for seed in seeds]))

n = 0
m = None
while n < len(seeds)-1:
    m2 = min([location(maps, seed, map_traversal) for seed in range(seeds[n], seeds[n]+seeds[n+1])])
    print(m2)
    m = min(m, m2) if m is not None else m2
    n += 2

print(m)