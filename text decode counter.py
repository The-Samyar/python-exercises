# Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

# For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

# You can assume that the messages are decodable. For example, '001' is not allowed.

'''
Logic explanation:
I used a recursive approach for this problem. Let's say we have an empty string n = ''. The different combinations that n can be divided into groups of length one and two would be 0.
If n = '1', the groupings would be:
1:
1
Now consider n = '12'. Then combinations would be:
12:
1 2
12

If you look closely, we can obtain the groupings of string '12' by using grouping combinations of '1' and ''. We take all the combinations for '1' and add the last character of n, and we take the combinations of '' and add the last two characters of n:
1 2 --> '1' and the last character of n, '2' 
12 --> combinations for '' and the last two characters of n

If n = '123', then we need to consider for '12' and '1':
for '12':
1 2 3
12 3
for '1':
1 23

If n = '1234', we consider '123' and '12':
for '123':
1 2 3 4
12 3 4
1 23 4
for '12':
1 2 34
12 34

So in general, for a string of length X, we need to add Xth element at the end of all of the grouping combinations of string X-1, and add 'X-1'th and 'X'th element together as a two digit number at the end of all of the combinations that string X-2 would have and count all of the obtained combinations.
Note that in the process of finding each combination, if the two digit number created by X-1 and X is not in range 1 to 26, then skip counting that combination as it contains an element that is out of the required range.
'''

# Recursive
message = list(str(123456))
def recursive(message):
    combinations = []

    if len(message) == 0:
        combinations.append([])
        return combinations
    if len(message) == 1:
        combinations.append(message)
        return combinations

    fst_grp = recursive(message[:-1])
    for item in fst_grp:
        item.append(message[-1])
        combinations.append(item)

    sec_grp = recursive(message[:-2])
    for item in sec_grp:
        if 0 < int(message[-2] + message[-1]) < 27:
            item.append(message[-2] + message[-1])
            combinations.append(item)

    return combinations

print(len(recursive(message)))