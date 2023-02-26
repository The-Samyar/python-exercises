'''
Given an array of numbers representing the stock prices of a company in chronological order and an integer k, return the maximum profit you can make from k buys and sells. You must buy the stock before you can sell it, and you must sell the stock before you can buy it again.

For example, given k = 2 and the array [5, 2, 4, 0, 1], you should return 3.
'''
# Algorithm used : https://www.youtube.com/watch?v=oDhu5uGq_ic

days = [2, 5, 7, 1, 2, 3, 2, 1]
k = 3
k += 1

table = [[0 for j in range(len(days))] for i in range(k)]

for i in range(1, k):
    max_diff = 0 - days[0]
    for j in (range(1, len(days))):
        a = table[i][j - 1]
        max_diff = max(max_diff, table[i - 1][j - 1] - days[j - 1])
        b = max_diff + days[j]
        table[i][j] = max(a, b)

i = len(table) - 1 
j = len(table[0]) - 1

texts = []
while i >= 0 and j >=0 :

    if table[i][j] == table[i][j-1]:
        j = j - 1
    else:
        texts.append(f"Sold at day {j+1} for {days[j]}.\n")
        
        profit_so_far = table[i][j] - days[j]
        for k in range(j,-1,-1):
            if (table[i-1][k] - days[k]) == profit_so_far:
                texts.append(f"Bought at day {k+1} for {days[k]}.\n")
                break
        i = i - 1
        j = k

for a in range(len(texts)-1, -1, -1):
    print(texts[a])

print(f"maximum profit : {table[-1][-1]}")