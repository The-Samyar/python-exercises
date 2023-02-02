'''
Given a string, determine whether any permutation of it is a palindrome.

For example, carrace should return true, since it can be rearranged to form racecar, which is a palindrome.
daily should return false, since there's no rearrangement that can form a palindrome.
'''

def palindrome_check(word):
    # It is used to store the number of times a character is used in the word. Every key is a distinct character and its value holds the repetition count
    table = {}

    # Initially I set it to true and later on if conditions are met, it can change to false
    is_palindrome = True

    # Initialise the table 
    for letter in word:
        if letter in table:
            # if the letter is already added, its count is incremented by 1
            table[letter] += 1
        else:
            # if the letter is not in the table, it is added with repetition count of 1
            table[letter] = 1


    # if the number of characters in the word is even, then there should be no odd count of repetition for any letter, otherwise the word is not a palindrome. But in a case where word length is odd, then there should be one letter that has been repeated odd number of times, while the rest are repeated for some even number of times. If the number of letters with odd count is more than 1, then again the word is not a palindrome. I have combined both the situations using a odd_count_limit that is set to 0 or 1, if the length of the word is even or odd repesctively.

    if len(word) % 2 == 0:
        odd_count_limit = 0
    else:
        odd_count_limit = 1

    odd_count = 0
    for row in table:
        if table[row] % 2 != 0:
            odd_count += 1
        
        if odd_count > odd_count_limit:
            is_palindrome = False
            break

    return is_palindrome

word = 'carrace'
print(palindrome_check(word))