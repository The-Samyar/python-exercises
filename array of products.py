'''
Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i. For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].
'''

numbers = [1, 2, 3, 4, 5]

product_list = []
product = 1

# Calculates the product of all numbers in the list
for number in numbers:
    product *= number

# Divides the current number from the whole product and adds it to the list, so for example, the first number in product_list will have the product of the rest of the numbers
for number in numbers:
    product_list.append(int(product // number))

print(product_list)

# This algorithm works super efficently and calculates extremely large numbers like a charm