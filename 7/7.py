with open('7.txt') as f:
    puzzle = f.read()

import re # Part 2
from collections import Counter # Part 2

parents = {}
programs = []
weights = {} # Part 2
for note in puzzle.split("\n"):
    noteParts = note.split(" -> ")
    parentParts = noteParts[0].split(" ")
    parent = parentParts[0]
    programs.append(parent)
    weights[parent] = re.sub("\(|\)", "", parentParts[1]) # Part 2
    if len(noteParts) < 2:
        continue
    else:
        children = noteParts[1].split(", ")
        for child in children:
            parents[child] = parent

rootProg = ""
for program in programs:
    if program not in parents.keys():
        rootProg = program
        break
print(rootProg) # Part 1

# Part 2
children = {}
for child, parent in parents.items():
    if parent not in children:
        children[parent] = []
    children[parent].append(child)

def weight(programParam):
    weightTotal = int(weights[programParam])
    for childProg, parentProg in parents.items():
        if parentProg == programParam:
            weightTotal += weight(childProg)
    return weightTotal

def siblings(programParam):
    return children[parents[programParam]]

def balanceDiscrepancy(programParam):
    discrepancy = programParam
    if programParam in children:
        childWeights = {child: weight(child) for child in children[programParam]}
        if len(childWeights) != 1:
            wrongValue = Counter(childWeights.values()).most_common()[:-1-1:-1][0][0]
            commonValue = Counter(childWeights.values()).most_common()[0][0]
            if wrongValue == commonValue:
                return discrepancy
            for childProg, weightVal in childWeights.items():
                if weightVal == wrongValue:
                    childDiscrepancy = balanceDiscrepancy(childProg)
                    if childDiscrepancy is not None:
                        discrepancy = childDiscrepancy
    return discrepancy

damageProg = balanceDiscrepancy(rootProg)
print(damageProg)
for sibling in siblings(damageProg):
    if sibling != damageProg:
        print(int(weights[damageProg]) + weight(sibling) - weight(damageProg))
        break