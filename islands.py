'''
Given a matrix of 1s and 0s, return the number of "islands" in the matrix.
A 1 represents land and 0 represents water, so an island is a group of 1s
that are neighboring whose perimeter is surrounded by water.

For example, this matrix has 4 islands.

1 0 0 0 0
0 0 1 1 0
0 1 1 0 0
0 0 0 0 0
1 1 0 0 1
1 1 0 0 1
'''

# logic explanation:
#   the algorithm goes through each element of the matrix and checks if it is a 1. If there is a 1, the count of islands is incremented by 1 and the value of element is replaced by a zero. Then, it checks the surrounding of the element that used to be 1 for other 1s and if there were other 1s, again the process repeats for them as well. If there was no other 1s, however, the algorithm checks the next element of the matrix. This goes on until the whole matrix is checked.

matrix = [[0, 1, 0],
          [1, 0, 0],
          [1, 0, 1],
          [1, 0, 0],
          [1, 1, 0]]

# it is a list of tuples that hold the coordinates to an element that has the value of 1 and is in surrounding of the element that is currently being checked. the format of coordinates would be in the form of tuples : (i,j)
unchecked_land = []

# count of islands
count = 0

# goes through ever element of the matrix
for i in range(0,len(matrix)):
    for j in range(0,len(matrix[0])):
        if matrix[i][j] == 1:
            count += 1
            # adds the coordinates of the element of value 1 as the first item of the unchecked_list
            unchecked_land.append((i, j))
            while unchecked_land:
                # only the first item of unchecked_list would always be checked, after using it, it is then removed from the list and the second item of the list would become the first one
                land = unchecked_land[0]

                # its value (which is 1) is set to 0 so it would not be checked again later on
                matrix[land[0]][land[1]] = 0

                # the following loops are used to check all the elements with 1 unit of distance from the element that is being currently checked
                for a in range(-1, 2):
                    for b in range(-1, 2):
                        x = land[1] + b
                        y = land[0] + a

                        # checks so that x and y are within the boundries of the matrix, so that IndexError wouldn't occur (trust me, try and except would not work for this problem)
                        if (y >= 0 and y < len(matrix)) and (x >= 0 and x < len(matrix[0])):

                            if matrix[y][x] == 1 and (y, x) not in unchecked_land:
                                unchecked_land.append((land[0] + a, land[1] + b))
                unchecked_land.remove(land)
print(count)
