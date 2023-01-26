'''
Given an array of elements, return the length of the longest subarray
where all of its elements are distinct.

For example, given the array [5, 1, 3, 5, 2, 3, 4, 1],
return 5 as the longest subarray of distinct elements is [5, 2, 3, 4, 1].

Extra : Return the subarray too.
'''
elements = [5, 1, 3, 5, 2, 3, 4, 1]

# Stores numbers and their indexes
data = {}

# Stores the length, starting index and ending index of the largest sublist by far. I used class in order to save the data because it seemed easier to me. Of course it is ok to use other data structures like list or dictionary and get the same result.
class largest_sublist:
    count = 1
    start_index = 0
    end_index = 0

ls = largest_sublist()

# Stores the length of the sublist it is checking. The moment a number is repeated, it is set to zero
new_count = 0

i = 0
while i < len(elements):
    # The following condition is met when the number (elements[i]) is not present in the data dictionary
    if elements[i] not in data:
        data[elements[i]] = i
        new_count += 1
        if ls.count < new_count:
            ls.count = new_count
            ls.start_index = next(iter(data.values()))
            ls.end_index = i
        i += 1

    # This condition happens when the number that is being checked had been already added before, so the current element would be the second occurance of it, so this would be the end of the current sublist, and data is cleared to be used for the next sublist.
    else:
        new_count = 0

        # The reason I used this line is to skip the first occurance of the repeated number, and begin the new sublist with the number after it.
        i = data[elements[i]] + 1

        data = {}


print(f"Longest sublist with distinct items: \n{elements[ls.start_index:ls.end_index+1]}\nwith {ls.count} item(s)")