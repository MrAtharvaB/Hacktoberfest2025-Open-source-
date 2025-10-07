n = 3
matrix = []
count = 1

for i in range(n):
    row = []
    for j in range(n):
        row.append(count)
        count += 1
    matrix.append(row)

print(matrix)
