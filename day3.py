from aoc_tools import AoCPuzzle, flatten
import functools
import re

def check(s: str):
    return len(re.sub("[\\d|\\.]+", "", s)) > 0

def valid(s: str, n: int, idx: int, line: str, p: AoCPuzzle):
    prv = check(p.lines[idx-1][max(0, n-1): min(len(p.lines[idx-1]), n+len(s)+1)]) if idx > 0 else False
    nxt = check(p.lines[idx+1][max(0, n-1): min(len(p.lines[idx+1]), n+len(s)+1)]) if idx < len(p.lines)-1 else False
    lft = check(line[n-1]) if n > 0 else False
    rght = check(line[n+len(s)]) if n+len(s) < len(line) else False
    return prv or nxt or lft or rght

def valid_numbers(line: str, idx: int, p: AoCPuzzle):
    n = 0
    numbers = []
    while n < len(line):
        m = n
        while m < len(line) and ord(line[m]) >= ord('0') and ord(line[m]) <= ord('9'):
            m += 1
        num = line[n:m]
        if m > n and valid(num, n, idx, line, p):
            numbers += [int(num)]
        n = m+1

    print(numbers)
    return numbers

def is_number(x: int, y: int, p: AoCPuzzle):
    return re.match("\\d", p.lines[y][x]) != None

def cg(x: int, y: int, p: AoCPuzzle):
    if is_number(x, y, p):
        xs = x
        while xs > 0 and is_number(xs-1, y, p):
            xs -= 1
        xe = xs
        while xe < len(p.lines[y]) and is_number(xe, y, p):
            xe += 1
        return int(p.lines[y][xs: xe])
    return None

def gear_ratio(x: int, y: int, p: AoCPuzzle):
    numbers = [ cg(x-1, y-1, p), cg(x, y-1, p), cg(x+1, y-1, p), 
                cg(x-1, y, p), cg(x+1, y, p), 
                cg(x-1, y+1, p), cg(x, y+1, p), cg(x+1, y+1, p)]
    numbers = list(set([n for n in numbers if n != None]))
    if len(numbers) == 2:
        return numbers[0]*numbers[1]
    return None
    

def gear_ratios(y: int, line: str, p: AoCPuzzle):
    ratios = [gear_ratio(m.start(), y, p) for m in re.finditer('\\*', line)]
    ratios = [r for r in ratios if r != None]
    
    return ratios



p = AoCPuzzle('day3.txt', "")
p.lines = [r.strip() for r in p.lines]
print(sum(flatten([valid_numbers(l, n, p) for n, l in enumerate(p.lines)])))

gears = flatten([gear_ratios(n, l, p) for n,l in enumerate(p.lines)])
print(gears)
print(sum(gears))