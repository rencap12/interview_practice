# hi this is reneca
# hey its maham
# wassup 

# P1 transpose matrix
"""
row[0][1] = row[1][0]
2 -10 18
4 5 -7
-1 11 6

for x in range(len(matrix)):
    for y in range(x+1, len(matrix[0])):
        matrix[x][y] = matrix[y][x]
        
return matrix (double check if need this??)
def transpose(matrix):
    if not matrix or not matrix[0]:
        return []

    rows = len(matrix)
    cols = len(matrix[0])
    
    # Initialize the transposed matrix with the flipped dimensions
    transposed_matrix = [[0] * rows for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed_matrix[j][i] = matrix[i][j]
    
    return transposed_matrix
"""

def transpose(matrix):
    # first check if len(matrix) == len(matrix[0])
    if not matrix or not matrix[0]:
        return []
    
    rows = len(matrix)
    cols = len(matrix[0])

    toRet = []
    for col in range(cols):
        temp = []
        for row in range(rows):
            temp.append(matrix[row][col])
        toRet.append(temp)
    return toRet
            
    
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(transpose(matrix))

matrix = [
    [1, 2, 3],
    [4, 5, 6]
]

print(transpose(matrix))

# P 2 reverse list elements