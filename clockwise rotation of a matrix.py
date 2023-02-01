'''
Given an N by N matrix, rotate it by 90 degrees clockwise.

For example, given the following matrix:

[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

you should return:

[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

'''


# Algorithm explanation
'''
Matrix A:
[[1, 2, 3],
 [4, 5, 6],
 [7, 8, 9]]

Matrix B:
[[7, 4, 1],
 [8, 5, 2],
 [9, 6, 3]]

Matrix B, by referencing to matrix A's indexes:
|[2][0],[1][0],[0][0]|
|[2][1],[1][1],[0][1]|
|[2][2],[1][2],[0][2]|

'''

def rotate(matrix):
    rotated = []
    for i in range(len(matrix)):
        rotated.append([])
        for j in range(len(matrix))[::-1]:
            rotated[i].append(matrix[j][i])
    return rotated


# Generates a n by n matrix. Each row has numbers from 1 to n in order. You can use any other n by n matrix instead too
n = 10
matrixA = []
for i in range(n):
    matrixA.append([])
    for j in range(1,n+1):
        matrixA[i].append(j)


matrixB = rotate(matrixA)

# Shows the rotated matrix
for row in matrixB:
    print(row)