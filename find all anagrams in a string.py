'''
Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
'''

def anagram_finder(word, string):
    # 'char_count' initiation. the dictionary holds every character present in the 'word' as key and the number each one is repeated as value
    char_count = {}
    for letter in word:
        if letter in char_count:
            # if it is already present in the dict, increment the count by 1
            char_count[letter] += 1
        else:
            # if it is not present in the dict, add it to the dict
            char_count[letter] = 1

    # it is required to keep a copy of the char_count as it is going to be altered during the code and we would require the original version again later on
    char_count_copy = char_count.copy()

    # list of starting indexes of anagrams 
    index_list = []


    #len(string) - (len(word) - 1) is used because the 'string' is being checked letter by letter, so it approaches an index where the remaining letters in 'string' would be shorter than length of word
    for i in range(len(string) - (len(word) - 1)):

        # to break out of loop in case there is no anagram present in 'substring' of 'string'
        error = False

        substring = string[i:i + len(word)]

        for letter in substring:
            
            # the 'letter' in substring has to be present in 'char_count' otherwise there is no anagram in the 'substring'
            if letter in char_count_copy:

                # the 'letter' has to have a count more than 0 or else there is not enough of that letter in the 'substring' so again, no anagram present in 'substring'
                if char_count_copy[letter] > 0:
                    char_count_copy[letter] -= 1
                else:
                    error = True
                    break
            else:
                error = True
                break
        
        if not error:
            index_list.append(i)
        char_count_copy = char_count.copy()

    return index_list



word = "ab"
string = "abxaba"

print(f"index_list = {anagram_finder(word, string)}")
