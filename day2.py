from aoc_tools import AoCPuzzle
from collections import ChainMap
import functools
import re


configuration = { 'red':12, 'green':13, 'blue':14 }


def to_round(game: str):
    r = re.match('(\\d+)\\s+(red|blue|green)', game)
    return { r.groups()[1]: r.groups()[0] }

def to_game(part: str):
    return [to_round(game) for game in part.strip().split(', ')]

def valid_game(line: str):
    games = [to_game(l) for l in  line.strip()[line.find(": ")+2:].split("; ")]
    result = {}
    for g in [item for sublist in games for item in sublist]:
        key = list(g.keys())[0]
        value = list(g.values())[0]
        if int(value) > configuration[key]:
            print(f'{key} value {value} > configuration {configuration[key]}!')
            return False
        if key not in result or int(result[key]) < int(value) :
            result.update(g)
    # print(result)
    return True 

def game_id(line: str):
    return int(re.match('Game (\\d+):', line).groups()[0])


def power(line: str):
    games = [to_game(l) for l in  line.strip()[line.find(": ")+2:].split("; ")]
    result = {}
    for g in [item for sublist in games for item in sublist]:
        key = list(g.keys())[0]
        value = list(g.values())[0]
        if key not in result or int(result[key]) < int(value) :
            result.update(g)

    return functools.reduce(lambda x,y: int(x)*int(y), result.values())

p = AoCPuzzle('day2.txt', "")
lines = [game_id(l) for l in p.lines if valid_game(l)]
print(sum(list(lines)))

lines = [power(l) for l in p.lines]
print(sum(lines))