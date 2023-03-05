# Given an array of integers, find the first missing positive integer in 
# linear time and constant space. In other words, find the lowest positive
# integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

# For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] 
# should give 3.

# You can modify the input array in-place.



# SOURCE:
# I have used the idea presented in this video for my algorithm. Make sure you watch it to understand the code better : https://www.youtube.com/watch?v=-lfHWWMmXXM

def missing_digit(numbers):
    length = len(numbers)
    for i in range(length):
        # checks if:
        #   - number is at wrong index
        #   - number is lesser than the total number of numbers
        #   - number is a positive number
        #   - number's value is not same as the value of the number that it is going to replace (otherwise the while loop would never end because it keeps switching the two numbers)
        while (numbers[i] != i + 1) and (0 < numbers[i] < length) and (numbers[i] != numbers[numbers[i] - 1]):
            # swaps two numbers
            temp = numbers[i]
            numbers[i], numbers[temp - 1] = numbers[temp - 1], numbers[i]

    # finds the first number that is at an index, not equal to number's value
    for i in range(len(numbers)):
        if numbers[i] != i + 1:
            return i+1
    # if all numbers are at the right indexes, then the missing number would be total number of numbers + 1
    return len(numbers) + 1


numbers = [3, 4, -1, 1]
print(missing_digit(numbers))