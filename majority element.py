'''
Given a list of elements, find the majority element, which appears more than half the time (> floor(len(lst) / 2.0)).

You can assume that such element exists.

For example, given [1, 2, 1, 1, 3, 4, 0], return 1.

Follow up: Solve the problem in linear time and in O(1) space
'''

elements = [1, 2, 1, 1, 3, 4, 0, 0, 0, 4, 4, 4, 4, 4, 4, 0, 0, 0, 4]


# Method 1

elements_count = {} # a dictionary consisted of every digit as key, and the number they are repeated as value

majority_element = elements[0]

for element in elements:
    if element in elements_count:
        # if element exists in the dictionary, increment the count by 1
        elements_count[element] += 1
    else:
        # if element exists doesn't exist, add it to the dictionary
        elements_count[element] = 1

    # swaps the element that is currently being checked with the majority element, if element is repeated more than the current majority element
    majority_element = element if elements_count[element] > elements_count[majority_element] else majority_element

print(majority_element)


# Method 2 (using Boyer Moore algorithm)
# at the first sight, this algorithm might confuse you. They only way to understand what is actually happening is to use a simple example, and then type the value of every variable for each iteration of the loop.

majority_element = 0
count = 0 # keeps the count of current majority_element

for element in elements:

    if element == majority_element:
        count += 1
    else:
        if count == 0:
            majority_element = element
            count = 1
        else:
            count -= 1
            
print(majority_element)

