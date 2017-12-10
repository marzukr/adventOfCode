puzzle = "130,126,1,11,140,2,255,207,18,254,246,164,29,104,0,224"

def reverseSection(start, sectLength, array):
    indicesToRev = sectionIndices(start, sectLength, array)
    for i in range(0, int(sectLength/2)):
        temp = array[indicesToRev[i]]
        array[indicesToRev[i]] = array[indicesToRev[sectLength - 1 - i]]
        array[indicesToRev[sectLength - 1 - i]] = temp

def sectionIndices(start, sectLength, array):
    indices = []
    for i in range(start, start + sectLength):
        indices.append(usableIndex(i, array))
    return indices

def usableIndex(index, array):
    returnIndex = index
    while returnIndex >= len(array):
        returnIndex = returnIndex - len(array)
    return returnIndex

# lengths = [int(length) for length in puzzle.split(",")] # Part 1
lengths = [ord(length) for length in puzzle] + [int(num) for num in "17, 31, 73, 47, 23".split(", ")] # Part 2

numList = [i for i in range(0,256)]
currentPos = 0
skip = 0
for _ in range(0,64): # Part 2
    for length in lengths:
        reverseSection(currentPos, length, numList)
        currentPos = usableIndex(currentPos + length + skip, numList)
        skip += 1

# print(numList[0] * numList[1]) # Part 1

# Part 2
denseHash = []
for i in range(0, 16):
    dense = numList[16*i]
    for j in range(16*i + 1, (i+1)*16):
        dense ^= numList[j]
    denseHash.append(dense)

hexHash = "".join(["{:02x}".format(num) for num in denseHash])
print(hexHash)