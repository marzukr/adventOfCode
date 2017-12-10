with open('6.txt') as f:
    puzzle = f.read()
banks = [int(block) for block in puzzle.split("\t")]

states = []
lastState = []
cycle = 0
while lastState not in states:
    states.append(lastState[:])

    maxBank = 0
    maxBankIndex = 0
    for i in range(0, len(banks)):
        if banks[i] > maxBank:
            maxBank = banks[i]
            maxBankIndex = i
    banks[maxBankIndex] = 0

    redisIndex = maxBankIndex + 1
    while maxBank > 0:
        if redisIndex >= len(banks):
            redisIndex = 0
        banks[redisIndex] += 1
        maxBank -= 1
        redisIndex += 1

    lastState = banks[:]
    cycle += 1

# print(cycle) # Part 1
print(len(states) - states.index(lastState)) # Part 2

