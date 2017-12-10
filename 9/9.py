with open('9.txt') as f:
    puzzle = f.read()

def getScore(stream):
    garbage = 0 # Part 2

    # # Part 1
    # score = 0
    # closedGroups = 0
    # openGroups = 0

    inGarbage = False
    isCanceled = False
    for character in puzzle:
        # # Part 1
        # if character == "{" and not isCanceled and not inGarbage:
        #     openGroups += 1
        #     continue
        # if character == "}" and not isCanceled and not inGarbage:
        #     closedGroups += 1
        #     score += openGroups
        #     openGroups -= 1
        #     continue

        if character == "<" and not isCanceled and not inGarbage:
            inGarbage = True
            continue
        if character == ">" and not isCanceled:
            inGarbage = False
            continue

        # Part 2
        if inGarbage and character != "!" and not isCanceled:
            garbage += 1

        if character == "!" and not isCanceled:
            isCanceled = True
            continue
        if isCanceled:
            isCanceled = False
    
    # return score # Part 1
    return garbage # Part 2

print(getScore(puzzle))