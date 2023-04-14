# The following class contains tools to manipulate any n x m matrix. In order to use the tools on a matrix, create an object by inputting the matrix in the format of a 2D list.

from fractions import Fraction

class Matrix:
    def __init__(self, matrix) -> None:
        self.matrix = matrix
        self.rows = len(matrix)
        self.columns = len(matrix[0])
        self._identity = None
        self._augmented = None
        self._inverse = None
        self._determinant = None

    # Row elementary operations: (Note: there is no function for row displacement operation as it can be done using python's syntax, so I saw no point in defining a function for it)

    # Adds n times rowA to rowB
    def _add(self, rowA, rowB, n=1):
        for i in range(len(rowA)):
            rowB[i] = rowB[i] + (n * rowA[i])
        return rowB
    
    # Divides whole row by divider
    def _divide(self, row, divider):
        for i in range(len(row)):
            row[i] /= divider
        return row
    
    # Generates an n x n identity matrix
    @property
    def identity(self):
        if not self._identity:
            if self.rows == self.columns:
                self._identity = []
                for a in range(self.rows):
                    self._identity.append([])
                    for b in range(self.columns):
                        if a == b:
                            self._identity[a].append(1)
                        else:
                            self._identity[a].append(0)
            else:
                print("Identity matrix can only be generated for a matrix with equal number of rows and columns")
                return None
        return self._identity
    
    # Generates an augmented matrix for a given matrix by joining it to its identity matrix using self.i_generator
    @property
    def augmented(self):
        if self.identity:
            if not self._augmented:
                self._augmented = []
                for i in range(self.rows):
                    self._augmented.append(self.matrix[i].copy())
                    self._augmented[i].extend(self.identity[i])
            return self._augmented
        else:
            print("Augmented matrix requires a matrix with equal number of rows and columns")
            return None
        
    # Generates the inverse of a given matrix
    @property
    def inverse(self):
        if not self._inverse:
            self._inverse = self.augmented
            for i in range(self.columns):
                divider = self._inverse[i][i]
                preferred_index = -1
                for j in range(i, self.rows):
                    if self._inverse[j][i] == 1:
                        preferred_index = j
                        break
                    if self._inverse[j][i] != 0:
                        preferred_index = j
                if preferred_index == -1:
                    print("The given matrix is not invertible")
                    return None
                else:
                    if (divider == 0) or (divider > 1 and self._inverse[preferred_index][i] == 1):
                        self._inverse[i], self._inverse[preferred_index] = self._inverse[preferred_index], self._inverse[i]
                        divider = self._inverse[i][i]
                    if divider != 1:
                        self._inverse[i] = self._divide(self._inverse[i], divider)
                for j in range(self.rows):
                    if j != i:
                        self._inverse[j] = self._add(self._inverse[i], self._inverse[j], -1 * self._inverse[j][i])
            for i in range(self.rows):
                self._inverse[i] = self._inverse[i][self.columns:]
        return self._inverse
        
    # Calculates the determinant
    # The method used is applicable for any n by n matrix. In this method, the matrix is converted to an upper triangle matrix while keeping the diagonal elements as 1 using row elementary operations. Dividing any row by a constant (C), divided the determinant by C too. Also displacing rows changes the sign of the determinant. So the determinant is calculated by keeping track of the sign change and the product of all the numbers that the rows were divided by.
    @property
    def determinant(self):
        if not self._determinant:
            if self.columns == self.rows:
                matrix = self.matrix

                # This variable hold the sign of the determinant. Its value changes from 1 to -1 and vice versa if two rows are replaced with eachother. It is multiplied by the value of the determinant at the end of the algorithm
                sign = 1

                # This variable grows bigger as rows are divided. When the diagonal's elements are all equal to 1, this variable would contain the value of the determinant
                multiple = 1

                for i in range(self.columns):
                    # print("Start")
                    # for row in matrix:
                    #     print(row)
                    divider = matrix[i][i]
                    preferred_index = -1
                    for j in range(i, self.rows):
                        if matrix[j][i] == 1:
                            preferred_index = j
                            break
                        if matrix[j][i] != 0:
                            preferred_index = j
                    if preferred_index == -1:
                        return 0
                    else:
                        if (divider == 0) or (divider > 1 and matrix[preferred_index][i] == 1):
                            matrix[i], matrix[preferred_index] = matrix[preferred_index], matrix[i]
                            sign *= -1
                            divider = matrix[i][i]
                        if divider != 1:
                            matrix[i] = self._divide(matrix[i], divider)
                            multiple *= divider
                    for j in range(i +1, self.rows):
                        if matrix[j][i] != 0:
                            matrix[j] = self._add(matrix[i], matrix[j], -1 * matrix[j][i])
                    # print("End")
                    # for row in matrix:
                    #     print(row)
                    self._determinant = multiple * sign
            else:
                print("Your matrix does not have equal number of rows and columns")
                return None
        return self._determinant
    
    def __repr__(self) -> str:
        string = ""
        for row in self.matrix:
            string = string + str(row) + '\n'
        return string