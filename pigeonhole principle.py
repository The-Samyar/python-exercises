'''
You are given an array of length n + 1 whose elements belong to the set {1, 2, ..., n}.
By the pigeonhole principle, there must be a duplicate.
Find it in linear time and space.
'''

length = 7
elements = [1, 2, 3, 4, 5, 4, 6]

# //// Method 1

def MethodA(elements):
    element_count = {}
    
    for element in elements:
    
        if element in element_count:
            return element
        else:
            element_count[element] = 1

print(MethodA(elements))




# //// Method 2

# The duplicated number can be found by using the following formula. I used an example to show how it works:
# Let's say for length 3, we would have a list such as [1,2,2] and we call it list_a. Then its sum would be 1 + 2 + 2 = 5.
# If we wanted to generate a list with same length but no duplicated item, we would have [1,2,3]calling it list_b, with the sum 1 + 2 + 3 = 6. Note that the last item of this list is same as the length of the list. So if we were to remove the last item (that is equal to length of it) from the list_b, then we would have [1, 2]. Notice that after removing the last item, all the items in list_b, would be present in list_a plus an aditional item which would be the duplicated item.
# So, if we subtract the sum of the new list_b from the sum of list_a, what we are left with would be the duplicated item. 

def MethodB(elements):
    list_a_sum, list_b_sum = 0, 0
    # Finds the sum of both lists mentioned in the example, simultaneously.
    for i in range(len(elements)):
        list_a_sum += elements[i]
        list_b_sum += (i + 1)
    
    # Note that length of the list_b is same as the last item of list_b
    return list_a_sum - (list_b_sum - len(elements))

print(MethodB(elements))
