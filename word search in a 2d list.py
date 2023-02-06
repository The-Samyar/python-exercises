'''
Given a 2D matrix of characters and a target word, write a function that returns whether the word can be found in the matrix by going left-to-right, or up-to-down.

For example, given the following matrix:

[['F', 'A', 'C', 'I'],
 ['O', 'B', 'Q', 'P'],
 ['A', 'N', 'O', 'B'],
 ['M', 'A', 'S', 'S']]

and the target word 'FOAM', you should return true, since it's the leftmost column. Similarly, given the target word 'MASS', you should return true, since it's the last row.
'''

def search(word, matrix):
    # for simplicity
    height = len(matrix)
    width = len(matrix[0])

    # searches the 2d list to find elements that are same as first letter in 'word'
    for i in range(height):
        for j in range(width):

            if matrix[i][j] == word[0]:

                # checking across, only if the remaining letters in the row are equal or greater than 'word'
                if len(word) <= width - j:
                    is_present_row = True
                    # checks from the second letter (index 1) of input word, because the first letter has already been checked (in line 27)
                    for k in range(1, len(word)):
                        if word[k] != matrix[i][j+k]:
                            # if at some point the letters of a row don't match with letters in 'word', then there is no point in checking further anymore
                            is_present_row = False
                            break
                    if is_present_row:
                        return True

                # checking top to bottom, only if the remaining letters in the column are equal or greater than 'word'
                if len(word) <= height - i:
                    is_present_column = True
                    for k in range(1, len(word)):
                        if word[k] != matrix[i+k][j]:
                            is_present_column = False
                            break
                    if is_present_column:
                        return True
                    
    # if the word was not present in 2d list
    return False

word = 'MASS'

matrix = [['F', 'A', 'C', 'I'],
          ['O', 'B', 'Q', 'P'],
          ['A', 'M', 'O', 'B'],
          ['M', 'A', 'S', 'S']]

print(search(word, matrix))