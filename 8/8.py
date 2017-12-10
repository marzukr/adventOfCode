with open('8.txt') as f:
    puzzle = f.read()

import operator

instructions = [instruction for instruction in puzzle.split("\n")]
instructions = [instruction.split(" ") for instruction in instructions]

registers = {instruction[0]: 0 for instruction in instructions}

comparators = {"<": operator.lt, ">": operator.gt, "<=": operator.le, ">=": operator.ge, "==": operator.eq, "!=": operator.ne, "inc": operator.add, "dec": operator.sub}

highestValues = [] # Part 2
for instruction in instructions:
    if comparators[instruction[5]](registers[instruction[4]], int(instruction[6])):
        registers[instruction[0]] = comparators[instruction[1]](registers[instruction[0]], int(instruction[2]))
        highestValues.append(max(registers.values())) # Part 2

# print(max(registers.values())) # Part 1
print(max(highestValues)) # Part 2