'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
Find the minimum element in O(log N) time. You may assume the array does not contain duplicates.

For example, given [5, 7, 10, 3, 4], return 3.
'''

Elements = [4,5,6,7,8,9,2,3]

# When a list has pivot point, the smallest number is the one right after the pivot point
# The recursive function used breaks the list in half, and checks if the middle element is greater or smaller than the 0th element to find the pivot point.
# It repeats this until only two items are left, and on comparison, the smaller one is returned.

def smallest(elements):
    print(elements)
    if len(elements) == 2:
        return elements[0] if elements[0] < elements[1] else elements[1]
    
    middle_index = int(len(elements)/2)

    # Checks if there is any pivot point
    if (elements[middle_index] > elements[0]) and (elements[middle_index] < elements[-1]):
        return elements[0]
    else:
        # If there was a pivot point, starts breaking the list in half, and checks for the half which contains the pivot point
        if elements[middle_index] < elements[0]:
            return smallest(elements[0:middle_index+1])

        if elements[middle_index] > elements[-1]:
            return smallest(elements[middle_index:])

print(smallest(Elements))