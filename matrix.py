
# create matrix 5x5
N = 5
matrix = []
for row_number in range(0, N):
    row = []
    for col_number in range(0, N):
        row.append(0)
        print(row_number, col_number)
    matrix.append(row)

# add edge 1 -> 2
matrix[1][2] = 1
print(matrix)

print(len(matrix))

for idx, row in enumerate(matrix):
    print(idx, row)