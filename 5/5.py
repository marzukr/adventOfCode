with open('5.txt') as f:
    puzzle = f.read()

instructions = puzzle.split("\n")
instructions = [int(instruction) for instruction in instructions]

currentI = 0
steps = 0

while currentI >= 0 and currentI < len(instructions):
    thisI = currentI
    currentI += instructions[thisI]

    # # Part 1
    # instructions[thisI] += 1

    # Part 2
    if instructions[thisI] >= 3:
        instructions[thisI] -= 1
    else:
        instructions[thisI] += 1

    steps += 1

print(steps)