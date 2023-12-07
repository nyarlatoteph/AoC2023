from aoc_tools import AoCPuzzle, flatten
import functools
import re

def number_of_ways_to_beat_record(time: int, distance: int):
    res = 0
    for i in range(time):
        acceleration = i
        time_left = time-i
        res += (1 if acceleration*time_left > distance else 0)
    return res


# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day6.txt')

times = [int(i) for i in p.lines[0][10:].strip().split(" ") if len(i) > 0]
distances = [int(i) for i in p.lines[1][10:].strip().split(" ") if len(i) > 0]

print(functools.reduce(lambda a, b: a*b, [number_of_ways_to_beat_record(times[i], distances[i]) for i in range(len(times))]))


t = int(functools.reduce(lambda a, b: a+b, [str(t) for t in times]))
d = int(functools.reduce(lambda a, b: a+b, [str(d) for d in distances]))
print(t,d)
print(number_of_ways_to_beat_record(t, d))