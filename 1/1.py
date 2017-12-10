with open('1.txt') as f:
    puzzle = f.read()

output = 0
shift = int(len(puzzle)/2)
for i in range(len(puzzle)):
    if puzzle[i] == puzzle[i-shift]:
        output += int(puzzle[i])

# if input[0] == input[len(input) - 1]:
#     output += int(input[0])

print(output)