with open('4.txt') as f:
    puzzle = f.read()

# # Part 1
# passphrases = puzzle.split("\n")
# valid = 0
# for passphrase in passphrases:
#     words = passphrase.split(" ")
#     seen = []
#     shouldContinue = False
#     for word in words:
#         if word not in seen:
#             seen.append(word)
#         else:
#             shouldContinue = True
#             break
#     if shouldContinue:
#         continue
#     else:
#         valid += 1
# print(valid)

# Part 2
from collections import Counter
passphrases = puzzle.split("\n")
valid = 0
for passphrase in passphrases:
    words = passphrase.split(" ")
    counters = [Counter(word) for word in words]
    shouldBreak = False
    for i in range(0, len(counters)):
        for j in range(0, len(counters)):
            if i != j and counters[i] == counters[j]:
                shouldBreak = True
                break
        if shouldBreak:
            break
    if shouldBreak:
        continue
    else:
        valid += 1
print(valid)