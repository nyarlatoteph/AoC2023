from aoc_tools import AoCPuzzle
import re

digits = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
spelled = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def calibration_value(line: str):
    val = first_digit(line) + last_digit(line)
    print(line, val)
    return int(val)

def first_digit(line: str):
    lowest_digits = filter(lambda x: x[1] >= 0, map(lambda d: [d, line.find(d)], digits))
    lowest_spelleds = filter(lambda x: x[1] >= 0, map(lambda s: [s, line.find(s)], spelled))
    lowest_all = list(lowest_digits) + list(lowest_spelleds)
    x = min(map(lambda l: l[1], lowest_all))
    return to_str([y for y in lowest_all if y[1] == x][0][0])

def to_str(res: str):
    if len(res) > 1:
        return str(spelled.index(res)+1)
    return res

def last_digit(line: str):
    highest_digits = filter(lambda x: x[1] >= 0, map(lambda d: [d, line.rfind(d)], digits))
    highest_spelleds = filter(lambda x: x[1] >= 0, map(lambda s: [s, line.rfind(s)], spelled))
    highest_all = list(highest_digits) + list(highest_spelleds)
    x = max(map(lambda l: l[1], highest_all))
    return to_str([y for y in highest_all if y[1] == x][0][0])


p = AoCPuzzle('day1.txt', "")
print(calibration_value('fourzqlhcjksixthreejrl9'))
print(sum(map(calibration_value, p.lines)))
