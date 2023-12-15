from aoc_tools import AoCPuzzle, flatten
import functools

def differences(values: [int]):
    return [v-values[n] for n,v in enumerate(values[1:])] 

def prediction(values: [int], left: bool = False):
    # print(values)
    d = differences(values)
    if len(d) == 1 or (len(set(d)) == 1 and d[0] == 0):
        return values[0]
    return values[0] - prediction(d, left) if left else values[-1] + prediction(d,left)


# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day9.txt')

print(sum([prediction([int(v) for v in l.strip().split(' ')]) for l in p.lines]))
print(sum([prediction([int(v) for v in l.strip().split(' ')], True) for l in p.lines]))
