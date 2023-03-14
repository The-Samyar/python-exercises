# Given a list of numbers and a number k, return whether 
# any two numbers from the list add up to k.

# For example, given [10, 15, 3, 7] and k of 17, 
# return true since 10 + 7 is 17.

numbers = [10, 15, 3, 7]
k = 17

# Both methods are kinda similar and easy to understand, except in the second method, I used python's in-operator, and it seemed to work much quicker for larger data. Also i added a few checks (especially for the 'complement' variable) to make the algorithm even quicker. 

# Method 1
def finder(numbers, k):
    for i in range(0,len(numbers)):
        for j in range(i + 1,len(numbers)):
            if numbers[i] + numbers[j] == k:
                return True
    return False

# Method 2 (much faster)
def finder2(numbers, k):
    for i in range(len(numbers)):
        complement = k - numbers[i]
        if complement >= 0:
            
            # so that the algorithm would'nt consider the element it is currenly checking as the complement. The -1 at the end is in case the number it is checking is a zero.
            numbers[i] = (numbers[i] * -1) -1
            
            if complement in numbers:
                return True
    return False


print(finder(numbers, k))
print(finder2(numbers, k))
