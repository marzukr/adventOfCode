# 17  16  15  14  13
# 18   5   4   3  12
# 19   6   1   2  11
# 20   7   8   9  10
# 21  22  23  24  25

# 4   3   2   3   4
# 3   2   1   2   3
# 2   1   0   1   2
# 3   2   1   2   3
# 4   3   2   3   4

location = 325489

# # PART 1
# layer = 0 # The layer that the location is located
# square = 1 # The max value of the layer of the location
# while square*square < location:
#     square += 2
#     layer += 1

# # Get the values for the corners of the layer of the location
# bottomRight = square*square
# bottomLeft = bottomRight - square + 1
# topLeft = bottomLeft - square + 1
# topRight = topLeft - square + 1
# corners = [bottomRight, bottomLeft, topLeft, topRight]

# # Get the distance between the location and the closest corner
# cornerDistances = [abs(corner-location) for corner in corners]
# minCornerDistance = min(cornerDistances)

# # Get the max distance of the layer, then subtract the distance to closest corner
# layerMaxSteps = 2*layer
# steps = layerMaxSteps - minCornerDistance
# print(steps)

# PART 2
# Generate the directions to create the spiral
def spiralGenerator():
    yield (1, 0)
    square = 3
    while True:
        for _ in range(0, square-2):
            yield (0, 1)
        for _ in range(0, square-1):
            yield (-1, 0)
        for _ in range(0, square-1):
            yield (0, -1)
        for _ in range(0, square):
            yield (1, 0)
        square += 2

values = {0: {0: 1}}
lastValue = {"x": 0, "y": 0, "val": 1}

spiral = spiralGenerator()
while lastValue["val"] < location:
    # Get the coordinates of the next sqaure in the spiral
    nextDirection = next(spiral)
    nextCoord = (lastValue["x"]+nextDirection[0], lastValue["y"]+nextDirection[1])

    # Get the adjacent coordinates of nextCoord
    adjCoords = []
    for x in range(-1, 2):
        for y in range(-1, 2):
            if (x != 0) or (y != 0):
                adjCoord = (nextCoord[0] + x, nextCoord[1] + y)
                adjCoords.append(adjCoord)

    # Add the value of adjacent squares if they exist
    value = 0
    for adjCoord in adjCoords:
        try:
            value += values[adjCoord[0]][adjCoord[1]]
        except KeyError:
            continue

    # Set the value of lastValue to the current sqaure
    lastValue = {"x": nextCoord[0], "y": nextCoord[1], "val": value}

    # Add the current square to values, making sure the keys exist
    try:
        values[nextCoord[0]]
    except KeyError:
        values[nextCoord[0]] = {}
    values[nextCoord[0]][nextCoord[1]] = value

print(lastValue["val"])