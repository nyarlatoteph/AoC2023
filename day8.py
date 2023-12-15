from aoc_tools import AoCPuzzle, flatten
import functools

# p = AoCPuzzle('day_debug.txt')
p = AoCPuzzle('day8.txt')

instructions = p.lines[0].strip()
map = {l.split(" = ")[0] : l.split(" = ")[1].strip().replace('(', '').replace(')', '').split(", ") for l in p.lines[2:]}

print(map)

# node = 'AAA'
# ii = 0
# steps = 0
# while node != 'ZZZ':
#     instruction = instructions[ii]
#     ii = (ii + 1) % len(instructions)
#     nn = 0 if instruction == 'L' else 1
#     print(node)
#     node = map[node][nn]
#     steps += 1
    
# print(steps)

node = 'A'
sim_nodes = [n for n in map.keys() if n[-1] == node]
print(sim_nodes)
ii = 0
steps = 0
while len([s for s in sim_nodes if s[-1] != 'Z']) > 0:
    instruction = instructions[ii]
    ii = (ii + 1) % len(instructions)
    nn = 0 if instruction == 'L' else 1
    sim_nodes = [map[s][nn] for s in sim_nodes]
    # print(sim_nodes)
    steps += 1
    
print(steps)
