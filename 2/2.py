with open('2.txt') as f:
    spreadsheet = f.read()

# Create a list of rows from the input and convert them to ints
rows = [list(map(int, row.split("\t"))) for row in spreadsheet.split("\n")]

# Part 1
# checksum = 0
# for row in rows:
#     checksum += max(row) - min(row)
# print(checksum)

# Part 2
def divisbleValueResult(row):
    for i in range(0, len(row)):
        for j in range(0, len(row)):
            if i != j and row[i] % row[j] == 0:
                return int(row[i]/row[j])
    return 0

result = 0
for row in rows:
    result += divisbleValueResult(row)

print(result)