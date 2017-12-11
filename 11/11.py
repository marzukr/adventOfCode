"""
http://keekerdc.com/2011/03/hexagon-grids-coordinate-systems-and-distance-calculations/
See above link for explanations on hex grid distances.
"""

import operator

with open('11.txt') as f:
    puzzle = f.read()

directions = puzzle.split(",")
currentPos = (0,0,0)

movements = {
    "n": (0, 1, -1),
    "ne": (-1, 1, 0),
    "nw": (1, 0, -1),
    "s": (0, -1, 1),
    "se": (-1, 0, 1),
    "sw": (1, -1, 0),
}

maxDistance = 0 # Part 2
for direction in directions:
    currentPos = tuple(map(operator.add, currentPos, movements[direction]))

    # Part 2
    currentDistance = max([currentPos[0] - 0, currentPos[1] - 0, currentPos[2] - 0])
    if currentDistance > maxDistance:
        maxDistance = currentDistance

# # Part 1
# distance = max([currentPos[0] - 0, currentPos[1] - 0, currentPos[2] - 0])
# print(distance)

print(maxDistance) # Part 2