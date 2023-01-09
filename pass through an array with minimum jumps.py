'''
You are given an array of integers, where each element represents the maximum number of steps that can be jumped going forward from that element. Write a function to return the minimum number of jumps you must take in order to get from the start to the end of the array.

For example, given [6, 2, 4, 0, 5, 1, 1, 4, 2, 9], you should return 2, as the optimal solution involves jumping from 6 to 5, and then from 5 to 9.

Challenge: Show the actual jumps to get from the start to the end
'''

# Watch https://www.youtube.com/watch?v=cETfFsSTGJI for better understanding of the logic

items        = [6, 2, 4, 0, 5, 1, 1, 4, 2, 9]
no_jumps     = [0]
prev_index   = [0]

# Goes through the list one by one and checks the least number of steps required to reach that element
for i in range(1, len(items)):
    for j in range(i):
        # Checks if it's possible to reach items[i] from items[j]
        if items[j] >= (i - j):
            jumps = no_jumps[j] + 1
            try:
                # Checks if number of jumps to reach items[j] + 1 (from items[j] to items[i]) is lesser than number of jumps it took to reach items[i]
                if no_jumps[i] > jumps:
                    no_jumps = jumps
                    prev_index[i] = j
            # In case the number of jumps it took reach items[i] is not calculated yet
            except IndexError:
                no_jumps.append(jumps)
                prev_index.append(j)

# Shows the final answer
i = len(items) - 1 
temp = []  
while True:
    if i == 0:
        temp.append(items[0])
        break
    else:
        temp.append(items[i])
        i = prev_index[i]

print(f"In {no_jumps[-1]} jumps:")

# Challenge : Demonstrates every step taken from beginning to the end
for j in range(len(temp) - 1, -1, -1):
    if j == 0:
        print(temp[0])
    
    else:
        print(temp[j]," ---> ", end='')