import re

class AoCPuzzle(object):

    def __init__(self, filename, regex = None):
        with open(filename) as f:
            self.lines = f.readlines()

        if regex is not None:
            self.matchers = [ re.match(re.compile(regex), line) for line in self.lines ]


def flatten(l):
    return [item for sublist in l for item in sublist]